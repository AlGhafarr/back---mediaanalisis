# Big Data Backend - Project Setup Complete

This is a production-ready backend prototype for managing big data infrastructure (websites, servers, domains, networks).

## Project Overview

**Stack**: FastAPI + PostgreSQL + Redis + Celery + Docker + Terraform/AWS

**Key Components**:
- RESTful API for infrastructure management
- Async task queue for background jobs
- Docker Compose for local development
- Terraform for AWS cloud deployment
- Comprehensive test suite

## What's Included

### Backend Code
- **API Routes**: Endpoints for servers, domains, networks, websites
- **Database Models**: SQLAlchemy ORM models
- **Services**: Business logic and operations
- **Celery Tasks**: Async job processing
- **Pydantic Schemas**: Request/response validation

### Infrastructure
- **Docker Compose**: PostgreSQL, Redis, API, Celery Worker, Flower monitoring
- **Terraform**: AWS infrastructure (ECS, RDS, ElastiCache, ALB, VPC, Security Groups)

### Configuration & Tools
- Environment setup (.env.example)
- Makefile for common commands
- pytest for testing
- Type hints and linting ready

## Getting Started

### Option 1: Docker Compose (Recommended for Local Dev)

```bash
cd c:\Users\mhmmd\testing_back

# Copy environment template
copy .env.example .env

# Start all services
docker-compose -f infrastructure/docker/docker-compose.yml up -d

# Access API: http://localhost:7000/docs
# Celery monitoring: http://localhost:5555
```

### Option 2: Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set up database and Redis separately
# Then run:
python -m app.main

# In another terminal, run Celery worker:
celery -A app.workers.celery_app worker --loglevel=info
```

### Option 3: AWS Deployment

```bash
cd infrastructure/terraform

# Configure variables
copy terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your values

# Deploy
terraform init
terraform plan
terraform apply
```

## API Endpoints

All endpoints are under `/api/v1/infrastructure/`:

**Servers**
- `GET /servers` - List servers
- `POST /servers` - Create server

**Domains**
- `GET /domains` - List domains
- `POST /domains` - Create domain

**Networks**
- `GET /networks` - List networks
- `POST /networks` - Create network

**Websites**
- `GET /websites` - List websites
- `POST /websites` - Create website

**Health**
- `GET /health` - Health check

## Project Structure

```
testing_back/
├── app/
│   ├── api/routes.py           # API endpoints
│   ├── models/infrastructure.py # Database models
│   ├── schemas/infrastructure.py# Request/response schemas
│   ├── services/infrastructure.py# Business logic
│   ├── workers/celery_app.py   # Async tasks
│   ├── main.py                 # FastAPI app
│   └── database.py             # DB config
├── infrastructure/
│   ├── docker/                 # Docker files & Compose
│   └── terraform/              # AWS IaC
├── config/settings.py          # App settings
├── tests/test_api.py           # Tests
├── requirements.txt            # Dependencies
├── README.md                   # Full documentation
├── DEVELOPMENT.md              # Detailed dev guide
├── Makefile                    # Common commands
└── .env.example                # Environment template
```

## Key Files

| File | Purpose |
|------|---------|
| `app/main.py` | FastAPI application entry point |
| `app/api/routes.py` | All API endpoint definitions |
| `app/models/infrastructure.py` | Database models |
| `app/workers/celery_app.py` | Async tasks |
| `docker-compose.yml` | Local dev environment |
| `infrastructure/terraform/` | AWS infrastructure as code |
| `requirements.txt` | Python dependencies |

## Development Workflow

1. **Make code changes** in `app/` directory
2. **Add tests** in `tests/` directory
3. **Run tests**: `pytest`
4. **Format code**: `black app`
5. **Check types**: `mypy app`
6. **Lint**: `flake8 app`
7. **Commit** and push

## Useful Commands

```bash
# Using Makefile
make help              # Show all commands
make docker-up        # Start services
make docker-down      # Stop services
make test             # Run tests
make lint             # Check code
make format           # Format code

# Manual commands
pytest tests/                    # Run tests
black app tests                  # Format code
mypy app                        # Type checking
flake8 app tests                # Linting
docker-compose logs -f          # View logs
```

## Configuration

Edit `.env` file to customize:
- Database credentials
- Redis connection
- Celery settings
- API host/port
- CORS origins
- AWS region and credentials

See `.env.example` for all available options.

## Database

PostgreSQL database with models for:
- Servers (name, IP, CPU/memory/disk usage)
- Domains (name, provider, expiry, auto-renew)
- Networks (name, CIDR, gateway)
- Websites (name, domain, server, uptime)

## Background Tasks

Celery tasks for:
- Server monitoring
- Domain DNS sync
- Server data backup
- Network traffic analysis

Monitor tasks in Flower UI: http://localhost:5555

## AWS Deployment

Terraform provisions:
- VPC with public/private subnets (multi-AZ)
- Application Load Balancer
- ECS Fargate cluster
- RDS PostgreSQL database
- ElastiCache Redis
- CloudWatch logging
- Security groups and IAM roles

## Testing

```bash
pytest              # Run all tests
pytest -v           # Verbose output
pytest --cov=app    # With coverage
pytest -k test_api  # Run specific tests
```

## Next Steps

1. **Customize models** in `app/models/` for your needs
2. **Add API endpoints** in `app/api/routes.py`
3. **Create Celery tasks** in `app/workers/celery_app.py`
4. **Add tests** in `tests/`
5. **Update Terraform** in `infrastructure/terraform/` for AWS
6. **Configure environment** in `.env`
7. **Run locally** with Docker Compose
8. **Deploy** to AWS using Terraform

## Documentation

- **README.md**: Full feature overview and quick start
- **DEVELOPMENT.md**: Detailed development guide
- **Makefile**: Common commands
- **requirements.txt**: All dependencies

## Support

Check the API documentation at:
- Swagger UI: http://localhost:7000/docs
- ReDoc: http://localhost:7000/redoc

---

**Ready to develop! Start with Docker Compose or read README.md for detailed instructions.**
