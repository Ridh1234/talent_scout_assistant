# AI Hiring Assistant Chatbot

## **Project Overview**
This AI-powered chatbot assists in the initial screening of candidates for technical positions by collecting user information and generating relevant interview questions based on their tech stack. The chatbot is built using **Streamlit** for the UI and integrates **Google Gemini API** for AI-based question generation.

---
## **Features**
✅ Interactive chatbot UI using Streamlit  
✅ Collects essential candidate details (Name, Email, Experience, Tech Stack, etc.)  
✅ Generates 3-5 technical interview questions dynamically  
✅ Uses **Google Gemini API** for AI-based response generation  
✅ Fallback mechanism for unexpected inputs  
✅ Easy deployment (local/cloud)  

---
## **Project Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/ai-hiring-chatbot.git
cd ai-hiring-chatbot
```

### **2. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Google Gemini API Key**
1. Obtain a **Gemini API Key** from [Google AI](https://ai.google.com/)
2. Create a `.env` file and store your API key:
   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```
3. Alternatively, set the environment variable manually:
   ```bash
   export GEMINI_API_KEY=your_api_key_here  # macOS/Linux
   set GEMINI_API_KEY=your_api_key_here     # Windows
   ```

---
## **How to Run the Chatbot**
### **1. Run the Streamlit App**
```bash
streamlit run chatbot.py
```
This will launch the chatbot interface in your browser.

---
## **File Structure**
```
/ai-hiring-chatbot/
│── chatbot.py       # Main script to run the chatbot UI
│── backend.py       # Handles AI interactions and question generation
│── config.py        # Stores API keys and configurations
│── requirements.txt # List of dependencies
│── .env             # Stores API keys securely
│── README.md        # Project documentation
└── .gitignore       # Ignore unnecessary files (optional)
```

---
## **Code Explanation**
### **1. Chatbot UI (chatbot.py)**
- Uses Streamlit to create an interactive interface.
- Collects user details such as **name, email, experience, tech stack**.
- Sends input data to `backend.py` for AI-generated questions.

### **2. Backend Logic (backend.py)**
- Uses **Google Gemini API** to generate technical interview questions based on the candidate’s tech stack.
- Implements fallback mechanisms for invalid inputs.

Example function to generate questions:
```python
import os
import google.generativeai as genai

def generate_questions(tech_stack):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    prompt = f"Generate 3-5 technical interview questions for {tech_stack}."
    response = genai.generate_text(prompt)
    return response
```

### **3. API Key Configuration (config.py)**
- Loads the **Google Gemini API Key** from the environment.
- Ensures security by avoiding hardcoded credentials.

### **4. Dependencies (requirements.txt)**
```
streamlit
google-generativeai
dotenv
```

---
## **Deployment (Optional)**
### **Deploy on Streamlit Cloud**
1. Push the repository to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and deploy the app.

### **Deploy on Hugging Face Spaces**
1. Create a **new Space** on [Hugging Face](https://huggingface.co/spaces).
2. Select **Streamlit** as the framework.
3. Upload your code and add `requirements.txt`.

---
## **Final Deliverables**
✅ **Source Code**: Available on GitHub  
✅ **Documentation**: Clear README with setup guide  
✅ **Demo**: Live link (if deployed) or a recorded walkthrough  

🚀 **Congratulations! Your AI Hiring Assistant Chatbot is ready!**

