# Full Stack Facts Application

## Description
This project is a simple full-stack web application developed as part of an exercise to understand backend API development, frontend integration, and cloud deployment.  
The backend provides a REST API that returns a list of hardcoded facts in JSON format.

---

## How I Developed This Application

1. I started by creating a backend REST API using Django and Django REST Framework.
2. I set up a Django project and a dedicated app for handling facts.
3. Using Django REST Framework, I created an API endpoint (`GET /api/facts`) that returns a hardcoded list of facts in JSON format.
4. I structured the backend code in a clean and modular way to follow best practices.
5. I tested the API locally using a browser and Postman to ensure correct responses.
6. The project was organized into separate backend and frontend folders to follow a full-stack project structure.
7. The source code was pushed to a public GitHub repository with proper documentation.

---

## What I Learnt in This Exercise

- How to create REST APIs using Django REST Framework.
- How to structure a backend project properly for scalability.
- Understanding of API endpoints, HTTP methods, and JSON responses.
- Importance of virtual environments and dependency management.
- How to troubleshoot common environment and module errors.
- How to organize a full-stack project repository on GitHub.
- Writing clear and professional README documentation for projects.

---

## Tech Stack
- Python
- Django
- Django REST Framework

---

## API Endpoint

### Get Facts


### Sample Response
```json
[
  { "id": 1, "fact": "The sun is a star." },
  { "id": 2, "fact": "Water boils at 100°C." },
  { "id": 3, "fact": "Earth has one moon." }
]
