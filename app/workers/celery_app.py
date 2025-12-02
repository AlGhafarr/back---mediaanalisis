from celery import Celery
from config.settings import settings

celery_app = Celery(
    "bigdata_backend",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@celery_app.task
def monitor_server(server_id: int):
    """Monitor server health and metrics."""
    print(f"Monitoring server {server_id}")
    return {"server_id": server_id, "status": "monitored"}


@celery_app.task
def sync_domain_dns(domain_id: int):
    """Sync domain DNS records."""
    print(f"Syncing domain {domain_id}")
    return {"domain_id": domain_id, "status": "synced"}


@celery_app.task
def backup_server_data(server_id: int):
    """Backup server data."""
    print(f"Backing up server {server_id}")
    return {"server_id": server_id, "status": "backed_up"}


@celery_app.task
def analyze_network_traffic(network_id: int):
    """Analyze network traffic patterns."""
    print(f"Analyzing network {network_id}")
    return {"network_id": network_id, "status": "analyzed"}
