import joblib
from pathlib import Path
from fastapi import HTTPException
from app.core.config import settings
from sklearn import __version__ as sklearn_version

def load_model():
    """Load ML model and scaler with version check"""
    try:
        # Load model info
        model_info = joblib.load(settings.MODEL_PATH)
        
        # Check scikit-learn version
        if model_info['sklearn_version'] != sklearn_version:
            print(f"Warning: Model trained with scikit-learn {model_info['sklearn_version']}, "
                  f"but running with {sklearn_version}")
        
        return model_info['model'], model_info['scaler']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mapping dictionary
iris_mapping = {
    0: 'Iris-setosa',
    1: 'Iris-versicolor', 
    2: 'Iris-virginica'
}