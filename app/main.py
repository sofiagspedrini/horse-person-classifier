from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from app.utils.preprocessing import preprocessing

app = Flask(__name__)

model = load_model("app/model/horse_person_cnn_model.keras")

@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['file']

    try:
        image = preprocessing(file)
        prediction = model.predict(image)[0][0]
        if prediction > 0.5:
                label = "Is a person"
        else:
            label = "Is a horse"
        return jsonify({'Prediction': label})
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)