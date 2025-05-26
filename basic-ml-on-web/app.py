from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    salary = float(request.form['salary'])
    input_features = np.array([[age, salary]])
    prediction = model.predict(input_features)[0]
    return render_template('index.html', prediction_text=f'Prediction: {prediction}')

if __name__ == '__main__':
    app.run(debug=True)