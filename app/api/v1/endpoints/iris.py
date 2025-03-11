from fastapi import APIRouter, HTTPException
from app.schemas.iris import IrisInput, IrisResponse
from app.utils.model_utils import load_model, iris_mapping
import pandas as pd

# Initialize router with tags for API documentation
router = APIRouter(tags=["iris"])

# Load model and scaler at startup
try:
    model, scaler = load_model()
    print("✅ Model and scaler loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {str(e)}")
    raise

@router.post("/predict", response_model=IrisResponse)
async def predict_iris(data: IrisInput):
    """
    Predict Iris species from input measurements
    
    Args:
        data (IrisInput): Input features for prediction
        
    Returns:
        IrisResponse: Predicted species and input features
        
    Raises:
        HTTPException: If prediction fails
    """
    try:
        # Prepare input data
        input_data = [[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]]
        
        # Convert to DataFrame
        input_df = pd.DataFrame(
            input_data, 
            columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        )
        
        # Scale and predict
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        species = iris_mapping[prediction[0]]
        
        return {
            'prediction': species,
            'input_features': data
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )