from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from auth import router as auth_router, get_current_user

from response import response_ok
import models, schemas

router = APIRouter(tags=["hasil kalkulasi"])

# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create table 'hasil kalkulasi' when not exist
models.Base.metadata.create_all(bind=engine, tables=[models.HasilKalkulasi.__table__])

# CREATE GROUP TRAFO
@router.post("/hasil-kalkulasi/save", response_model=schemas.HasilKalkulasi)
def create_hasil_kalkulasi(group_trafo: schemas.HasilKalkulasiCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_hasil_kalkulasi = models.HasilKalkulasi(**group_trafo.dict(), owner_id=current_user.id)
    db.add(new_hasil_kalkulasi)
    db.commit()
    db.refresh(new_hasil_kalkulasi)
    return new_hasil_kalkulasi

# UPDATE
@router.post("/hasil-kalkulasi/update/{id}", response_model=schemas.HasilKalkulasi)
def update_hasil_kalkulasi(id: int, hasil_kalkulasi: schemas.HasilKalkulasiCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_hasil_kalkulasi = db.query(models.HasilKalkulasi).filter(models.HasilKalkulasi.id == id, models.HasilKalkulasi.owner_id == current_user.id).first()
    if not db_hasil_kalkulasi:
        raise HTTPException(status_code=404, detail="Hasil Kalkulasi not found")
    for key, value in hasil_kalkulasi.dict().items():
        setattr(db_hasil_kalkulasi, key, value)
    db.commit()
    db.refresh(db_hasil_kalkulasi)
    return response_ok(data=None, message="Hasil Kalkulasi updated")
