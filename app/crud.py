from sqlalchemy.orm import Session
from app import models
from app.utils import encode_base62

BASE_URL = "http://localhost:8000/"

def create_short_url(db: Session, original_url: str):
    new_url = models.URL(original_url=original_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    short_code = encode_base62(new_url.id)
    new_url.short_code = short_code

    db.commit()
    db.refresh(new_url)

    return BASE_URL + short_code


def get_url(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()


def log_click(db: Session, short_code: str, referrer: str, ip: str, user_agent: str):
    click = models.Click(
        short_code=short_code,
        referrer=referrer,
        ip_address=ip,
        user_agent=user_agent
    )
    db.add(click)
    db.commit()


def get_analytics(db: Session, short_code: str):
    clicks = db.query(models.Click).filter(models.Click.short_code == short_code).all()

    total = len(clicks)
    ref_count = {}
    devices = {}

    for c in clicks:
        ref = c.referrer or "direct"
        ref_count[ref] = ref_count.get(ref, 0) + 1

        device = c.user_agent or "unknown"
        devices[device] = devices.get(device, 0) + 1

    return total, ref_count, devices