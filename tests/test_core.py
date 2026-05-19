
import unittest
import pandas as pd
import numpy as np
from tennis_pro.core.model import TennisEnsemble
from tennis_pro.core.features import FeatureEngine

class TestTennisPro(unittest.TestCase):
    def setUp(self):
        self.model = TennisEnsemble()
        self.engine = FeatureEngine()

    def test_model_initialization(self):
        self.assertIsNotNone(self.model.model)

    def test_feature_engine_output(self):
        # Create dummy data
        data = pd.DataFrame({'winner_name': ['A'], 'loser_name': ['B'], 'minutes': [90], 'tourney_date': ['20230101']})
        processed = self.engine.apply_all(data)
        self.assertIsInstance(processed, pd.DataFrame)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
