from tensorflow import keras

data_generator = keras.preprocessing.image.ImageDataGenerator()
train = data_generator.flow_from_directory(directory='Data/train', class_mode='categorical', batch_size=64)
validation = data_generator.flow_from_directory(directory='Data/validation', class_mode='categorical', batch_size=64)
test = data_generator.flow_from_directory(directory='Data/test', class_mode='categorical', batch_size=64)

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
model.summary()
batchX, batchy = train.next()
print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))