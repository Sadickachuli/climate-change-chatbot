import streamlit as st
import torch
from transformers import BertTokenizer, BertModel
import json
import random
import pickle
from tensorflow.keras.models import load_model


# Loading Pre-trained Models and Assets


# Load the pre-trained BERT tokenizer and model (for embeddings)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')

# Load the saved Keras chatbot model
model = load_model('./data/model/chatbotmodel.h5')

# Load the intents dictionary (assumed to be stored as 'climate_change.json')
with open("./data/json/climate_change.json", "r") as f:
    intents_dict = json.load(f)

# Load the list of classes (tags) from pickle
with open('./data/model/classes.pkl', 'rb') as f:
    classes = pickle.load(f)


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
    
    Args:
        sentence (str): User input sentence.
        
    Returns:
        list: A list of dictionaries with predicted intent(s) and confidence scores.
              Returns an empty list if no prediction meets the threshold.
    """
    embedding = get_bert_embedding(sentence)
    res = model.predict(embedding)[0]
    ERROR_THRESHOLD = 0.35
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    
    # Debug: Output predicted intent and confidence to the Streamlit app for debugging purposes
    if results:
        st.write(f"Predicted Intent: {classes[results[0][0]]}, Confidence: {results[0][1]}")
        return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    else:
        st.write("Low confidence prediction. No suitable intent found.")
        return []

def get_response(intents_list, intents_json):
    """
    Retrieve a response based on the predicted intent.
    
    Args:
        intents_list (list): List of predicted intents with probabilities.
        intents_json (dict): The intents dictionary.
    
    Returns:
        str: A response chosen at random from the matching intent.
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
    # Get predictions from the model
    predicted_intents = predict_class(user_input)
    # Retrieve the chatbot's response based on predicted intent
    response = get_response(predicted_intents, intents_dict)
    # Display the bot's response
    st.write("Bot:", response)
