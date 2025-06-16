# Image Comparison FastAPI Project

## Project Structure
```
image-comparison-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   └── exceptions.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── image_service.py
│   │   └── storage_service.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── image_comparison.py
│   │   └── dependencies.py
│   ├── static/
│   │   ├── uploads/
│   │   ├── original/
│   │   └── generated/
│   └── templates/
│       └── index.html
├── tests/
│   ├── __init__.py
│   ├── test_image_service.py
│   └── test_api.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── deployment/
│   ├── aws/
│   │   ├── cloudformation/
│   │   │   └── infrastructure.yaml
│   │   ├── terraform/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   └── outputs.tf
│   │   └── scripts/
│   │       ├── deploy.sh
│   │       └── build.sh
│   └── k8s/
│       ├── deployment.yaml
│       ├── service.yaml
│       └── ingress.yaml
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── .gitignore
├── README.md
├── Makefile
└── pyproject.toml
```

## Step-by-Step Development Guide

### Step 1: Initial Setup

1. **Create project directory**
```bash
mkdir image-comparison-api
cd image-comparison-api
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Create basic project structure**
```bash
mkdir -p app/{config,core,services,models,api/routes,static/{uploads,original,generated},templates}
mkdir -p tests docker deployment/{aws/{cloudformation,terraform,scripts},k8s} .github/workflows
```

### Step 2: Dependencies and Configuration

4. **Create requirements.txt**
5. **Create .env.example**
6. **Create app/config/settings.py**
7. **Create app/__init__.py**

### Step 3: Core Components

8. **Create app/core/exceptions.py**
9. **Create app/core/dependencies.py**
10. **Create app/models/schemas.py**

### Step 4: Services Layer

11. **Create app/services/storage_service.py**
12. **Create app/services/image_service.py**

### Step 5: API Layer

13. **Create app/api/routes/image_comparison.py**
14. **Create app/main.py**

### Step 6: Frontend

15. **Create app/templates/index.html**

### Step 7: Testing

16. **Create tests/test_image_service.py**
17. **Create tests/test_api.py**

### Step 8: Containerization

18. **Create docker/Dockerfile**
19. **Create docker/docker-compose.yml**

### Step 9: CI/CD

20. **Create .github/workflows/ci.yml**
21. **Create .github/workflows/cd.yml**

### Step 10: AWS Deployment

22. **Create deployment/aws/terraform/main.tf**
23. **Create deployment/aws/scripts/deploy.sh**
24. **Create deployment/k8s/ files**

### Step 11: Final Configuration

25. **Create Makefile**
26. **Create pyproject.toml**
27. **Create README.md**

## Design Patterns Used

1. **Repository Pattern** - Storage service abstraction
2. **Service Layer Pattern** - Business logic separation
3. **Dependency Injection** - FastAPI dependencies
4. **Factory Pattern** - Configuration management
5. **Strategy Pattern** - Different storage backends
6. **Observer Pattern** - Event handling (optional)
7. **Singleton Pattern** - Configuration settings

## Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   API Layer     │    │   Service Layer │
│   (HTML/JS)     │◄──►│   (FastAPI)     │◄──►│   (Business)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                ▲                       ▲
                                │                       │
                                ▼                       ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   Models/       │    │   Storage       │
                       │   Schemas       │    │   (S3/Local)    │
                       └─────────────────┘    └─────────────────┘
```

## AWS Deployment Architecture

```
Internet Gateway
        │
    ALB (Load Balancer)
        │
┌───────┴────────┐
│   ECS Cluster  │
│ ┌─────────────┐│
│ │ FastAPI App ││◄─── ECR (Container Registry)
│ └─────────────┘│
└────────────────┘
        │
┌───────┴────────┐
│   S3 Bucket    │
│ (File Storage) │
└────────────────┘
```

Next, I'll provide the actual code for each file. Would you like me to start with the first few files?