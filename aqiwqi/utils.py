def calculate_wqi(tds, temperature, ph):
    """
    Calculate Water Quality Index (WQI) based on TDS, temperature, and pH values.

    :param tds: Total Dissolved Solids (TDS) value in ppm.
    :param temperature: Temperature value in degrees Celsius.
    :param ph: pH value.

    :return: Water Quality Index (WQI) value.
    """
    # Normalize and weight each parameter (you can adjust ranges and weights)
    normalized_tds = normalize_tds(tds)
    normalized_temp = normalize_temperature(temperature)
    normalized_ph = normalize_ph(ph)

    # Define weights for each parameter (you can adjust weights based on importance)
    weight_tds = 40
    weight_temp =30
    weight_ph =30

    # Calculate WQI using weighted sum approach
    wqi = (normalized_tds * weight_tds) + (normalized_temp * weight_temp) + (normalized_ph * weight_ph)

    return wqi

def normalize_tds(tds_value):
    """
    Normalize Total Dissolved Solids (TDS) value.

    :param tds_value: Total Dissolved Solids (TDS) value in ppm.

    :return: Normalized TDS value in the range [0, 1].
    """
    max_desirable_tds = 500.0  # Example: maximum desirable TDS in ppm
    return min(1.0, tds_value / max_desirable_tds)  # Normalize to range [0, 1]

def normalize_temperature(temp_value):
    """
    Normalize temperature value.

    :param temp_value: Temperature value in degrees Celsius.

    :return: Normalized temperature value in the range [0, 1].
    """
    max_temperature = 100.0  # Example: maximum temperature in °C
    return min(1.0, temp_value / max_temperature)  # Normalize to range [0, 1]

def normalize_ph(ph_value):
    """
    Normalize pH value.

    :param ph_value: pH value.

    :return: Normalized pH value in the range [0, 1].
    """
    min_desirable_ph = 6.5  # Example: minimum desirable pH
    max_desirable_ph = 8.5  # Example: maximum desirable pH

    if ph_value < min_desirable_ph:
        return 0.0
    elif ph_value > max_desirable_ph:
        return 1.0
    else:
        return (ph_value - min_desirable_ph) / (max_desirable_ph - min_desirable_ph)  # Normalize to range [0, 1]





###########################################################################################################################################

def calculate_aqi_pm_2_5(pm_2_5):
    # AQI calculation for PM 2.5 based on EPA breakpoints
    if 0 <= pm_2_5 <= 12:
        return linear_conversion(pm_2_5, 0, 12, 0, 50)
    elif 12.1 <= pm_2_5 <= 35.4:
        return linear_conversion(pm_2_5, 12.1, 35.4, 51, 100)
    elif 35.5 <= pm_2_5 <= 55.4:
        return linear_conversion(pm_2_5, 35.5, 55.4, 101, 150)
    elif 55.5 <= pm_2_5 <= 150.4:
        return linear_conversion(pm_2_5, 55.5, 150.4, 151, 200)
    elif 150.5 <= pm_2_5 <= 250.4:
        return linear_conversion(pm_2_5, 150.5, 250.4, 201, 300)
    elif 250.5 <= pm_2_5 <= 350.4:
        return linear_conversion(pm_2_5, 250.5, 350.4, 301, 400)
    elif 350.5 <= pm_2_5 <= 500.4:
        return linear_conversion(pm_2_5, 350.5, 500.4, 401, 500)
    else:
        return None  # Out of range

def calculate_aqi_pm_10(pm_10_0):
    # AQI calculation for PM 10 based on EPA breakpoints
    if 0 <= pm_10_0 <= 54:
        return linear_conversion(pm_10_0, 0, 54, 0, 50)
    elif 55 <= pm_10_0 <= 154:
        return linear_conversion(pm_10_0, 55, 154, 51, 100)
    elif 155 <= pm_10_0 <= 254:
        return linear_conversion(pm_10_0, 155, 254, 101, 150)
    elif 255 <= pm_10_0 <= 354:
        return linear_conversion(pm_10_0, 255, 354, 151, 200)
    elif 355 <= pm_10_0 <= 424:
        return linear_conversion(pm_10_0, 355, 424, 201, 300)
    elif 425 <= pm_10_0 <= 504:
        return linear_conversion(pm_10_0, 425, 504, 301, 400)
    elif 505 <= pm_10_0 <= 604:
        return linear_conversion(pm_10_0, 505, 604, 401, 500)
    else:
        return None  # Out of range

def calculate_aqi_mq7(mq7_data):
    # AQI calculation for mq7_data (Carbon Monoxide) based on EPA breakpoints
    if 0 <= mq7_data <= 4.4:
        return linear_conversion(mq7_data, 0, 4.4, 0, 50)
    elif 4.5 <= mq7_data <= 9.4:
        return linear_conversion(mq7_data, 4.5, 9.4, 51, 100)
    elif 9.5 <= mq7_data <= 12.4:
        return linear_conversion(mq7_data, 9.5, 12.4, 101, 150)
    elif 12.5 <= mq7_data <= 15.4:
        return linear_conversion(mq7_data, 12.5, 15.4, 151, 200)
    elif 15.5 <= mq7_data <= 30.4:
        return linear_conversion(mq7_data, 15.5, 30.4, 201, 300)
    elif 30.5 <= mq7_data <= 40.4:
        return linear_conversion(mq7_data, 30.5, 40.4, 301, 400)
    elif 40.5 <= mq7_data <= 50.4:
        return linear_conversion(mq7_data, 40.5, 50.4, 401, 500)
    else:
        return None  # Out of range

def linear_conversion(c, i_low, i_high, b_low, b_high):
    # Linear conversion function for AQI calculation
    return ((b_high - b_low) / (i_high - i_low)) * (c - i_low) + b_low

def calculate_aqi(pm_2_5, pm_10_0, mq7_data):
    # Calculate individual AQIs
    aqi_pm_2_5 = calculate_aqi_pm_2_5(pm_2_5)
    aqi_pm_10 = calculate_aqi_pm_10(pm_10_0)
    aqi_co = calculate_aqi_mq7(mq7_data)
    
    # The overall AQI is the highest of the individual AQIs
    aqi = max(aqi_pm_2_5, aqi_pm_10, aqi_co)
    print(aqi)
    return aqi


##################################################################################################################################

import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('aqiwqi/models/AQI_model.h5')

def predict_aqi(pm_2_5, pm_10_0, mq7_data):
    # Prepare input data for prediction
    input_data = np.array([[pm_2_5, pm_10_0, mq7_data]])
    # Reshape input_data to match the input shape expected by the LSTM model
    new_x_reshaped = np.reshape(input_data, (1, 1, input_data.shape[1]))

    # Make predictions using the model
    predictions = model.predict(new_x_reshaped)

    # Extract and return the predicted AQI value (as a single scalar)
    predicted_aqi = predictions[0][0]
    return predicted_aqi



##############################################################################################################################################




import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model1= load_model('aqiwqi/models/WQI_model.h5')

def predict_wqi(ph_data,temp,tds):
    # Define new input data for prediction
    new_x = np.array([[ph_data,temp,tds]])  # New input data point (shape: (1, number_of_features))

    # Reshape new_x to match the input shape expected by the LSTM model
    new_x_reshaped = np.reshape(new_x, (1, 1, new_x.shape[1]))  # Reshape to (1, 1, number_of_features)

    # Make predictions using the model
    predictions = model1.predict(new_x_reshaped)

    # Print the predicted AQI value
    predicted_wqi = predictions[0][0]
    return predicted_wqi
 


