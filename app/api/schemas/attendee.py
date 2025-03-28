from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class AttendeeBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone_number: Optional[str] = None

class AttendeeCreate(AttendeeBase):
    event_id: int

class Attendee(AttendeeBase):
    attendee_id: int
    event_id: int
    check_in_status: bool

    class Config:
        from_attributes = True