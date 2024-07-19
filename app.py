from flask import Flask, render_template, request
from suntracer import SuntracerForm, suntracerPredictions, suntracerPredictionsJSON
from sewy import SewyForm, sewyPredictions, sewyPredictionsJSON
from knx import TouchForm, touchPredictions, touchPredictionsJSON
import json
import numpy as np
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suntracer/json', methods=['POST'])
def predict_temperature_suntracer_json():
    prediction = suntracerPredictionsJSON(request.json)
    
    return prediction

@app.route('/suntracer/', methods=['GET','POST'])
def predict_temperature_suntracer():
    prediction, graphs, labels, form = suntracerPredictions()
    if prediction:
        return render_template('predict_form.html', device="Suntracer", form=form, prediction=prediction, img_data=graphs, labels=labels)
    return render_template('predict_form.html', device="Suntracer", form=form)

@app.route('/sewy/json', methods=['POST'])
def predict_temperature_sewy_json():
    prediction = sewyPredictionsJSON(request.json)
    
    return prediction

@app.route('/sewy/', methods=['GET','POST'])
def predict_temperature_sewy():
    prediction, graphs, labels, form = sewyPredictions()
    if prediction:
        return render_template('predict_form.html', device="Sewy", form=form, prediction=prediction, img_data=graphs, labels=labels)
    return render_template('predict_form.html', device="Sewy", form=form)

@app.route('/knx/json', methods=['POST'])
def predict_temperature_knx_json():
    prediction = touchPredictionsJSON(request.json)
    
    return prediction

@app.route('/knx/', methods=['GET','POST'])
def predict_temperature_knx():
    prediction, graphs, labels, form = touchPredictions()
    if prediction:
        return render_template('predict_form.html', device="KNX Touch", form=form, prediction=prediction, img_data=graphs, labels=labels)
    return render_template('predict_form.html', device="KNX Touch", form=form)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))