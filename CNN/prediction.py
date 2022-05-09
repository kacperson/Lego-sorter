import numpy as np
from tensorflow import keras




def make_pred(image="brick.png"):
    labels = {0: '2357', 1: '2412', 2: '2420', 3: '2429', 4: '2430', 5: '2431', 6: '2432', 7: '2436', 8: '2445', 9: '2450'}
    image = keras.preprocessing.image.load_img(image, target_size=(64, 64))
    image_arr = keras.preprocessing.image.img_to_array(image)
    image_batch = np.expand_dims(image_arr, axis=0)
    image_preproc = keras.applications.resnet50.preprocess_input(image_batch)
    model = keras.models.load_model("D:\\Lego-sorter\\CNN\\CNN_Model_final_Adam.h5")
    model.summary()
    prediction = model.predict(image_preproc)
    classes = np.argmax(prediction, axis=1)
    print(prediction)
    return labels[classes[0]]

