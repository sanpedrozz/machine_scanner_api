# routers.py

from fastapi import APIRouter

from models import SendMessageRequest
from services import ComPortService
from logger import logger

router = APIRouter()
com_port_service = ComPortService()


@router.get("/list-com-ports/")
async def read_list_com_ports():
    return com_port_service.virtual_com_ports_list


@router.get("/api-com-port/")
async def read_api_com_port():
    return com_port_service.api_com_port


@router.get("/machine-com-ports/")
async def read_machine_com_port():
    return com_port_service.machine_com_port


@router.post("/send-message/")
async def send_message(request: SendMessageRequest):
    success = com_port_service.send_to_com_port(request.id)
    return {"success": success, "message": request.id}
