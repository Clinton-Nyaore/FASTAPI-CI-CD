## FASTAPI for Iris Flower Classification with CI/CD pipeline

This project is for testing CI/CD integration using GitHub Actions

- Author: Clinton Nyaore
- Email: cnyaore@gmail.com

## Project Overview
This project implements a FastAPI application for classifying iris flowers. It uses a machine learning model to predict the species of iris based on sepal and petal measurements.

## Setup
To set up the project:
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `uvicorn main:app --reload`

The application will be available at `http://localhost:8000`.

## CI/CD Pipeline
The CI/CD pipeline is implemented using GitHub Actions and includes:
- Automated testing
- Docker image build
- Deployment to Google Cloud Run

The pipeline configuration can be found in `.github/workflows/cloudrun.yml`.
