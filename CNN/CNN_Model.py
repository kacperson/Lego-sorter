from tensorflow import keras
import pickle


data_generator = keras.preprocessing.image.ImageDataGenerator()
train = data_generator.flow_from_directory(directory='Data/train', class_mode='categorical', batch_size=16)
validation = data_generator.flow_from_directory(directory='Data/validation', class_mode='categorical', batch_size=16)
test = data_generator.flow_from_directory(directory='Data/test', class_mode='categorical', batch_size=16)

model = keras.Sequential()
model.add(keras.layers.Conv2D(16, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.GlobalAveragePooling2D())
model.summary()
model.add(keras.layers.Dense(16, activation='softmax'))
model.compile(optimizer="SGD", loss="categorical_crossentropy", metrics=['accuracy'])

history = model.fit(train, validation_data=validation, validation_steps=8, epochs=10)

loss = model.generator(test, steps=128)

filename = "CNN_Model_final.sav"
pickle.dump(model, open(filename, 'rb'))
