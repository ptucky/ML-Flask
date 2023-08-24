from flask import Flask, jsonify, request
from utilities import predict_pipeline

app = Flask(__name__)

@app.post('/predict')
def predict():
    data = request.json
    try:
      receiveData = data['text']
    except KeyError:
      return jsonify({'error', 'Empty text'})
    
    # Dictionaries [receiveData]
    receive_data = [receiveData]
    predictions = predict_pipeline(receive_data)

    try: 
      result = jsonify(predictions[0])
    except TypeError as e:
      result = jsonify({'error', str(e)})
    return result

if __name__ == '__main__':
   # debug=True
   app.run(host='127.0.0.1', debug=True)
    