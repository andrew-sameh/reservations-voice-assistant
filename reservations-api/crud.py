from sqlalchemy.orm import Session
from models import Reservation, ReservationCreate, ReservationUpdate

# Reservations
def get_reservation(db: Session, reservation_id: int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def list_reservations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reservation).offset(skip).limit(limit).all()

def create_reservation(db: Session, reservation: ReservationCreate):
    new_reservation = Reservation(**reservation.dict())
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation

def delete_reservation(db: Session, reservation_id: int):
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not reservation:
        return None

    db.delete(reservation)
    db.commit()
    return reservation

def update_reservation(db: Session, reservation_id: int, reservation: ReservationUpdate):
    existing_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not existing_reservation:
        return None

    for key, value in reservation.dict(exclude_unset=True).items():
        if value is not None:
            setattr(existing_reservation, key, value)

    db.commit()
    db.refresh(existing_reservation)
    return existing_reservation