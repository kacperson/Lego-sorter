from tensorflow import keras



data_generator = keras.preprocessing.image.ImageDataGenerator()
train = data_generator.flow_from_directory(directory='Data/train', class_mode='categorical', batch_size=32)
validation = data_generator.flow_from_directory(directory='Data/validation', class_mode='categorical', batch_size=32)
test = data_generator.flow_from_directory(directory='Data/test', class_mode='categorical', batch_size=32)

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(400, activation='relu'))
model.add(keras.layers.Dense(200))
model.summary()
model.compile(optimizer=keras.optimizers.SGD(learning_rate=1e-3), loss=keras.losses.SparseCategoricalCrossentropy(
    from_logits=True), metrics=keras.metrics.Accuracy())
#batchX, batchy = train.next()
#print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))

history = model.fit(train, steps_per_epoch=16, validation_data=validation, validation_steps=8)

loss = model.evaluate_generator(test, steps=24)
