import os
from modules.model import IrisModel, IrisData

def test_training_saving_model():
    """
    Test that the model trains correctly and saves to disk.
    """
    model = IrisModel()
    X_train, X_test, y_train, y_test = model.load_data()
    model.train(X_train, y_train)
    assert model.model is not None
    assert os.path.exists(model.file_path)

def test_loading_and_prediction():
    """
    Test that a saved model loads correctly and makes predictions.
    """
    model = IrisModel()
    model.load_model()
    
    sample = IrisData(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2)
    prediction = model.predict(sample)
    assert prediction is not None
    assert prediction[0] in [0, 1, 2]