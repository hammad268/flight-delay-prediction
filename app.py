import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Flight Delay Predictor",
    page_icon="✈️",
    layout="wide"
)


@st.cache_resource
def load_files():
    model = joblib.load("flight_delay_model.pkl")
    scaler = joblib.load("flight_delay_scaler.pkl")
    features = joblib.load("flight_delay_features.pkl")
    preprocessing = joblib.load("flight_delay_preprocessing.pkl")

    return model, scaler, features, preprocessing


model, scaler, feature_columns, preprocessing = load_files()

numerical_features = preprocessing["numerical_features"]
categorical_features = preprocessing["categorical_features"]


st.title("✈️ Flight Delay Predictor")
st.write("Enter the flight information to predict whether the flight will be delayed.")


st.divider()


col1, col2, col3 = st.columns(3)


with col1:
    day_of_month = st.number_input(
        "Day of Month",
        min_value=1,
        max_value=31,
        value=15
    )

    day_of_week = st.number_input(
        "Day of Week",
        min_value=1,
        max_value=7,
        value=3
    )

    flight_number = st.number_input(
        "Flight Number",
        min_value=1,
        max_value=9999,
        value=100
    )


with col2:
    dep_time = st.number_input(
        "Departure Time",
        min_value=0,
        max_value=2359,
        value=1200
    )

    dep_del15 = st.selectbox(
        "Departure Delay",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    distance = st.number_input(
        "Distance",
        min_value=1,
        max_value=5000,
        value=500
    )


with col3:
    carrier = st.text_input(
        "Airline Code",
        value="AA"
    )

    origin = st.text_input(
        "Origin Airport",
        value="ATL"
    )

    destination = st.text_input(
        "Destination Airport",
        value="LAX"
    )

    dep_time_blk = st.text_input(
        "Departure Time Block",
        value="1200-1259"
    )


st.divider()


if st.button("🔮 Predict Flight Delay", use_container_width=True):

    input_data = pd.DataFrame({
        "DAY_OF_MONTH": [day_of_month],
        "DAY_OF_WEEK": [day_of_week],
        "OP_CARRIER_FL_NUM": [flight_number],
        "DEP_TIME": [dep_time],
        "DEP_DEL15": [dep_del15],
        "DISTANCE": [distance],
        "OP_UNIQUE_CARRIER": [carrier],
        "ORIGIN": [origin],
        "DEST": [destination],
        "DEP_TIME_BLK": [dep_time_blk]
    })


    for column in categorical_features:
        input_data[column] = input_data[column].astype(str)


    input_data = pd.get_dummies(
        input_data,
        columns=categorical_features,
        drop_first=True
    )


    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )


    input_data = input_data.astype(int)


    input_scaled = scaler.transform(input_data)


    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]


    st.divider()

    if prediction == 1:

        st.error("⚠️ Flight is predicted to be DELAYED")

    else:

        st.success("✅ Flight is predicted to NOT be delayed")


    st.metric(
        "Delay Probability",
        f"{probability * 100:.2f}%"
    )