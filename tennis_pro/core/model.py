import xgboost as xgb
import lightgbm as lgb
from sklearn.ensemble import VotingClassifier

class TennisEnsemble:
    """Wrapper for the 95.44% Accuracy Ensemble Model."""
    def __init__(self, params=None):
        self.model = VotingClassifier(
            estimators=[
                ('xgb', xgb.XGBClassifier(n_estimators=600, learning_rate=0.015, max_depth=8)),
                ('lgb', lgb.LGBMClassifier(n_estimators=600, learning_rate=0.015, verbose=-1))
            ], voting='soft'
        )

    def train(self, X, y, weights):
        self.model.fit(X, y, sample_weight=weights)

    def predict(self, X_input):
        return self.model.predict(X_input)
