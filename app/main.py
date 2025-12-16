from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, UrlMapping, Click
from schemas import ShortenRequest, ShortenResponse, StatsResponse
from utils import encode_base62

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener with Analytics")


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST /api/shorten
@app.post("/api/shorten", response_model=ShortenResponse)
def shorten_url(request: ShortenRequest, db: Session = Depends(get_db)):
    # Convert HttpUrl to string before storing in DB
    url = UrlMapping(original_url=str(request.original_url))
    db.add(url)
    db.commit()
    db.refresh(url)

    # Generate unique Base62 short code
    short_code = encode_base62(url.id)
    url.short_code = short_code
    db.commit()

    return {"short_code": short_code}


# GET /{short_code} -> Redirect
@app.get("/{short_code}")
def redirect_url(short_code: str, request: Request, db: Session = Depends(get_db)):
    url = db.query(UrlMapping).filter_by(short_code=short_code).first()
    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    # Record click analytics
    click = Click(
        url_id=url.id,
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )
    db.add(click)
    db.commit()

    # 302 Temporary Redirect
    return RedirectResponse(url=url.original_url, status_code=302)


# GET /api/stats/{short_code}
@app.get("/api/stats/{short_code}", response_model=StatsResponse)
def get_stats(short_code: str, db: Session = Depends(get_db)):
    url = db.query(UrlMapping).filter_by(short_code=short_code).first()
    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    total_clicks = db.query(Click).filter_by(url_id=url.id).count()

    return {
        "short_code": short_code,
        "total_clicks": total_clicks
    }
