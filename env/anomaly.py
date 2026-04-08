import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest()
        data = np.random.rand(100, 3)
        self.model.fit(data)

    def detect(self, cpu, memory, errors):
        x = np.array([[cpu/100, memory/100, errors/100]])
        return int(self.model.predict(x)[0] == -1)