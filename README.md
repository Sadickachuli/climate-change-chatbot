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

| Questions                         | Answers                                                                                  | Patterns                                   | Tags               |
|------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------|--------------------|
| What is climate change?           | Climate change refers to long-term alterations in temperature, precipitation, and other atmospheric conditions on Earth. | Can you define climate change?            | Climate Science   |
| What are greenhouse gases?        | Greenhouse gases are gases that trap heat in the atmosphere, including carbon dioxide, methane, and water vapor.        | Can you explain what greenhouse gases are? | Greenhouse Gases  |
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

🛠️ Future Improvements
- Deploy React frontend using vercel.
  
- Deloy React backend with Render
  
- Expand the dataset for better chatbot accuracy.
  
- Improve model performance with hyperparameter tuning.

📜 License
This project is licensed under the MIT License.

AUTHOR
[Sadick
](https://github.com/Sadickachuli/)



