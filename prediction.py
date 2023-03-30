import joblib

def predict(data):
    model = joblib.load("reg_model.joblib")
    return model.predict(data)