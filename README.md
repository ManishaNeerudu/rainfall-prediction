# 🌧️ Rainfall Prediction Web Application

## Overview

This project is a Flask-based web application that predicts whether it will rain based on weather parameters using a Machine Learning model.

The application was developed to demonstrate the complete Machine Learning workflow—from data preprocessing and model training to backend integration and deployment.

The trained Random Forest model is integrated with a Flask backend and deployed on AWS EC2, allowing users to make rainfall predictions through a simple web interface.

---

## Features

- Predicts rainfall using weather parameters
- Machine Learning model built using Random Forest
- User-friendly Flask web interface
- Real-time prediction
- AWS EC2 deployment
- Clean and modular project structure

---

## Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy

### Backend

- Flask

### Deployment

- AWS EC2

### Tools

- Git
- GitHub
- VS Code

---

## Project Workflow

Dataset

↓

Data Preprocessing

↓

Feature Engineering

↓

Random Forest Model Training

↓

Model Evaluation

↓

Model Serialization (.pkl)

↓

Flask Backend

↓

Web Interface

↓

Rainfall Prediction

---

## Project Structure

```
RainfallPrediction/
│
├── static/
│
├── templates/
│   └── index.html
│
├── rainfall_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Install the required libraries.

```bash
pip install -r requirements.txt
```

3. Run the application.

```bash
python app.py
```

4. Open the Flask application in your browser.

---

## Future Improvements

- Improve prediction accuracy using additional weather features.
- Deploy using Docker.
- Add user authentication.
- Store prediction history in a database.
- Support live weather API integration.

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Machine Learning model development
- Flask backend development
- Model deployment using AWS EC2
- Git and GitHub version control
- Building end-to-end ML applications

---

## Author

**Manisha Neerudu**

AI & Machine Learning Undergraduate
