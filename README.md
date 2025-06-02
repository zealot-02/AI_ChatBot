# AI Chatbot with LangChain and Gradio

This is a 2nd-year B.Tech 3rd Semester project featuring a smart AI chatbot powered by LangChain and Ollama (LLaMA3). It includes both a web UI and backend, enables timestamped conversations, and allows saving chats to a file.

## 🔥 Features

- Conversational memory (last interactions)
- Custom UI with Gradio blocks
- Save chat history to conversation_history.txt file
- Timestamped messaging (WhatsApp-style in some versions)
- LLaMA3 (via `langchain_ollama`)

## 📁 Project Structure

```
├── .gradio/                     # Gradio Packages and libraries
├── .idea/                       # Idea files such as .iml
├── .venv/                       # Virtual environment
├── Screenshots/                 # Screenshots of the GUI and backend
├── GUI.py                       # Gradio UI with save and timestamp
├── main.py                      # CLI-based chatbot
├── conversation_history.txt     # Sample saved chat
├── requirements.txt             # Dependencies
└── README.md                    # Project description
```

## 🖼️ Screenshots

### 💬 Chatbot Backend
![Chatbot UI](Screenshot%202025-06-02%20131726.png)

### 📱 GUI Test (Postman)
![chat Test](Screenshot%202025-06-02%20131607.png)
![GUI Test](Screenshot%202025-06-02%20131654.png)


## 🚀 Run the App

To run the Gradio app:
```bash
python GUI.py
```

To run only backend:
```bash
python main.py
```

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## 🧠 Model Used

- `llama3` via Ollama
- LangChain for prompt chaining

## 👨‍🎓 Author

**SUJITHKAMAL KATTA** – 2nd Year B.Tech, Vasireddy Venkatadri Institute of Technology, Numburu, Andhra pradesh, India.  
This project is submitted as part of the 3rd Semester Project on Python Programming.
