# climate-change-chatbot

link to chatbot: https://climate-cbot.streamlit.app/

![cbot (2)](https://github.com/user-attachments/assets/d9dec30b-2752-4c60-9cf9-3d5ed2c0a6e5)

# 🌍 Climate Change Chatbot  

An AI-powered chatbot that provides reliable and informative responses to climate change-related queries. Built using a fine-tuned Transformer model, this chatbot leverages NLP techniques to deliver accurate answers, helping users understand climate science, effects, solutions, and policies.  

## 🚀 Features  
✅ **Natural Language Understanding** – Uses a fine-tuned Transformer model to generate responses.  
✅ **Pre-trained NLP Model** – Built using Hugging Face’s Transformer models and TensorFlow.  
✅ **Interactive Chat Interface** – Streamlit-based frontend for seamless user interaction.  
✅ **React.js Web App (Coming Soon)** – A modern, visually appealing UI for the chatbot.  
✅ **API Integration** – Uses FastAPI for backend processing.  

---

## 📂 Project Structure  

Climate-Change-Chatbot/ │── backend/ # FastAPI backend for chatbot API │── dataset/ # Dataset for chatbot training │── model/ # Trained Transformer model │── react-frontend/ # React.js user interface (Not Deployed) │── streamlit-app/ # Streamlit UI for testing chatbot │── training/ # Model training scripts (Colab) │── requirements.txt # Python dependencies │── README.md # Project documentation



## ⚙️ Installation Guide  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/climate-change-chatbot.git
cd climate-change-chatbot
💡 Setting Up the Backend
2️⃣ Create a Virtual Environment (Optional but Recommended)
bash

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
3️⃣ Install Backend Dependencies
bash

pip install -r requirements.txt
4️⃣ Run the FastAPI Backend
bash

cd backend
uvicorn main:app --reload
The backend should now be running at http://127.0.0.1:8000 🎉

🎨 Running the Streamlit Frontend
5️⃣ Navigate to the Streamlit App Directory
bash

cd streamlit-app
6️⃣ Install Dependencies
bash

pip install -r requirements.txt
7️⃣ Run the Streamlit App
bash

streamlit run app.py
The chatbot UI will be available at http://localhost:8501

🖥️ Running the React Frontend (Local Setup)
8️⃣ Navigate to the React Frontend Directory
bash

cd react-frontend
9️⃣ Install Node.js Dependencies
Ensure you have Node.js installed. Then, run:

bash

npm install
🔟 Start the React App
bash

npm run dev
The frontend should now be running on http://localhost:5173 🚀

🛠️ Future Improvements
🔹 Deploy React frontend using Vercel/Netlify.
🔹 Expand the dataset for better chatbot accuracy.
🔹 Improve model performance with hyperparameter tuning.

🤝 Contributing
Feel free to fork this repository, make changes, and submit a pull request. Contributions are always welcome!

📜 License
This project is licensed under the MIT License.

📧 Contact
For any questions, reach out at your-email@example.com.




