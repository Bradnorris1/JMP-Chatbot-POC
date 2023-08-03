import tkinter as tk
from tkinter import messagebox
import random

# Define responses for different types of user inputs
greetings = ["hello", "hi", "hey", "greetings"]
thank_you = ["thank you", "thanks", "appreciate it", "thank you so much"]
goodbyes = ["bye", "goodbye", "see you", "take care"]
unknown = [
    "I'm sorry, but I'm not familiar with that. Could you please ask something else?",
    "I'm afraid I don't have information on that. Is there anything else I can help with?",
    "I apologize, but I don't have knowledge about that. Can I assist you with something else?",
]

# Define a function to handle user input and provide appropriate responses
def handle_user_input(event=None):
    user_input = user_input_entry.get()
    add_to_chat_history("User: " + user_input)

    if user_input.lower() in greetings:
        response = "Hello! How can I assist you with JMP software today?"
        add_to_chat_history("Jumpy: " + response)

    elif user_input.lower() in thank_you:
        response = "You're welcome! If you have any more questions, feel free to ask."
        add_to_chat_history("Jumpy: " + response)

    elif user_input.lower() in goodbyes:
        response = "Goodbye! Have a great day!"
        add_to_chat_history("Jumpy: " + response)

    elif "import" in user_input.lower():
        if "text data" in user_input.lower():
            response = "To import text data in JMP software, you can use the 'Import Text Data' feature."
        elif "excel data" in user_input.lower():
            response = "To import Excel data in JMP software, you can use the 'Import Excel Data' feature."
        elif "xml data" in user_input.lower():
            response = "To import XML data in JMP software, you can use the 'Import XML Data' feature."
        elif "json data" in user_input.lower():
            response = "To import JSON data in JMP software, you can use the 'Import JSON Data' feature."
        elif "sas data" in user_input.lower():
            response = "To import SAS data in JMP software, you can use the 'Import SAS Data' feature."
        elif "multiple files" in user_input.lower():
            response = "To import multiple files in JMP software, you can use the 'Import Multiple Files' feature."
        elif "pdf data" in user_input.lower():
            response = "To import PDF data in JMP software, you can use the 'Import PDF Data' feature."
        elif "csv data" in user_input.lower():
            response = "To import CSV data in JMP software, you can use the 'Import CSV Data' feature."
        elif "r data" in user_input.lower():
            response = "To import R data in JMP software, you can use the 'Import R Data' feature."
        elif "python data" in user_input.lower():
            response = "To import Python data in JMP software, you can use the 'Import Python Data' feature."
        elif "matlab data" in user_input.lower():
            response = "To import MATLAB data in JMP software, you can use the 'Import MATLAB Data' feature."
        elif "import" in user_input.lower():
            response = "Sure! Which type of data would you like to import? Please specify one of the following: text data, Excel data, XML data, JSON data, SAS data, multiple files, PDF data, CSV data, R data, Python data, MATLAB data."
        else:
            response = "I'm sorry, I couldn't understand which type of data you want to import. Could you please specify?"

        add_to_chat_history("Jumpy: " + response)

    else:
        response = random.choice(unknown)
        add_to_chat_history("Jumpy: " + response)

    user_input_entry.delete(0, tk.END)


# Function to add a message to the chat history
def add_to_chat_history(message):
    chat_history_text.config(state=tk.NORMAL)
    chat_history_text.insert(tk.END, message + "\n")
    chat_history_text.config(state=tk.DISABLED)
    chat_history_text.see(tk.END)


# Create the main window
window = tk.Tk()
window.title("JMP Software Chatbot")

# Create a text widget to display the chat history
chat_history_text = tk.Text(window, height=10, width=50, state=tk.DISABLED)
chat_history_text.pack(fill=tk.BOTH, expand=True)

# Create a label for instructions
instructions_label = tk.Label(window, text="Enter your message:")
instructions_label.pack()

# Create an entry field for user input
user_input_entry = tk.Entry(window)
user_input_entry.pack()

# Bind the enter key to the user input entry field
user_input_entry.bind("<Return>", handle_user_input)

# Configure window resizing behavior
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Run the main event loop
window.mainloop()
