def fake_predict(user_age):
    if user_age > 10:
        Prediction = 'survive (Over10)'
    else:
        Prediction = 'super survive (Under10)'
    return Prediction
