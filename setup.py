
from setuptools import setup, find_packages

setup(
    name='tennis_pro',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas', 'numpy', 'xgboost', 'lightgbm', 'scikit-learn'
    ],
)
