from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_analytics

router = APIRouter()

@router.get("/analytics/{short_code}")
def analytics(short_code: str, db: Session = Depends(get_db)):
    total, ref, devices = get_analytics(db, short_code)
    return {
        "total_clicks": total,
        "referrers": ref,
        "devices": devices
    }