from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.domain import  MediaDomain
from app.models.user import User
from app.schemas.domain import DomainCreate, DomainUpdate, DomainResponse
from app.core.security import get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[DomainResponse])
def list_domains(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """List all domains"""
    domains = db.query(MediaDomain).offset(skip).limit(limit).all()
    return domains


@router.post("/", response_model=DomainResponse, status_code=status.HTTP_201_CREATED)
def create_domain(
    domain_data: DomainCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new domain"""
    if db.query(Domain).filter(Domain.name == domain_data.name).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Domain name already exists"
        )
    
    db_domain = Domain(
        **domain_data.dict(),
        created_by=current_user.id
    )
    
    db.add(db_domain)
    db.commit()
    db.refresh(db_domain)

    return db_domain



@router.get("/{domain_id}", response_model=DomainResponse)
def get_domain(
    domain_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get domain by ID"""
    domain = db.query(Domain).filter(Domain.id == domain_id).first()
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    return domain


@router.put("/{domain_id}", response_model=DomainResponse)
def update_domain(
    domain_id: int,
    domain_update: DomainUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update domain"""
    domain = db.query(Domain).filter(Domain.id == domain_id).first()
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    update_data = domain_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(domain, field, value)
    
    db.commit()
    db.refresh(domain)
    
    return domain

@router.delete("/{domain_id}")
def delete_domain(
    domain_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Delete domain"""
    domain = db.query(Domain).filter(Domain.id == domain_id).first()
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    db.delete(domain)
    db.commit()
    
    return {"message": "Domain deleted successfully"}