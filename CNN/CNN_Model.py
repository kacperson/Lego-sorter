from tensorflow import keras


data_generator = keras.preprocessing.image.ImageDataGenerator()
train = data_generator.flow_from_directory(directory='Data/train', class_mode='categorical', batch_size=32)
validation = data_generator.flow_from_directory(directory='Data/validation', class_mode='categorical', batch_size=32)
test = data_generator.flow_from_directory(directory='Data/test', class_mode='categorical', batch_size=32)

model = keras.Sequential()
model.add(keras.Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(keras.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(keras.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.Conv2D(256, kernel_size=(3, 3), activation='relu'))
model.add(keras.MaxPooling2D(pool_size=(2, 2)))
model.add(keras.Flatten())
model.add(keras.Dense(512, activation='relu'))
model.add(keras.Dense(256, activation='relu'))
model.add(keras.Dense(200, activation='softmax'))
model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])

history = model.fit(train, steps_per_epoch=16, validation_data=validation, validation_steps=8)

loss = model.evaluate_generator(test, steps=24)
