# Big Data Backend API

A production-ready backend prototype for managing big data infrastructure including websites, servers, domains, and network management.

## Architecture

```
app/
  ├── api/          # API routes and endpoints
  ├── models/       # SQLAlchemy database models
  ├── schemas/      # Pydantic request/response schemas
  ├── services/     # Business logic services
  ├── workers/      # Celery async tasks
  ├── main.py       # FastAPI application entry point
  └── database.py   # Database configuration

infrastructure/
  ├── docker/       # Docker configurations
  │   ├── Dockerfile
  │   ├── Dockerfile.worker
  │   └── docker-compose.yml
  └── terraform/    # AWS infrastructure as code

config/
  └── settings.py   # Application configuration

tests/
  └── test_api.py   # API tests
```

## Features

- **FastAPI**: Modern async web framework
- **PostgreSQL**: Relational database for structured data
- **Redis**: In-memory cache and Celery broker
- **Celery**: Async task queue for background jobs
- **Docker Compose**: Local development environment
- **Terraform**: AWS infrastructure provisioning (ECS, RDS, ElastiCache, ALB)
- **API Endpoints**: Manage servers, domains, networks, and websites

## Quick Start

### Local Development (Docker Compose)

1. **Clone and setup**:
   ```bash
   cd c:\Users\mhmmd\testing_back
   cp .env.example .env
   ```

2. **Start services**:
   ```bash
   docker-compose -f infrastructure/docker/docker-compose.yml up -d
   ```

3. **Access the API**:
   - API: http://localhost:7000
   - Docs: http://localhost:7000/docs
   - Flower (Celery): http://localhost:5555

4. **Stop services**:
   ```bash
   docker-compose -f infrastructure/docker/docker-compose.yml down
   ```

### Local Development (Manual)

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start PostgreSQL and Redis** (separately)

3. **Set environment variables** (.env file)

4. **Run the application**:
   ```bash
   python -m app.main
   ```

5. **Run Celery worker**:
   ```bash
   celery -A app.workers.celery_app worker --loglevel=info
   ```

## API Endpoints

### Servers
- `GET /api/v1/infrastructure/servers` - List all servers
- `POST /api/v1/infrastructure/servers` - Create a server

### Domains
- `GET /api/v1/infrastructure/domains` - List all domains
- `POST /api/v1/infrastructure/domains` - Create a domain

### Networks
- `GET /api/v1/infrastructure/networks` - List all networks
- `POST /api/v1/infrastructure/networks` - Create a network

### Websites
- `GET /api/v1/infrastructure/websites` - List all websites
- `POST /api/v1/infrastructure/websites` - Create a website

## Background Tasks (Celery)

- `monitor_server(server_id)` - Monitor server health
- `sync_domain_dns(domain_id)` - Sync domain DNS
- `backup_server_data(server_id)` - Backup server data
- `analyze_network_traffic(network_id)` - Analyze network patterns

## AWS Deployment (Terraform)

### Prerequisites
- AWS Account
- Terraform installed
- AWS CLI configured

### Deploy

1. **Configure Terraform**:
   ```bash
   cd infrastructure/terraform
   ```

2. **Initialize**:
   ```bash
   terraform init
   ```

3. **Plan**:
   ```bash
   terraform plan -var="environment=prod"
   ```

4. **Apply**:
   ```bash
   terraform apply -var="environment=prod"
   ```

### Infrastructure Provisioned
- VPC with public/private subnets
- Application Load Balancer
- ECS Fargate for containerized workloads
- RDS PostgreSQL database
- ElastiCache Redis
- Security groups and IAM roles
- CloudWatch logging

## Testing

Run tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=app
```

## Environment Variables

See `.env.example` for all available configuration options.

Key variables:
- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection string
- `CELERY_BROKER_URL` - Celery message broker (Redis)
- `AWS_REGION` - AWS region for deployment
- `DOMAIN_PROVIDER` - DNS provider (route53, cloudflare)

## Development Workflow

1. Create a feature branch
2. Make changes
3. Run tests: `pytest`
4. Format code: `black app tests`
5. Lint code: `flake8 app tests`
6. Type check: `mypy app`
7. Create pull request

## Monitoring & Logging

- **Flower**: Celery task monitoring at http://localhost:5555
- **CloudWatch**: AWS logs in production
- **Health Check**: GET /health endpoint

## Production Checklist

- [ ] Set up S3 bucket for Terraform state
- [ ] Configure AWS credentials
- [ ] Update environment variables
- [ ] Set up database backups
- [ ] Configure domain DNS
- [ ] Set up monitoring/alerting
- [ ] Configure SSL/TLS certificates
- [ ] Set up log aggregation
- [ ] Configure auto-scaling policies

## License

MIT
