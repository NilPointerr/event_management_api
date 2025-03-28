from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.core.database import get_db
from app.api.services.event_service import EventService
from app.api.schemas import event as event_schema
from typing import List, Optional
from datetime import datetime

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/", response_model=event_schema.Event)
def create_event(event: event_schema.EventCreate, db: Session = Depends(get_db)):
    try:
        return EventService.create_event(db, event)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{event_id}", response_model=event_schema.Event)
def update_event(event_id: int, event: event_schema.EventUpdate, db: Session = Depends(get_db)):
    updated_event = EventService.update_event(db, event_id, event)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.get("/", response_model=List[event_schema.Event])
def list_events(
    status: Optional[str] = None, 
    location: Optional[str] = None, 
    start_date: Optional[datetime] = None, 
    db: Session = Depends(get_db)
):
    return EventService.list_events(db, status, location, start_date)