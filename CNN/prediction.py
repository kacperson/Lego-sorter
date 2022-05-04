import numpy as np
from tensorflow import keras




def make_pred(image):

    image = keras.preprocessing.image.load_img(image, target_size=(64, 64))
    image_arr = keras.preprocessing.image.img_to_array(image)
    image_batch = np.expand_dims(image_arr, axis=0)
    image_preproc = keras.applications.resnet50.preprocess_input(image_batch)
    model = keras.models.load_model("D:\\Lego-sorter\\CNN\\CNN_Model_final.h5")

    prediction = model.predict(image_preproc)
    classes = np.argmax(prediction, axis=1)
    print(classes)

make_pred("D:\\Lego-sorter\\CNN\\brick.png")
