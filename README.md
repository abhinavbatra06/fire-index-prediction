# Fire Weather Index (FWI) Prediction  

## Project Overview  
This project predicts the **Fire Weather Index (FWI)**, a key indicator of wildfire risk, using meteorological data. The dataset consists of weather observations recorded from **June to September 2012** for 2 regions ,namely the Bejaia region located in the northeast of Algeria and the Sidi Bel-abbes region located in the northwest of Algeria.. Three **linear regression models** (Linear, Ridge, and Lasso) were applied, with **hyperparameter tuning** to improve performance.

---

## Live Web App
[You can access the live app here](https://fire-index-prediction-ano7hn3hjbmsdcsfrmemkk.streamlit.app/)

## Screenshot 

![image](https://github.com/user-attachments/assets/8b2b8c7e-b48d-4eb3-8703-2ba74c5de071)


## [Dataset](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset)

The dataset includes the following features:  
### Weather Data Observations:
- **Temperature (°C):** 22 - 42  
- **Relative Humidity (%):** 21 - 90  
- **Wind Speed (km/h):** 6 - 29  
- **Rainfall (mm):** 0 - 16.8  

### Fire Weather Index (FWI) System Components:
- **Fine Fuel Moisture Code (FFMC):** 28.6 - 92.5  
- **Duff Moisture Code (DMC):** 1.1 - 65.9  
- **Drought Code (DC):** 7 - 220.4  
- **Initial Spread Index (ISI):** 0 - 18.5  
- **Buildup Index (BUI):** 1.1 - 68  
- **Fire Weather Index (FWI) (Target Variable):** 0 - 31.1  


### Requirements & How to Use  
- Install Dependencies: pip install -r requirements.txt
- Clone the repository:
  - git clone https://github.com/abhinavbatra06/fire-index-prediction.git
  - cd fire-weather-index-prediction
- jupyter notebook

## Approach
#### Exploratory Data Analysis (EDA)
- Data Cleaning
  - Removed null values and corrected column names.
  - Standardized categorical labels and converted region info into a binary column (is_sidi_bel_region)
#### Feature Engineering
- Added is_august as a seasonality feature (August had the highest fire occurrences).
- Removed highly correlated features (BUI & DC) to reduce multicollinearity.
#### Model Training 
- Train-Test Split: 80-20 split.
- Regression Models Used:
  - Linear Regression (Baseline)
  - Ridge Regression (Best alpha = 5, L2 regularization)
  - Lasso Regression (Best alpha = 0.01, L1 regularization)

## Eval Metrics
Model             | R² Score	| Mean Squared Error (MSE)

Linear Regression	| 0.81	    | 2.43

Ridge Regression	| 0.81	    | 2.40

Lasso Regression	| 0.81	    | 2.40

### Key Observations 

- Minimal improvement in Ridge & Lasso over Linear Regression.
- Fire risk is highly seasonal, with August showing the highest fire occurrences.
- The highest values of coefficients are for - Initial Spread Index (ISI) & Duff Moisture Code (DMC)

