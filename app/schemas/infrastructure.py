from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ServerBase(BaseModel):
    name: str
    ip_address: str
    hostname: str


class ServerCreate(ServerBase):
    pass


class ServerUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    cpu_usage: Optional[float] = None
    memory_usage: Optional[float] = None


class ServerResponse(ServerBase):
    id: int
    status: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DomainBase(BaseModel):
    name: str
    provider: str


class DomainCreate(DomainBase):
    expiry_date: datetime
    auto_renew: bool = True


class DomainUpdate(BaseModel):
    provider: Optional[str] = None
    auto_renew: Optional[bool] = None


class DomainResponse(DomainBase):
    id: int
    status: str
    expiry_date: datetime
    auto_renew: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NetworkBase(BaseModel):
    name: str
    cidr: str
    gateway: str


class NetworkCreate(NetworkBase):
    pass


class NetworkUpdate(BaseModel):
    name: Optional[str] = None
    gateway: Optional[str] = None


class NetworkResponse(NetworkBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class WebsiteBase(BaseModel):
    name: str
    domain_id: int
    server_id: int


class WebsiteCreate(WebsiteBase):
    pass


class WebsiteUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None


class WebsiteResponse(WebsiteBase):
    id: int
    status: str
    uptime_percentage: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
