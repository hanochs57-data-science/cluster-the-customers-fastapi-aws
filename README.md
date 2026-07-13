#  Mall Customer Segmentation API

A production-ready Machine Learning application that segments mall customers into meaningful groups using the **K-Means Clustering** algorithm. The project provides a REST API built with **FastAPI**, containerized with **Docker**, version-controlled using **Git/GitHub**, and designed for cloud deployment on **AWS**.

---

##  Project Overview

Understanding customer behavior is essential for personalized marketing and improved customer engagement. This project leverages **unsupervised machine learning** to group customers with similar purchasing patterns.

Given customer information such as:

- Age
- Gender
- Annual Income (k$)
- Spending Score (1-100)

the model predicts the most appropriate customer segment, enabling businesses to tailor marketing strategies effectively.

---

##  Features

- K-Means Clustering for customer segmentation
- REST API using FastAPI
- Interactive Swagger UI
- Dockerized application
- Git & GitHub version control
- Cloud deployment ready
- Label Encoding
- Feature Scaling
- Model persistence using Joblib
- Clean HTML/CSS frontend
- Modular project architecture

---

##  Customer Segments

The model classifies customers into one of the following categories:

| Cluster | Segment |
|----------|-----------------------------|
| 1 | High-Value Loyalists |
| 2 | Budget Seekers |
| 3 | Window Shoppers |
| 4 | Churn Risks |
| 5 | Tech Innovators |
| 6 | Passive Consumers |
| 7 | Brand Advocates |
| 8 | Urban Professionals |
| 9 | Suburban Families |
|10 | Digital Nomads |
|11 | Seasonal Buyers |
|12 | Impulse Shoppers |
|13 | Discounts-Only Hunters |
|14 | Recent Onboarders |

---

##  Dataset

**Dataset:** Mall Customer Segmentation Dataset

Source:
https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

Features used:

- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

---

##  Machine Learning Workflow

```
Data Collection
       │
       ▼
Data Cleaning
       │
       ▼
Label Encoding
       │
       ▼
Feature Scaling
       │
       ▼
K-Means Clustering
       │
       ▼
Model Training
       │
       ▼
Model Serialization (Joblib)
       │
       ▼
FastAPI REST API
       │
       ▼
Docker Container
       │
       ▼
Cloud Deployment
```

---

##  Tech Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

### Backend

- FastAPI
- Uvicorn
- REST API

### Frontend

- HTML
- CSS

### DevOps

- Docker
- Git
- GitHub

### Cloud

- AWS (Deployment Ready)

---

##  Project Structure

```
Mall-Customer-Segmentation/

│
├── app.py
├── train_model.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
│
├── model/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── static/
│
├── templates/
│   └── index.html
│
├── dataset/
│
├── notebooks/
│
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Mall-Customer-Segmentation.git
```

Move into the project

```bash
cd Mall-Customer-Segmentation
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app:app --reload
```


---

##  Docker

Build Docker Image

```bash
docker build -t mall-customer-api .
```

Run Container

```bash
docker run -p 8000:8000 mall-customer-api
```

---

##  REST API

### Home

```
GET /
```

Loads the prediction interface.

### Predict

```
POST /predict
```

Returns the predicted customer segment.

---

##  Application Preview

Add screenshots here:

- Home Page
- Prediction Result
- Swagger UI

---

##  Future Enhancements

- GitHub Actions CI/CD pipeline
- Apache Airflow for automated retraining
- AWS ECS deployment
- Model monitoring with MLflow
- Prometheus & Grafana integration
- Prediction confidence and cluster visualization
- Real-time analytics dashboard

---

##  Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

##  License

This project is licensed under the MIT License.

---

##  Author

Developed as an end-to-end Machine Learning Deployment project demonstrating:

- Machine Learning
- FastAPI
- REST APIs
- Docker
- Git & GitHub
- Cloud Deployment
- Production-ready project architecture