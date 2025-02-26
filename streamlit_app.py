import streamlit as st
import torch
from transformers import BertTokenizer, BertModel
import json
import random
import pickle
from tensorflow.keras.models import load_model

# Loading Pre-trained Models and Assets

# Load the pre-trained BERT tokenizer and model (this is for embeddings)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')

# Load the saved Keras chatbot model
model = load_model('./data/model/chatbotmodel.h5')

# Load the intents dictionary 
with open("./data/json/climate_change.json", "r") as f:
    intents_dict = json.load(f)

# Load the list of classes (tags)
with open('./data/model/classes.pkl', 'rb') as f:
    classes = pickle.load(f)

# Hardcoded greeting responses
greeting_responses = [
    "Hello! 👋 I'm your Climate Change Chatbot. Ask me anything about climate change, and I'll be happy to help!",
    "Hey there! 🌍 I'm here to answer your questions about climate change. Just type your question, and I'll do my best!",
    "Hi! 👋 Need info on climate change? Just ask, and I'll provide insights!",
]

# Common greetings to check for
greeting_keywords = {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"}

# Defining Helper Functions

def get_bert_embedding(sentence):
    """
    Generate a BERT embedding for a given sentence.
    """
    inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    # Compute the mean of the last hidden state as the sentence embedding
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

def predict_class(sentence):
    """
    Predict the intent of an input sentence using the trained chatbot model.
    """
    embedding = get_bert_embedding(sentence)
    res = model.predict(embedding)[0]
    ERROR_THRESHOLD = 0.33
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)

    if results:
        st.write(f"Predicted Intent: {classes[results[0][0]]}, Confidence: {results[0][1]}")
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    else:
        st.write("Low confidence prediction. No suitable intent found.")
        return []

def get_response(intents_list, intents_json):
    """
    Retrieve a response based on the predicted intent.
    """
    if not intents_list:
        return "Sorry, I don't understand."
    
    tag = intents_list[0]['intent']
    for intent in intents_json['intents']:
        if tag in intent['tags']:
            return random.choice(intent['responses'])
    return "Sorry, I don't understand."

# Building the Streamlit Interface

st.title("Climate Change Chatbot")
st.markdown("Ask a question about climate change and get an intelligent response!")

# Text input for user query
user_input = st.text_input("You:")

if user_input:
    user_text = user_input.lower().strip()

    # Check if user input is a greeting
    if any(word in user_text for word in greeting_keywords):
        response = random.choice(greeting_responses)
    else:
        # Get predictions from the model
        predicted_intents = predict_class(user_text)
        # Get the chatbot's response based on predicted intent
        response = get_response(predicted_intents, intents_dict)

    # Display the bot's response
    st.write("Bot:", response)
