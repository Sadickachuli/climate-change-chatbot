# climate-change-chatbot

![cbot (2)](https://github.com/user-attachments/assets/d9dec30b-2752-4c60-9cf9-3d5ed2c0a6e5)

#  Climate Change Chatbot  

An AI-powered chatbot that provides reliable and informative responses to climate change-related queries. Built using a fine-tuned Transformer model, this chatbot leverages NLP techniques to deliver accurate answers, helping users understand climate science, effects, solutions, and policies.  

##  Features  
- **Natural Language Understanding** – Uses a fine-tuned Transformer model to generate responses.  
- **Pre-trained NLP Model** – Built using Hugging Face’s Transformer models and TensorFlow.  
- **Interactive Chat Interface** – Streamlit-based frontend for seamless user interaction.  
- **React.js Web App (Coming Soon)** – A modern, visually appealing UI for the chatbot.  
- **API Integration** – Uses FastAPI for backend processing.  

---

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
🔹 Deploy React frontend using vercel.
🔹 Deloy React backend with Render
🔹 Expand the dataset for better chatbot accuracy.
🔹 Improve model performance with hyperparameter tuning.

📜 License
This project is licensed under the MIT License.

AUTHOR
[Sadick
](https://github.com/Sadickachuli/)



