from fastapi import APIRouter
from base_web.healthcheck_module.controller import HealthCheckController

router = APIRouter()
controller = HealthCheckController()

@router.get("/")
async def read_root():
    return await controller.get_health_check()