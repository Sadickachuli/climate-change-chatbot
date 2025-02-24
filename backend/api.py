from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
import numpy as np
from transformers import DistilBertTokenizer, DistilBertModel
import json
import random
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

# ========================== #
# ✅ Optimize TensorFlow to Prevent Crashes
# ========================== #
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Force TensorFlow to use CPU

# Limit memory growth
physical_devices = tf.config.list_physical_devices('CPU')
if physical_devices:
    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
    except Exception as e:
        print(f"TensorFlow memory limit error: {e}")

# ========================== #
# ✅ FastAPI Initialization & CORS
# ========================== #
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# ========================== #
# ✅ Load Models & Data
# ========================== #

try:
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    bert_model = DistilBertModel.from_pretrained('distilbert-base-uncased')

    # Load chatbot model
    model = load_model('../data/model/chatbotmodel.h5')

    # Load intents
    with open("../data/json/climate_change.json", "r") as f:
        intents_dict = json.load(f)

    # Load classes
    with open('../data/model/classes.pkl', 'rb') as f:
        classes = pickle.load(f)

    print("✅ Models and data loaded successfully.")

except Exception as e:
    print(f"🚨 Error loading models or data: {e}")

# ========================== #
# ✅ Helper Functions
# ========================== #

class UserInput(BaseModel):
    text: str

def get_bert_embedding(sentence: str) -> np.ndarray:
    """Generate a BERT embedding for a given sentence."""
    inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

def predict_class(sentence: str):
    """Predict the intent of an input sentence."""
    embedding = get_bert_embedding(sentence)
    res = model.predict(embedding)[0]
    ERROR_THRESHOLD = 0.30
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results] if results else []

def get_response(intents_list):
    """Retrieve a response based on the predicted intent."""
    if not intents_list:
        return "Sorry, I don't understand."
    
    tag = intents_list[0]['intent']
    for intent in intents_dict['intents']:
        if tag in intent['tags']:
            return random.choice(intent['responses'])
    
    return "Sorry, I don't understand."

# ========================== #
# ✅ FastAPI Routes
# ========================== #

@app.post("/chat")
def chat_response(user_input: UserInput):
    predicted_intents = predict_class(user_input.text)
    response = get_response(predicted_intents)
    return {"response": response}

# ========================== #
# ✅ Deployment Configuration for Render
# ========================== #

PORT = int(os.environ.get("PORT", 8000))  # Get port from environment

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
