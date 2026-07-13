# Mall Customer Segmentation API

## Overview

Mall Customer Segmentation API is an end-to-end Machine Learning deployment project that predicts the customer segment using the K-Means clustering algorithm.

The application is built with FastAPI, containerized using Docker, deployed on AWS EC2, and managed using Git & GitHub.

---

## Features

- Customer Segmentation using K-Means Clustering
- FastAPI REST API
- Interactive HTML/CSS frontend
- Dockerized deployment
- AWS EC2 deployment
- Git & GitHub integration
- Production-ready project structure

---

## Customer Segments

- High-Value Loyalists
- Budget Seekers
- Window Shoppers
- Churn Risks
- Tech Innovators
- Passive Consumers
- Brand Advocates
- Urban Professionals
- Suburban Families
- Digital Nomads
- Seasonal Buyers
- Impulse Shoppers
- Discounts-Only Hunters
- Recent Onboarders

---

## Dataset

Dataset:
Mall Customer Segmentation Dataset

Features

- Gender
- Age
- Annual Income
- Spending Score

---

## Technology Stack

### Machine Learning

- Python
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Backend

- FastAPI
- REST API
- Uvicorn

### Frontend

- HTML
- CSS

### DevOps

- Docker
- Git
- GitHub

### Cloud

- AWS EC2

---

## Project Structure

```
Mall-Customer-Segmentation/

│── app.py
│── train_model.py
│── model.pkl
│── requirements.txt
│── Dockerfile
│── .dockerignore
│── .gitignore
│
├── templates/
│      index.html
│
├── static/
│      style.css
│
├── dataset/
│
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repo>.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run locally

```bash
uvicorn app:app --reload
```

Visit

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Docker

Build

```bash
docker build -t mall-customer-segmentation .
```

Run

```bash
docker run -d -p 8000:8000 mall-customer-segmentation
```

---

## AWS Deployment

The application is deployed on an AWS EC2 Ubuntu instance using Docker.

Deployment workflow:

GitHub → Docker → AWS EC2

---

## API Endpoint

### Home

```
GET /
```

### Predict

```
POST /predict
```

---

## Future Improvements

- GitHub Actions CI/CD
- Apache Airflow integration
- MLflow experiment tracking
- Amazon ECR & ECS deployment
- Kubernetes deployment
- Prometheus & Grafana monitoring

---

## Author

Hanoch Shetty

B.Sc. Information Technology Student

Interested in Machine Learning, AI Engineering, Data Science, and MLOps.
