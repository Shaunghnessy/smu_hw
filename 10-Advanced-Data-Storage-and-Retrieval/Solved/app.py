from flask import Flask, jsonify
import pandas as pd
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper()

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
        return(
        f"""Welcome to the Hawaii Weather API!<br>
        <a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a>""")

@app.route("/api/v1.0/precipitation")
def prcp():
    recent_prcp = session.query(str(Measurement.date), Measurement.prcp)\
    .filter(Measurement.date > '2016-08-22')\
    .filter(Measurement.date <= '2017-08-23')\
    .order_by(Measurement.date).all()

    # convert results to a dictionary with date as key and prcp as value
    prcp_dict = dict(recent_prcp)

    # return json list of dictionary
    return jsonify(prcp_dict)


# create station route of a list of the stations in the dataset
@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.name, Station.station).all()

    # convert results to a dictionary
    stations_dict = dict(stations)

    # return json list of dictionary 
    return jsonify(stations_dict)


# create tobs route of temp observations for most active station over last 12 months
@app.route("/api/v1.0/tobs")
def tobs():
    tobs_station = session.query(str(Measurement.date), Measurement.tobs)\
    .filter(Measurement.date > '2016-08-23')\
    .filter(Measurement.date <= '2017-08-23')\
    .filter(Measurement.station == "USC00519281")\
    .order_by(Measurement.date).all()

    # convert results to dictionary
    tobs_dict = dict(tobs_station)

    # return json list of dictionary
    return jsonify(tobs_dict)


# create start and start/end route
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_date(start, end=None):

    q = session.query(str(func.min(Measurement.tobs)), str(func.max(Measurement.tobs)), str(func.round(func.avg(Measurement.tobs))))
    if start:
        q = q.filter(Measurement.date >= start)
    if end:
        q = q.filter(Measurement.date <= end)

    # convert results into a dictionary 

    results = q.all()[0]
    keys = ["Min Temp", "Max Temp", "Avg Temp"]
    temp_dict = {keys[i]: results[i] for i in range(len(keys))}
    return jsonify(temp_dict)


if __name__ == "__main__":
    app.run(debug=True)