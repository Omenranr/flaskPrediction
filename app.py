from flask import Flask
import pandas as pd 
# from fbprophet import Prophet

app = Flask(__name__) 

@app.route("/") 
def home_view():
	return {"timeline":[1, 2, 3]}


app.run()