from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/infrastructure", tags=["infrastructure"])


@router.get("/servers")
async def list_servers(db: Session = Depends(get_db)):
    """List all managed servers."""
    return {
        "servers": [
            {
                "id": 1,
                "name": "Server 1",
                "ip": "192.168.1.10",
                "status": "running",
                "cpu_usage": 45.2,
                "memory_usage": 72.5,
            }
        ]
    }


@router.post("/servers")
async def create_server(server_data: dict, db: Session = Depends(get_db)):
    """Create a new server entry."""
    return {"message": "Server created", "data": server_data}


@router.get("/domains")
async def list_domains(db: Session = Depends(get_db)):
    """List all managed domains."""
    return {
        "domains": [
            {
                "id": 1,
                "name": "example.com",
                "provider": "route53",
                "status": "active",
                "expiry_date": "2025-12-31",
            }
        ]
    }


@router.post("/domains")
async def create_domain(domain_data: dict, db: Session = Depends(get_db)):
    """Create a new domain entry."""
    return {"message": "Domain created", "data": domain_data}


@router.get("/networks")
async def list_networks(db: Session = Depends(get_db)):
    """List all managed networks."""
    return {
        "networks": [
            {
                "id": 1,
                "name": "Production Network",
                "cidr": "10.0.0.0/16",
                "status": "active",
            }
        ]
    }


@router.post("/networks")
async def create_network(network_data: dict, db: Session = Depends(get_db)):
    """Create a new network entry."""
    return {"message": "Network created", "data": network_data}


@router.get("/websites")
async def list_websites(db: Session = Depends(get_db)):
    """List all managed websites."""
    return {
        "websites": [
            {
                "id": 1,
                "name": "Main Website",
                "domain": "example.com",
                "server_id": 1,
                "status": "online",
                "uptime_percentage": 99.95,
            }
        ]
    }


@router.post("/websites")
async def create_website(website_data: dict, db: Session = Depends(get_db)):
    """Create a new website entry."""
    return {"message": "Website created", "data": website_data}
