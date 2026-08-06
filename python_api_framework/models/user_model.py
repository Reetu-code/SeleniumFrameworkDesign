from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict


class GeoModel(BaseModel):
    lat: Optional[str] = None
    lng: Optional[str] = None


class AddressModel(BaseModel):
    street: Optional[str] = None
    suite: Optional[str] = None
    city: Optional[str] = None
    zipcode: Optional[str] = None
    geo: Optional[GeoModel] = None


class CompanyModel(BaseModel):
    name: Optional[str] = None
    catchPhrase: Optional[str] = None
    bs: Optional[str] = None


class UserModel(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: Optional[int] = None
    name: str
    username: Optional[str] = None
    email: Optional[str] = None
    address: Optional[AddressModel] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    company: Optional[CompanyModel] = None


class CreateUserRequest(BaseModel):
    name: str
    username: str
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None


class UserResponseModel(UserModel):
    """Pydantic model representing User API response."""
    pass
