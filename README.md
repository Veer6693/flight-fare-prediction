
# Flight Fare Prediction

This project aims to predict flight fares using a machine learning model. The dataset used contains information such as departure date, arrival date, source, destination, stopage, and airline name.

## Features

- Data preprocessing: Includes changing data types, removing unwanted columns, and applying one-hot encoding.
- Machine learning model: Tried multiple algorithms, with XGBoost being the best performer after hyperparameter tuning.
- Web interface: Created using Flask for deployment, allowing users to input flight details for fare prediction.

## Usage

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Veer6693/flight-fare-prediction.git
   
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   
3. Run the Flask app:

   ```bash
   python app.py
                  
4. Open your browser and navigate to http://localhost:5000 to access the web interface.

## Dataset

The dataset used for this project contains 11 columns:

- Airline
- Date_of_Journey
- Source
- Destination
- Route
- Dep_Time
- Arrival_Time
- Duration
- Total_Stops
- Additional_Info
- Price

It consists of 10683 rows.

## Results

The model was evaluated using multiple metrics, including Mean Absolute Error, Mean Square Error, Root Mean Square Error, and R2 Score.

After hyperparameter tuning, XGBoost achieved the following results:

- R2 Score: 83.29 (initial) -> 84.95 (after tuning)
- Mean Absolute Error: 1133.0690
- Mean Squared Error: 3213613.2413
- Root Mean Squared Error: 1792.6554

These results indicate that the model performs well in predicting flight fares.

## Future Improvements

- Include more features for better prediction accuracy.
- Implement a more robust user interface.
