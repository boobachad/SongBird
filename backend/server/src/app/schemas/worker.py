import uuid
from enum import StrEnum

from pydantic import BaseModel


class IncomeBand(StrEnum):
    LOW = "LOW"
    MID = "MID"
    HIGH = "HIGH"
    ULTRA = "ULTRA"
    # about the above instead of tieing to bands why
    # not accoding to income levels needs more thinking on this
    # cause someone might be too low even for the low band
    # or too high even for the utlra band


class KycStatus(StrEnum):
    MOCK_VERIFIED = "mock_verified"
    VERIFIED = "verified"
    PENDING = "pending"
    REJECTED = "rejected"


class WorkerRegister(BaseModel):
    name: str
    phone_number: str
    platform_id: str
    city: str
    zone_id: str
    income_band: IncomeBand
    aadhaar_last4: str  # mock KYC last 4 digits only


class WorkerLoginRequest(BaseModel):
    phone_number: str
    otp: str


class WorkerRead(BaseModel):
    id: uuid.UUID
    name: str
    phone_number: str
    platform_id: str
    city: str
    zone_id: str
    income_band: IncomeBand
    kyc_status: KycStatus

    model_config = {"from_attributes": True}
