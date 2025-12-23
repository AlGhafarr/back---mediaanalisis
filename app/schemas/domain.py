from pydantic import BaseModels
from typing import Optional
from datetime import datetime

class DomainBase(BaseModels):
    name: str
    description: Optional[str] = None
    status: str = "active"

class DomainCreate(DomainBase):
    pass

class DomainUpdate(BaseModels):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class DomainResponse(DomainBase):
    id: int
    created_by: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class config:
        from_attributes = True
        