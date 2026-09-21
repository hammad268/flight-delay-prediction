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
```

---

## 📊 Dataset

The project uses flight data from **January 2020**.

The original dataset contains approximately **410,000 records**. Due to computational requirements, a sample of **100,000 records** was used for model development.

### Features

#### Numerical Features

| Feature             | Description                     |
| -------------------- | -------------------------------- |
| `DAY_OF_MONTH`      | Day of the month                |
| `DAY_OF_WEEK`       | Day of the week                 |
| `OP_CARRIER_FL_NUM` | Operating carrier flight number |
| `DEP_TIME`          | Departure time                  |
| `DEP_DEL15`         | Departure delay indicator       |
| `DISTANCE`          | Flight distance                 |

#### Categorical Features

| Feature             | Description              |
| -------------------- | -------------------------- |
| `OP_UNIQUE_CARRIER` | Unique operating airline |
| `ORIGIN`            | Origin airport           |
| `DEST`              | Destination airport      |
| `DEP_TIME_BLK`      | Departure time block     |

---

## 🔄 Machine Learning Pipeline

```text
                    Flight Dataset
                          │
                          ▼
                  Data Cleaning
                          │
                          ▼
                Select 100,000 Rows
                          │
                          ▼
                 Train/Test Split
                    80% / 20%
                          │
                          ▼
                Missing Value Handling
                          │
                          ▼
              Categorical Encoding
                          │
                          ▼
                 Feature Alignment
                          │
                          ▼
                  Feature Scaling
                          │
                          ▼
                 Model Comparison
                          │
                          ▼
              Hyperparameter Tuning
                          │
                          ▼
             Gradient Boosting Model
                          │
                          ▼
                 Model Evaluation
                          │
                          ▼
                 Save Model Files
                          │
                          ▼
              Streamlit Web Application
```

---

## 🧹 Data Preprocessing

### 1. Train/Test Split

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

Stratified splitting was used to maintain the distribution of the target classes.

### 2. Missing Values

Missing numerical values were handled using the **median** calculated from the training data.

Missing categorical values were handled using the **mode** calculated from the training data.

### 3. Categorical Encoding

Categorical features were converted into numerical features using:

```python
pd.get_dummies()
```

with:

```python
drop_first=True
```

Training and testing features were then aligned to ensure both datasets contained the same columns.

### 4. Feature Scaling

`StandardScaler` was used to standardize the feature values.

The scaler was fitted on the training data and then applied to the test data.

---

## 🤖 Models Compared

Multiple classification algorithms were tested during the model comparison stage.

| Model                  | Mean F1 Score |
| ------------------------ | --------------: |
| Gradient Boosting      |    **0.7393** |
| XGBoost                |        0.7358 |
| Hist Gradient Boosting |        0.7345 |
| Random Forest          |        0.7067 |
| Extra Trees            |        0.6924 |
| Logistic Regression    |        0.6815 |
| SGD Classifier         |        0.6271 |
| Decision Tree          |        0.5994 |
| Naive Bayes            |        0.2436 |
| KNN                    |        0.0943 |

> **Note:** These comparison results were obtained using a 20,000-row training subset with 3-fold cross-validation.

---

## 🏆 Final Model

After comparing multiple algorithms, **Gradient Boosting Classifier** was selected for the final model.

### Best Parameters

```text
n_estimators = 50
learning_rate = 0.1
max_depth = 3
random_state = 42
```

Hyperparameter tuning was performed using `GridSearchCV`.

### Best Cross-Validation F1 Score

```text
0.75056
```

---

## ⚙️ Hyperparameter Tuning

The Gradient Boosting model was tuned using `GridSearchCV`.

The following parameters were explored:

```text
n_estimators
learning_rate
max_depth
```

The tuning configuration used:

```text
Cross Validation : 3-Fold
Scoring          : F1 Score
```

---

## 💾 Saved Model Files

The trained model and preprocessing components were saved using `Joblib`.

| File                              | Purpose                         |
| ----------------------------------- | ---------------------------------- |
| `flight_delay_model.pkl`         | Trained Gradient Boosting model |
| `flight_delay_scaler.pkl`        | Fitted StandardScaler           |
| `flight_delay_features.pkl`      | Final feature column list       |
| `flight_delay_preprocessing.pkl` | Preprocessing information       |

These files allow the Streamlit application to load the trained model without retraining it.

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application where users can enter flight information.

### Input Features

- Day of Month
- Day of Week
- Flight Number
- Departure Time
- Departure Delay
- Flight Distance
- Airline
- Origin Airport
- Destination Airport
- Departure Time Block

The application processes the input using the same preprocessing pipeline used during model training.

It then displays:

```text
Prediction
+
Prediction Probability
```

---

## 📸 Application Preview

> Add your Streamlit application screenshot here.

```text
[ Streamlit Application Screenshot ]
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/hammad268/flight-delay-prediction.git
```

Navigate to the project directory:

```bash
cd flight-delay-prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📁 Project Structure

```text
flight-delay-prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── flight_delay_model.pkl
├── flight_delay_scaler.pkl
├── flight_delay_features.pkl
└── flight_delay_preprocessing.pkl
```

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Joblib**
- **Streamlit**
- **GridSearchCV**
- **Gradient Boosting**
- **Machine Learning**

---

## ⚠️ Important Limitation

The feature `DEP_DEL15` represents departure delay information.

Therefore, this model should not be considered a purely **pre-departure prediction system**, because departure-delay information may only be available after the departure process has begun.

---

## 🔮 Future Improvements

Possible improvements include:

- Using the complete dataset for training
- Feature engineering from date and time information
- Testing additional boosting algorithms
- Improving categorical feature handling
- Optimizing model inference
- Deploying the Streamlit application online
- Adding interactive visualizations
- Adding model monitoring

---

## 👨‍💻 Author

### Hammad Kamran

**BS Artificial Intelligence Student**

GitHub: [@hammad268](https://github.com/hammad268)

---

## 📄 License

This project is licensed under the **MIT License**.
