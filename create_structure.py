import os

# Define the full structure
structure = {
    "image-comparison-api": {
        "app": {
            "config": ["__init__.py", "settings.py"],
            "core": ["__init__.py", "dependencies.py", "exceptions.py"],
            "services": ["__init__.py", "image_service.py", "storage_service.py"],
            "models": ["__init__.py", "schemas.py"],
            "api": {
                "routes": ["__init__.py", "image_comparison.py"],
                "dependencies.py": None,
                "__init__.py": None,
            },
            "static": {
                "uploads": {},
                "original": {},
                "generated": {},
            },
            "templates": ["index.html"],
            "__init__.py": None,
            "main.py": None,
        },
        "tests": ["__init__.py", "test_image_service.py", "test_api.py"],
        "docker": ["Dockerfile", "docker-compose.yml"],
        "deployment": {
            "aws": {
                "cloudformation": ["infrastructure.yaml"],
                "terraform": ["main.tf", "variables.tf", "outputs.tf"],
                "scripts": ["deploy.sh", "build.sh"],
            },
            "k8s": ["deployment.yaml", "service.yaml", "ingress.yaml"],
        },
        ".github": {
            "workflows": ["ci.yml", "cd.yml"]
        },
        "requirements.txt": None,
        "requirements-dev.txt": None,
        ".env.example": None,
        ".gitignore": None,
        "README.md": None,
        "Makefile": None,
        "pyproject.toml": None,
    }
}


def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                open(os.path.join(path, file), "w", encoding="utf-8").close()
        elif content is None:
            open(path, "w", encoding="utf-8").close()


if __name__ == "__main__":
    create_structure(".", structure)
    print("Directory and file structure created successfully.")
