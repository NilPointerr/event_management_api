from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from app.api.core.database import get_db
from app.api.services.attendee_service import AttendeeService
from app.api.schemas import attendee as attendee_schema
from typing import List
    
router = APIRouter(prefix="/attendees", tags=["attendees"])

@router.post("/register", response_model=attendee_schema.Attendee)
def register_attendee(attendee: attendee_schema.AttendeeCreate, db: Session = Depends(get_db)):
    try:
        return AttendeeService.register_attendee(db, attendee)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{event_id}/check-in/{attendee_id}")
def check_in_attendee(event_id: int, attendee_id: int, db: Session = Depends(get_db)):
    try:
        return AttendeeService.check_in_attendee(db, event_id, attendee_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{event_id}/bulk-check-in")
def bulk_check_in(event_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        result = AttendeeService.bulk_check_in(db, event_id, file.file)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))