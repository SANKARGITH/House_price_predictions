from flask import Flask,request, jsonify
import utils
app: Flask = Flask(__name__)

utils.load_utils()
@app.route('/locations',methods=['GET'])
def get_location():
    response = jsonify(
        {'locations': utils.get_locations()}
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_predict_price',methods=['POST'])
def get_predict_price():
    total_sqft = int(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    response = jsonify(
        {
            "predicted_price" : utils.get_predicted_price(location,total_sqft,bath,bhk)
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Server started")
    app.run()