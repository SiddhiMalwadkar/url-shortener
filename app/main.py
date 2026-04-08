from fastapi import FastAPI, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.schemas import URLCreate
from app.crud import create_short_url, get_url, log_click
from app.analytics import router as analytics_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(analytics_router)


@app.post("/shorten")
def shorten_url(data: URLCreate, db: Session = Depends(get_db)):
    short_url = create_short_url(db, data.original_url)
    return {"short_url": short_url}


@app.get("/{short_code}")
def redirect(short_code: str, request: Request, db: Session = Depends(get_db)):
    url = get_url(db, short_code)

    if not url:
        return {"error": "URL not found"}

    referrer = request.headers.get("referer", "direct")
    ip = request.client.host
    user_agent = request.headers.get("user-agent", "unknown")

    log_click(db, short_code, referrer, ip, user_agent)

    return RedirectResponse(url.original_url)