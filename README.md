
[![FastAPI](https://img.shields.io/badge/FastAPI-000000?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) [![Containerized: Docker](https://img.shields.io/badge/Container-Docker-blue?logo=docker)](https://www.docker.com/) [![Deployed on Render](https://img.shields.io/badge/Hosted-Render-green)]()  

A FastAPI-based MLOps showcase that predicts energy usage for buildings using building + environment features. Built with scikit-learn, XGBoost, Dockerized for reproducible deployments and currently deployed on Render for production-ready inference. This repo demonstrates a complete regression MLOps flow: preprocessing, validation, model packaging, API endpoints, and containerized deployment.

---

# Project Overview 🚀

This project demonstrates a realistic MLOps pipeline for **energy consumption regression**:

- **Framework:** FastAPI  
- **Modeling:** scikit-learn pipeline, XGBoost model (pre-trained `Model/energy_consumption.pkl`)  
- **Validation:** Pydantic request validation + robust error handling  
- **Deployment:** Docker, deployed on Render.com (serverless container)  
- **Docs:** Interactive OpenAPI docs (served by FastAPI)

Features included: feature engineering, preprocessing (categoricals, scaling, imputing), pipeline serialization (joblib/pickle), containerized deployment, and API docs for easy integration.

---

# Directory Structure 📁

```
ENERGY_CONSUMPTION/
├── main.py
├── requirements.txt
├── Dockerfile
├── Model/
│   └── energy_consumption.pkl
├── README.md
├── .gitignore
└── ...
```

---

# Installation & Quickstart 🛠️


```bash
python -m venv env
source env/bin/activate         # macOS / Linux
# env\Scripts\activate          # Windows PowerShell

pip install --upgrade pip
pip install -r requirements.txt

# run the app
python main.py

```

---

# API Endpoints 🧭

All endpoints are defined in `main.py` — use the OpenAPI docs to interactively test payloads.

### `GET /`
Basic API health response (quick check)

**Response**
```json
{ "status": "ok", "message": "Energy Consumption Model API" }
```

### `GET /health`
API, model, and version status check (returns model loaded state & app version)

**Response (example)**
```json
{
  "status": "ok",
  "Version": true,
  "mode": "25.0.9.2025"
}
```

### `POST /predict`
Predict energy consumption given building + environment features.

**Example request JSON**
```json
{
  "building_type": "Residential",
  "Square_Footage": 14000,
  "Number_of_Occupants": 3,
  "use": 2,
  "Temperature": 34.5,
  "dayofweek": "Weekday"
}
```

**Example `curl`**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
        "building_type":"Residential",
        "Square_Footage":14000,
        "Number_of_Occupants":3,
        "use":2,
        "Temperature":34.5,
        "dayofweek":"Weekday"
      }'
```

**Response (example)**
```json
{
  "power_consumption": 12345.67,
}
```

---

# Live Documentation 🧾

Interactive OpenAPI docs (Swagger UI) are available at:

```
https://energy-consume-model.onrender.com/docs
```

(Replace the URL above with your deployment URL if deploying elsewhere.)

---

# Deployment (Render.com) ☁️

This project is packaged in a Docker image and deployed on Render.com. Basic Dockerfile highlights:

- Base: `python:3.10-slim`
- Installs dependencies from `requirements.txt`
- Copies app code and serialized model (`Model/energy_consumption.pkl`)
- Exposes port `8000` and runs `uvicorn main:app --host 0.0.0.0 --port 8000`

If you want to deploy to Render:
1. Connect your GitHub repo to Render.
2. Configure service to deploy the Dockerfile.
3. Set health check route (e.g., `/health`) and environment variables as needed.

---

# Main Tech Stack 🧩

- FastAPI — REST API + automatic docs  
- scikit-learn & XGBoost — modeling & pipelines  
- Pydantic — input validation & schemas  
- Docker — containerized packaging  
- Render.com — cloud hosting / production runtime

---

# MLOps Skills Demonstrated 🧪

- Feature engineering & preprocessing (categorical encoding, scaling, imputation)  
- Robust input validation and helpful error messages  
- Model pickling / pipeline management (joblib `.pkl`)  
- Reproducible Docker builds and container deployments  
- API documentation and testability via OpenAPI/Swagger  
- Cloud-native hosting & scaling with Render

---



# Author & Contact ✉️

- GitHub: `[https://github.com/CodewithAvijit]` — replace with your GitHub username  

# License

This project is released under the **MIT License** — feel free to adapt and reuse. Add a `LICENSE` file to the repo.
