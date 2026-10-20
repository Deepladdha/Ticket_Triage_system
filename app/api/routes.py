from fastapi import APIRouter
from app.models.ticket import TicketResponse, TicketSubmission
from app.services.classifier import classify_ticket





router = APIRouter()



@router.post("/tickets", response_model= TicketResponse)
async def create_ticket(submission: TicketSubmission):
    combined_text = f"{submission.title}\n\n{submission.body}"
    classification = await classify_ticket(combined_text)

    return TicketResponse(
        submission= submission,
        classification= classification
    )

