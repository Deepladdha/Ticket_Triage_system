from pydantic import BaseModel,Field, EmailStr
from enum import Enum
from typing import Literal
from datetime import datetime, UTC
import uuid


class TicketCategory(str ,Enum):
    ORDER = "order"
    BILLING = "billing" 
    TECHNICAL = "technical"
    ACCOUNT = "account"
    OTHER = "other"

class TicketClassification(BaseModel):
    category : TicketCategory
    urgency : int = Field(default=5,description="1 indicates lowest urgency increasing upto 5 which indicates highest urgency ",ge=1, le=5)
    sentiment : Literal["positive","neutral","negative"]

class TicketSubmission(BaseModel):
    email : EmailStr
    title : str = Field(..., min_length=2,max_length=100)
    body : str = Field(..., min_length=2,max_length=1000)
    time : datetime = Field(default_factory = lambda : datetime.now(UTC)) 

class TicketResponse(BaseModel):
    submission : TicketSubmission
    classification : TicketClassification
    id : uuid.UUID = Field(default_factory= uuid.uuid4)








