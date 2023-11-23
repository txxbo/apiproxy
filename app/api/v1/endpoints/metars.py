from fastapi import APIRouter
from app.dependencies import db

router = APIRouter()

@router.get("/metars")
async def read_items(output: str = "JSON"):
    """Read items from file.
    
    Args:
        output (str): Output type (JSON or XML)
    Return:
        str: formatted data stored from last API call.
    """
    data =  db.read_items(output.upper())
    return data
