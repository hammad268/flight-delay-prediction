# ✈️ Flight Delay Prediction

<p align="center">
  <b>Machine Learning Classification Project</b>
  <br>
  Predict whether a flight will experience an arrival delay using flight operational data.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Scikit--Learn-1.6.1-orange?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Machine-Learning-green" />
</p>

---

## 📌 Overview

Flight delays are a common problem in the aviation industry. They can be influenced by factors such as departure time, airline, flight route, departure delay, and flight distance.

This project uses **Machine Learning classification algorithms** to predict whether a flight will experience an arrival delay.

The project covers the complete Machine Learning workflow:

**Data Cleaning → Preprocessing → Encoding → Scaling → Model Comparison → Hyperparameter Tuning → Evaluation → Deployment**

An interactive **Streamlit web application** is also included for making predictions.

---

## 🎯 Objective

The objective of this project is to predict the arrival delay status of a flight.

### Target Variable

| Value | Meaning |
|------:|---------|
| `0` | Flight is not delayed |
| `1` | Flight is delayed |

The target column used in the dataset is:

```text
ARR_DEL15

📊 Dataset

The project uses flight data from January 2020.

The original dataset contains approximately 410,000 records. Due to computational requirements, a sample of 100,000 records was used for model development.

Features
Numerical Features
Feature	Description
DAY_OF_MONTH	Day of the month
DAY_OF_WEEK	Day of the week
OP_CARRIER_FL_NUM	Operating carrier flight number
DEP_TIME	Departure time
DEP_DEL15	Departure delay indicator
DISTANCE	Flight distance
Categorical Features
Feature	Description
OP_UNIQUE_CARRIER	Unique operating airline
ORIGIN	Origin airport
DEST	Destination airport
DEP_TIME_BLK	Departure time block
