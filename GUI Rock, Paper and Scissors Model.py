import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

dataset = pd.read_excel("GUI RPS.xlsx")
feature_data = dataset[["User"]]
target_data = dataset[["Computer"]]

scaled_feature_data = StandardScaler().fit_transform(feature_data)
X_train, X_test, y_train, y_test = train_test_split(feature_data, target_data, test_size=0.2, random_state=1)

model = Sequential()
model.add(Dense(1, input_dim=1, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=5, epochs=10, verbose=2, validation_data=(X_test, y_test))

model.save('my_model.h5')
