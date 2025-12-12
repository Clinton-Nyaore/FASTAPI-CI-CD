from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import numpy as np
from pydantic import BaseModel, Field

class IrisData(BaseModel):
    sepal_length: float = Field(...)
    sepal_width: float = Field(...)
    petal_length: float = Field(...)
    petal_width: float = Field(...)

    model_config = {
        "json_schema_extra": {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }
    }

class IrisModel:
    def __init__(self, n_estimators=100, random_state=42):
        self.model = RandomForestClassifier(
            n_estimators=n_estimators, 
            random_state=random_state)
        self.file_path = "models/iris_rf_model.joblib"

    def load_data(self):
        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy

    def save_model(self):
        joblib.dump(self.model, self.file_path)

    def load_model(self):
        self.model = joblib.load(self.file_path)
    
    def predict(self, data):
        arr = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        return self.model.predict(arr).tolist()

if __name__ == "__main__":
    iris_model = IrisModel()
    # X_train, X_test, y_train, y_test = iris_model.load_data()
    # iris_model.train(X_train, y_train)
    # accuracy = iris_model.evaluate(X_test, y_test)
    # print(f"Model Accuracy: {accuracy * 100:.2f}%")
    # iris_model.save_model()
    iris_model.load_model()
    data = IrisData(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2)
    prediction = iris_model.predict(data)
    print(f"Prediction for input {data}: {prediction}")