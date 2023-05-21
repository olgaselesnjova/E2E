from flask import Flask
#import joblib
#import numpy

#MODEL_PATH = 'mlmodels/model.pkl'
#SCALER_PATH = 'mlmodels/scaler.pkl'
app = Flask(__name__)
#model = joblib.load(MODEL_PATH)
#scaler = joblib.load(SCALER_PATH)

@app.route('/')
#@app.route('/predict_price', methods = ['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'
    #args = request.args
    #open_plan = args.get('open_plan', default=-1, type=int)
    #rooms = args.get('rooms', default=-1, type=int)
    #area = args.get('area', default=-1, type=float)
    #renovation = args.get('renovation', default=-1, type=int)


if __name__ == '__main__':
    app.run()
