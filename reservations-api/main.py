import logging
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from models import (
    ReservationCreate,
    ReservationUpdate,
    ReservationResponse,
    SessionLocal,
)
from starlette.middleware.cors import CORSMiddleware
import crud
logger = logging.getLogger("api")
logger.setLevel(logging.INFO)

# FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoints

@app.get("/reservations", response_model=list[ReservationResponse], tags=["reservations"])
def list_reservations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reservations = crud.list_reservations(db, skip, limit)
    return reservations


@app.post("/reservations", response_model=ReservationResponse, tags=["reservations"])
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    new_reservation = crud.create_reservation(db, reservation)
    return new_reservation


@app.get("/reservations/{reservation_id}", response_model=ReservationResponse, tags=["reservations"])
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = crud.get_reservation(db, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@app.put("/reservations/{reservation_id}", response_model=ReservationResponse, tags=["reservations"])
def update_reservation(
    reservation_id: int, reservation: ReservationUpdate, db: Session = Depends(get_db)
):
    updated_reservation = crud.update_reservation(db, reservation_id, reservation)
    return updated_reservation

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
