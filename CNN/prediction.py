import pickle


def make_pred(image):
    image = [image]
    loaded_model = pickle.load(open("CNN_Model_final.sav", 'rb'))
    prediction = loaded_model.predict_classes(image)
    return prediction
