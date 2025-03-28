# app/services/event_service.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.api.models.event import Event, EventStatus
from app.api.schemas import event as event_schema
from datetime import datetime

class EventService:
    @staticmethod
    def create_event(db: Session, event: event_schema.EventCreate):
        db_event = Event(**event.model_dump())
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event

    @staticmethod
    def update_event(db: Session, event_id: int, event_update: event_schema.EventUpdate):
        db_event = db.query(Event).filter(Event.event_id == event_id).first()
        if not db_event:
            return None

        update_data = event_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_event, key, value)

        db.commit()
        db.refresh(db_event)
        return db_event

    @staticmethod
    def list_events(db: Session, status: str = None, location: str = None, start_date: datetime = None):
        query = db.query(Event)
        if status:
            query = query.filter(Event.status == status)
        if location:
            query = query.filter(Event.location.ilike(f"%{location}%"))
        if start_date:
            query = query.filter(func.date(Event.start_time) == func.date(start_date))
        return query.all()