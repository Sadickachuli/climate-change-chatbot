from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import BertTokenizer, BertModel
import json
import random
import pickle
from tensorflow.keras.models import load_model
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Force TensorFlow to use CPU

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load pre-trained tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')

# Load chatbot model
model = load_model('../data/model/chatbotmodel.h5')

# Load intents
with open("../data/json/climate_change.json", "r") as f:
    intents_dict = json.load(f)

# Load classes
with open('../data/model/classes.pkl', 'rb') as f:
    classes = pickle.load(f)

class UserInput(BaseModel):
    text: str

# Hardcoded greeting responses
greeting_responses = [
    "Hello! 👋 I'm your Climate Change Chatbot. Ask me anything about climate change, and I'll be happy to help!",
    "Hey there! 🌍 I'm here to answer your questions about climate change. Just type your question, and I'll do my best!",
    "Hi! 👋 Need info on climate change? Just ask, and I'll provide insights!",
]

# Common greetings to check for
greeting_keywords = {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"}

def get_bert_embedding(sentence):
    """Generate a BERT embedding for a given sentence."""
    inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

def predict_class(sentence):
    """Predict intent of an input sentence."""
    embedding = get_bert_embedding(sentence)
    res = model.predict(embedding)[0]
    ERROR_THRESHOLD = 0.35
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

@app.post("/chat")
def chat_response(user_input: UserInput):
    user_text = user_input.text.lower().strip()

    # Check if user input is a greeting
    if any(word in user_text for word in greeting_keywords):
        return {"response": random.choice(greeting_responses)}

    # Normal chatbot logic
    predicted_intents = predict_class(user_text)
    response = get_response(predicted_intents)
    return {"response": response}
