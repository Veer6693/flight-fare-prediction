from flask import Flask, render_template, request
from sklearn.model_selection import GridSearchCV
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('flight_fare_xgb.pkl','rb'))

data = pd.read_excel("Data_Train.xlsx")

@app.route('/')
def home():
    unique_sources = data['Source'].unique().tolist()
    unique_destinations = data['Destination'].unique().tolist()
    unique_airlines = data['Airline'].unique().tolist()

    return render_template('index.html', sources=unique_sources, destinations=unique_destinations, airlines=unique_airlines)



@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        Total_Stops = int(request.form['stop'])
        Dep_date = request.form['departure_date']
        Arrival_date = request.form['arrival_date']
        airline = request.form['airline']
        source = request.form['source']
        destination = request.form['destination']

        Journey_Day = int(pd.to_datetime(Dep_date).day)
        Journey_Month = int(pd.to_datetime(Dep_date).month)
        Dep_Hour = int(pd.to_datetime(Dep_date).hour)
        Dep_Minute = int(pd.to_datetime(Dep_date).minute)
        Journey_DOW = int(pd.to_datetime(Dep_date).dayofweek)

        Arrival_Hour = int(pd.to_datetime(Arrival_date).hour)
        Arrival_Minute = int(pd.to_datetime(Arrival_date).minute)

        Duration_Hour = abs(Arrival_Hour - Dep_Hour)
        Duration_Minute = abs(Arrival_Minute - Dep_Minute)
        Total_Duration = (Duration_Hour * 60) + Duration_Minute

        Airline_Air_India = 1 if airline == "Air India" else 0
        Airline_GoAir = 1 if airline == "GoAir" else 0
        Airline_IndiGo = 1 if airline == "IndiGo" else 0
        Airline_Jet_Airways = 1 if airline == "Jet Airways" else 0
        Airline_Jet_Airways_Business = 1 if airline == "Jet Airways Business" else 0
        Airline_Multiple_carriers = 1 if airline == "Multiple carriers" else 0
        Airline_Multiple_carriers_Premium_economy = 1 if airline == "Multiple carriers Premium economy" else 0
        Airline_SpiceJet = 1 if airline == "SpiceJet" else 0
        Airline_Trujet = 1 if airline == "Trujet" else 0
        Airline_Vistara = 1 if airline == "Vistara" else 0
        Airline_Vistara_Premium_economy = 1 if airline == "Vistara Premium economy" else 0
        

        Source_Chennai = 1 if source == "Chennai" else 0
        Source_Delhi = 1 if source == "Delhi" else 0
        Source_Kolkata = 1 if source == "Kolkata" else 0
        Source_Mumbai = 1 if source == "Mumbai" else 0



        Destination_Cochin = 1 if destination == "Cochin" else 0
        Destination_Delhi = 1 if destination == "Delhi" else 0
        Destination_Hyderabad = 1 if destination == "Hyderabad" else 0
        Destination_Kolkata = 1 if destination == "Kolkata" else 0
        Destination_New_Delhi = 1 if destination == "New Delhi" else 0



        predict = model.predict([[Total_Stops,
                                     
                                Journey_Day,Journey_Month,Journey_DOW,
                                     
                                Dep_Hour,Dep_Minute,

                                Arrival_Hour,Arrival_Minute,
                                     
                                Duration_Hour,Duration_Minute,Total_Duration,
                                     
                                Airline_Air_India, Airline_GoAir, Airline_IndiGo, Airline_Jet_Airways, 
                                Airline_Jet_Airways_Business, Airline_Multiple_carriers, 
                                Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, 
                                Airline_Trujet, Airline_Vistara, Airline_Vistara_Premium_economy,

                                Source_Chennai, Source_Delhi, Source_Kolkata, Source_Mumbai,

                                Destination_Cochin, Destination_Delhi, Destination_Hyderabad, 
                                Destination_Kolkata, Destination_New_Delhi
                                   ]])

        prediction = int(predict)

   
        return render_template('index.html', prediction_output = f"Estimated price From {source} to {destination} is Rs. {prediction}")


    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)




