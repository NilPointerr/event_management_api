from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from app.api.models.event import EventStatus

class EventBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    location: str
    max_attendees: int = Field(gt=0)

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    location: Optional[str] = None
    max_attendees: Optional[int] = None
    status: Optional[EventStatus] = None

class Event(EventBase):
    event_id: int
    status: EventStatus

    class Config:
        from_attributes = True