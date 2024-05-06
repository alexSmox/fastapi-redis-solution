from fastapi import APIRouter, Depends, HTTPException, status

from .dependencies import get_redis_client
from .schemas import PhoneBookRecord, PhoneBookRecordCreate

router = APIRouter()


@router.get(
    "/check_data", response_model=PhoneBookRecord, status_code=status.HTTP_200_OK
)
async def get_one_record(phone_number: str, redis_client=Depends(get_redis_client)):
    record = redis_client.get(phone_number)
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return PhoneBookRecord(adres=record)


@router.post(
    "/write_data",
    response_model=PhoneBookRecordCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_one_record(
    data: PhoneBookRecordCreate, redis_client=Depends(get_redis_client)
):
    redis_client.set(data.phone_number, data.address)
    return PhoneBookRecordCreate(phone_number=data.phone_number, address=data.address)
