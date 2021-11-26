from fastapi import APIRouter


router = APIRouter(
    prefix="/tickets",
    tags=["tickets"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_tickets():
    return "Estos son todos los tickets"


@router.get("/{ticket_id}")
async def read_item(ticket_id: str):
    return "Esto es un ticket con id" + ticket_id
