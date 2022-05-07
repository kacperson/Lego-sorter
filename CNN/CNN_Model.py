from tensorflow import keras
import sklearn


data_generator = keras.preprocessing.image.ImageDataGenerator()
train = data_generator.flow_from_directory(directory='Data/train', class_mode='categorical', batch_size=10)
validation = data_generator.flow_from_directory(directory='Data/validation', class_mode='categorical', batch_size=10)
test = data_generator.flow_from_directory(directory='Data/test', class_mode='categorical', batch_size=10)

model = keras.Sequential()
model.add(keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.Conv2D(256, kernel_size=(3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.layers.GlobalAveragePooling2D())
model.add(keras.layers.Flatten())

model.summary()
model.add(keras.layers.Dense(10, activation='softmax'))
model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=['accuracy'])

history = model.fit(train, validation_data=validation, validation_steps=8, epochs=160, batch_size=3)

loss = model.evaluate(test, steps=128)
filename = "D:\\Lego-sorter\\CNN\\CNN_Model_final_Adam.h5"
model.save(filename)
