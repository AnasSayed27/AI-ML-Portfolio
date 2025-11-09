from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import uvicorn
from typing import Tuple # Import for type hinting

# -------------------------------
# 1. App Setup
# -------------------------------
app = FastAPI(title="Potato Disease Classifier", version="1.0")

# -------------------------------
# 2. Model & Class Configuration
# -------------------------------
MODEL_PATH = "Potato_Disease_Classifier_Model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# The correct class order you identified
CLASS_NAMES = ["Early_Blight", "Late_Blight", "Healthy"]

# -------------------------------
# 3. Template Configuration
# -------------------------------
templates = Jinja2Templates(directory="templates")

# -------------------------------
# 4. Prediction Helper Function
# -------------------------------
def predict_image(image_bytes: bytes) -> Tuple[str, float]:
    """
    Takes image bytes, preprocesses the image, and returns
    the predicted label and its confidence.
    """
    try:
        # Open and prepare the image
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((256, 256)) # Must match training size
        
        # Convert to numpy array and add batch dimension
        # IMPORTANT: No / 255.0, as the model's first layer handles rescaling
        img_array = np.expand_dims(np.array(img), axis=0) 

        # Make prediction
        predictions = model.predict(img_array)
        
        # Get top prediction
        pred_idx = np.argmax(predictions[0])
        confidence = float(np.max(predictions[0]))
        label = CLASS_NAMES[pred_idx]
        
        return label, confidence
        
    except Exception as e:
        print(f"Error in predict_image: {e}")
        return "Error", 0.0

# -------------------------------
# 5. API Routes
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """Serves the main HTML page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(file: UploadFile = File(...)) -> JSONResponse:
    """
    Receives an image file, predicts its class, and 
    returns a JSON response with the label and confidence.
    """
    image_bytes = await file.read()
    label, confidence = predict_image(image_bytes)
    
    return JSONResponse(content={
        "label": label,
        "confidence": float(confidence * 100) # Send as percentage
    })

# -------------------------------
# 6. Run the App
# -------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)