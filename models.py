class DrugReactionPredictor:
    def __init__(self):
        self.model = None

    def predict(self, X):
        return [0 for _ in range(len(X))]
