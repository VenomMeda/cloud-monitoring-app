# Flask Application Deployment on AWS with Docker and Kubernetes

---

## Overview

This repository contains code for deploying a Flask application on AWS using Docker for containerization and Kubernetes for orchestration, which is our 4th Semester DevOps project. The Flask application monitors system metrics such as CPU and memory utilization and displays them on a web interface.

---

## Setup Instructions

1. **Clone the Repository**

```
  git clone https://github.com/VenomMeda/cloud-monitoring-app
```

2. **Install Dependencies**

```
  pip install -r requirements.txt
```

3. **Local Deployment**

- Run the Flask application locally:
  ```
  python app.py
  ```

4. **Dockerization**

- Build the Docker image:
  ```
  docker build -t <image_name> .
  ```
- Run the Docker container:
  ```
  docker run -p 5000:5000 <image_name>
  ```

5. **Push Image to AWS ECR**

- Create an ECR repository using the provided Python script.
- Push the Docker image to the ECR repository:
  ```
  docker push <ecr_repo_uri>:<tag>
  ```

6. **Deploy on AWS EKS**

- Create an EKS cluster and add a node group.
- Use the provided Python script to deploy the application on the EKS cluster.

---

## File Structure

- **app.py**: Main Flask application code.
- **Dockerfile**: Configuration file for building Docker image.
- **requirements.txt**: List of Python dependencies.
- **create_ecr_repo.py**: Python script to create ECR repository.
- **deploy_on_eks.py**: Python script to deploy application on EKS.
- **README.md**: Documentation file.

---

## Contributors

- Devagya Raghav
- Avish Jain

---
