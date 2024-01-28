from fastapi import APIRouter, HTTPException
from starlette import status
from schema.request_body import RequestBody
from services.services import find_fact_process


router = APIRouter()


router.get("/health")
async def test_api():
    return {"status_code": status.HTTP_200_OK}


router.post(path="/fact_finder")
async def fact_finder(request_body: RequestBody):
    if not isinstance(request_body, RequestBody):
        raise HTTPException(status_code=400, detail="Некорректный формат \
            запроса")
    return await find_fact_process(request_body=request_body)
