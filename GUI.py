from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import gradio as gr
from datetime import datetime

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

# Chain the prompt with the model
chain = prompt | model

# Define a function to handle the conversation
def handle_conversation(user_input, history):
    # Use only the last 3 exchanges to reduce latency
    recent_history = history[-3:] if len(history) > 3 else history
    context = "\n".join([f"User: {h[0]} ({h[2]})\nAI: {h[1]} ({h[3]})" for h in recent_history])
    
    # Capture the current time in the desired format
    timestamp = datetime.now().strftime("%A %d-%m-%Y %H:%M%p")  # Example: "Wednesday 30-11-2024 14:05AM"
    
    # Get the AI response
    result = chain.invoke({"context": context, "question": user_input})
    
    # Append user input and AI response along with timestamps to history
    history.append((user_input, result, timestamp, timestamp))
    return history, result

# Function to save the conversation to a file
def save_conversation(history):
    filename = "conversation_history.txt"
    with open(filename, "w") as file:
        for user_input, bot_response, user_time, bot_time in history:
            file.write(f"User: {user_input} ({user_time})\n")
            file.write(f"AI: {bot_response} ({bot_time})\n")
            file.write("\n")  # Add spacing between exchanges
    return f"Conversation saved to {filename}"

# Create the Gradio interface
with gr.Blocks(css="""
    #header {
        background-color: #4CAF50; /* Green theme color */
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
    }
    #chatbot {
        border: 1px solid #4CAF50;
        border-radius: 10px;
        padding: 15px;
        background-color: #f9f9f9;
    }
    #save-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        font-size: 16px;
    }
    #save-button:hover {
        background-color: #45a049;
    }
""") as demo:
    # Add a custom theme header
    gr.HTML("<div id='header'>AI Chatbot</div>")
    
    chatbot = gr.Chatbot(label="Chat Conversation", elem_id="chatbot")
    user_input = gr.Textbox(label="Type your question here and press Enter!")
    
    # Add a state to store conversation history
    history_state = gr.State([])

    # Define the submit function
    def submit(user_input, history):
        history, bot_response = handle_conversation(user_input, history)
        chatbot_value = [
            (
                f"User: {h[0]} <small style='font-size: 10px; color: gray;'>({h[2]})</small>",
                f"AI: {h[1]} <small style='font-size: 10px; color: gray;'>({h[3]})</small>",
            )
            for h in history
        ]
        return history, chatbot_value, ""  # Return updated history, chatbot, and clear input box

    # Define the save function
    def save(history):
        return save_conversation(history)
    
    # Link the submit function to the textbox
    user_input.submit(submit, [user_input, history_state], [history_state, chatbot, user_input])
    
    # Add a styled save button
    save_button = gr.Button("press here to save your chat!!!", elem_id="save-button")
    save_button.click(save, inputs=[history_state], outputs=gr.Text(label="Save Status"))

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch(share=True)
