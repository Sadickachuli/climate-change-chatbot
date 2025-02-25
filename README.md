#  **Climate Change Chatbot** 

![cbot (2)](https://github.com/user-attachments/assets/d9dec30b-2752-4c60-9cf9-3d5ed2c0a6e5)



An AI-powered chatbot that provides reliable and informative responses to climate change-related queries. Built using a fine-tuned Transformer model, this chatbot leverages NLP techniques to deliver accurate answers, helping users understand climate science, effects, solutions, and policies.  

##  **Features**  
- **Natural Language Understanding** – Uses a fine-tuned Transformer model to generate responses.  
- **Pre-trained NLP Model** – Built using Hugging Face’s Transformer models and TensorFlow.  
- **Interactive Chat Interface** – Streamlit-based frontend for seamless user interaction.  
- **React.js Web App (Coming Soon)** – A modern, visually appealing UI for the chatbot.  
- **API Integration** – Uses FastAPI for backend processing.  

---
## **Dataset**
The dataset used for training the climate change chatbot consists of structured question-answer pairs covering various aspects of climate science, causes, effects, mitigation strategies, and policies. It is designed to improve chatbot interactions by mapping user queries to relevant responses using predefined tags.

### **Structure of the Dataset**
The dataset is organized into four main fields:

1. Questions: Commonly asked user queries related to climate change.

2. Answers: Corresponding responses providing accurate and concise information.

3. Patterns: Alternative phrasings of the questions to enhance the chatbot’s ability to recognize diverse user inputs.

4. Tags: Categorization labels that group similar topics, enabling efficient intent recognition.

## **Data Format**
The dataset is stored in JSON format, which allows efficient processing for training a Transformer-based chatbot.

## **Why This Dataset?**
- Covers key climate change topics including causes, effects, solutions, policies, and scientific concepts.

- Provides diverse question variations to enhance chatbot accuracy.

- Enables intent classification for better user interaction.

- Supports easy expansion for improved chatbot performance over time.

This dataset serves as the foundation for training the chatbot, ensuring that it can provide informative and contextually relevant responses to users’ climate-related queries.

## **Sample Entries**

| Questions                         | Answers                                                                                  | Patterns                                   | Tags               |
|------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------|--------------------|
| What is climate change?           | Climate change refers to long-term alterations in temperature, precipitation, and other atmospheric conditions on Earth. | Can you define climate change?            | Climate Science   |
| How does carbon dioxide contribute to global warming?       | Carbon dioxide traps heat in the Earth's atmosphere, leading to increased global temperatures.        | What is the role of CO2 in climate change? | CO2 Impact  |
| What is the Paris Agreement?      | The Paris Agreement is an international treaty aimed at limiting global temperature rise to well below 2°C.             | Can you explain the Paris Agreement?      | Climate Policy    |


## 📂 Project Structure  

Climate-Change-Chatbot/ 
│── backend/ # FastAPI backend for chatbot API 

│── data/ # Dataset for chatbot training including the saved model 

│── my-chatbot/ # React.js user interface (Not Deployed) 

│── notebook/ # final colab notebook with model training scripts

│── streamlit-app/ # Deployed Streamlit UI for testing chatbot 

│── requirements.txt # Python dependencies 

│── README.md # Project documentation



## ⚙️ Installation Guide  

### **1️. Clone the Repository**  
```bash
git clone https://github.com/your-username/climate-change-chatbot.git
cd climate-change-chatbot

```
### **2️. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3️. **Install Backend Dependencies**
```bash
pip install -r requirements.txt
```
### 4️. **Run the FastAPI Backend**
```bash
cd backend
uvicorn api:app --reload
```
The backend should now be running at http://127.0.0.1:8000 🎉

### 5. **Running the React Frontend (Local Setup)**
 Navigate to the React Frontend Directory in another terminal
```bash
cd my-chatbot
```
### **6. Install Node.js Dependencies**
Ensure you have Node.js installed. Then, run:

```bash
npm install
```
### **7. Start the React App**
```bash
npm run dev
```
The frontend should now be running on http://localhost:5173 🚀

## Running the Streamlit
The deployed streamlit chatbot is located at: https://climate-cbot.streamlit.app/

### **Hyperparameter Tuning**

| Experiment   | Learning Rate | Batch Size | Epochs | Accuracy | Precision | Recall | F1 Score |
|-------------|--------------|------------|--------|----------|-----------|--------|----------|
| Experiment 1 | 1e-4         | 4          | 10     | 0.75     | 0.78      | 0.65   | 0.71     |
| Experiment 2 | 2e-4         | 8          | 15     | 0.82     | 0.85      | 0.76   | 0.80     |
| Experiment 3 | 5e-5         | 2          | 20      | 0.68     | 0.70      | 0.58   | 0.63     |
| Experiment 4 | 1e-4         | 8          | 25      | 0.79     | 0.82      | 0.72   | 0.77     |
| Experiment 5 | 5e-5         | 4          | 35      | 0.73     | 0.76      | 0.61   | 0.68     |
| Experiment 7 | 1e-4         | 12         | 50     | 0.87     | 0.99      | 0.81   | 0.89     |


### **Performance Metrics**  
The chatbot was trained using a pre-trained Transformer model fine-tuned on the domain-specific dataset above. Below are the key performance metrics from the training process:

| Epoch | Precision | Recall  | Accuracy | Loss  |
|-------|-----------|---------|----------|-------|
| 46    | 0.9779    | 0.7311  | 0.8973   | 0.5218 |
| 47    | 0.9895    | 0.6833  | 0.9012   | 0.5806 |
| 48    | 0.9876    | 0.8085  | 0.9489   | 0.3789 |
| 49    | 0.9872    | 0.7248  | 0.9204   | 0.4366 |
| 50    | 0.9052    | 0.6851  | 0.8744   | 0.5319 |

### **Observations**
- The model achieved its **highest accuracy (94.89%)** at **epoch 48**, with a **precision of 98.76%** and **recall of 80.85%**.
- Loss generally decreased over the epochs, reaching a low of **0.3789** at epoch 48.
- Some fluctuations in recall suggest potential improvements through hyperparameter tuning or dataset augmentation.


 ###  🛠️**Future Improvements**
- Deploy React frontend using vercel.
  
- Deloy React backend with Heroku.
  
- Expand the dataset for better chatbot accuracy.
  
- Improve model performance with hyperparameter tuning.

📜 License
This project is licensed under the MIT License.

AUTHOR
[Sadick
](https://github.com/Sadickachuli/)



