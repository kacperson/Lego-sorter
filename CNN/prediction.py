import pickle
from tensorflow import keras


def make_pred(image):
    image = keras.preprocessing.image.load_img(image)
    loaded_model = pickle.load(open("CNN_Model_final.sav", 'rb'))
    prediction = loaded_model.predict_classes(image)
    print(prediction)
    return prediction

make_pred("brick.png")
