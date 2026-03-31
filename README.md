# Student Performance Prediction using Machine Learning

## 📌 Overview

This project applies Machine Learning techniques to predict whether a student will pass or fail based on academic and behavioral attributes such as study hours, attendance, and past scores.

The objective is to demonstrate fundamental Artificial Intelligence and Machine Learning concepts including data preprocessing, model training, evaluation, and prediction.

---

## 🎯 Problem Statement

Educational institutions often struggle to identify students who are at risk of failing early enough to provide support.

This project builds a machine learning model that predicts student performance so that educators can intervene earlier and improve academic outcomes.

---

## 🧠 Machine Learning Concepts Used

* Supervised Learning
* Classification
* Data Preprocessing
* Feature Engineering
* Model Evaluation
* Model Persistence

Algorithms used:

* Logistic Regression
* Random Forest Classifier

---

## 🗂 Dataset Features

| Feature               | Description                     |
| --------------------- | ------------------------------- |
| study_hours           | Hours studied per day           |
| attendance            | Percentage attendance           |
| previous_score        | Score in previous exam          |
| assignments_completed | Number of assignments submitted |
| result                | Pass / Fail                     |

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/student-performance-ml.git
cd student-performance-ml
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Train the model:

```bash
python src/train_model.py
```

Make predictions:

```bash
python src/predict.py
```

---

## 📊 Model Performance

Accuracy achieved:

```
Random Forest Accuracy: ~90%
Logistic Regression Accuracy: ~85%
```

Random Forest was selected as the final model due to better performance.

---

## 💡 Applications

* Early student risk detection
* Personalized academic support
* Educational analytics systems
* Academic performance monitoring

---

## 🚀 Future Improvements

* Use deep learning models
* Add more student behavioral features
* Deploy as a web application
* Integrate with school management systems

---

## 👨‍💻 Author

Course Project – Artificial Intelligence & Machine Learning
