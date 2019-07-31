from keras.models import Sequential
from keras.layers import dense
from keras.models import model_from_json
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import MinMaxScaler


class PredictOutput:
    def predict(self, array):
        #load in the model from the json file and run it
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        # load weights into new model
        loaded_model.load_weights("model.h5")
        print("Loaded model from disk")

        Xnew = array
        Ynew = loaded_model.predict_classes(Xnew)

        return Ynew
