from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from ..security.api_key import verify_api_key
import asyncio

router = APIRouter(
    prefix="/api/stream",
    tags=["realtime"],
    dependencies=[Depends(verify_api_key)],
)

async def event_generator(message: str):
    yield f"data: {message}\n\n"
    await asyncio.sleep(0.01)

@router.get("/campaign/{id}")
async def stream_campaign(id: int):
    async def generator():
        async for _ in asyncio.as_completed([asyncio.sleep(0.1)]):
            yield f"data: campaign {id} progress\n\n"
    return StreamingResponse(generator(), media_type="text/event-stream")

@router.get("/system")
async def stream_system():
    return StreamingResponse(event_generator("system"), media_type="text/event-stream")

@router.get("/uploads")
async def stream_uploads():
    return StreamingResponse(event_generator("uploads"), media_type="text/event-stream")
