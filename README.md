# Basic Rule-Based Chatbot Using Python

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A beginner-friendly, console-based chatbot built using Python for the **CodeAlpha Python Programming Internship**. This chatbot uses simple rule-based logic with `if-elif-else` conditions to respond to user messages.

## 📝 Project Description

This is a simple command-line chatbot that interacts with users through text-based conversations. It understands predefined commands and responds accordingly. The chatbot demonstrates fundamental Python programming concepts including functions, loops, conditional statements, and user input handling.

## ✨ Features

- **Console-based Interface**: Runs entirely in the terminal/command prompt
- **Rule-based Responses**: Uses `if-elif-else` conditions to match user inputs
- **Case-Insensitive**: Understands commands regardless of letter casing (HELLO, hello, Hello)
- **Continuous Conversation**: Keeps chatting until the user types 'bye'
- **Help Command**: Displays available commands when needed
- **Error Handling**: Gracefully handles empty inputs and interruptions
- **Clean Code**: Well-organized with functions and comments for easy understanding

## 🎯 Supported Commands

| Command | Bot Response |
|---------|--------------|
| `hello` | Hi! How can I help you? |
| `hi` | Hello! |
| `how are you` | I'm fine, thanks! How about you? |
| `what is your name` | I'm Python Bot. Nice to meet you! |
| `help` | Displays all available commands |
| `bye` | Goodbye! Have a great day! 👋 (exits the chat) |
| *Unknown* | Sorry, I don't understand that message... |

## 🛠️ Requirements

- **Python 3.6 or higher**
- No external libraries or dependencies required
- Works on Windows, macOS, and Linux

## 🚀 How to Run the Chatbot

### Step 1: Download the Code
Clone or download this repository to your computer.

### Step 2: Open Terminal/Command Prompt
Navigate to the project folder:
```bash
cd path/to/Based\ Chatbot\ Using\ Python
```

### Step 3: Run the Chatbot
Execute the following command:
```bash
python chatbot.py
```

### Step 4: Start Chatting!
Type your messages and press Enter. The bot will respond based on the predefined rules.

### Step 5: Exit
Type `bye` and press Enter to exit the chatbot.

## 💬 Sample Conversation

```
==================================================
🤖 Welcome to Python Bot! 🤖
==================================================
I'm here to chat with you!
Type 'help' to see what I can do.
Type 'bye' to exit the chat.

You: hello
Bot: Hi! How can I help you?

You: what is your name
Bot: I'm Python Bot. Nice to meet you!

You: how are you
Bot: I'm fine, thanks! How about you?

You: help

📋 Here are the commands I understand:
  - hello         : I'll greet you
  - hi            : A simple greeting
  - how are you   : Ask about my well-being
  - what is your name : Know my name
  - help          : Show this help message
  - bye           : Exit the chat

You: where are you from
Bot: Sorry, I don't understand that message. Type 'help' to see available commands.

You: bye
Bot: Goodbye! Have a great day! 👋
```

## 📂 Project Structure

```
Based Chatbot Using Python/
│
├── chatbot.py          # Main Python source code
├── README.md           # Project documentation (this file)
└── EXPLANATION.md      # Detailed code explanation in English & Tanglish
```

## 🎓 Learning Objectives

This project demonstrates the following Python concepts:

1. **Functions**: Organizing code into reusable blocks
2. **Input/Output**: Using `input()` and `print()` for user interaction
3. **String Methods**: `.lower()`, `.strip()` for text processing
4. **Conditional Statements**: `if-elif-else` for decision making
5. **Loops**: `while` loop for continuous execution
6. **Boolean Logic**: Controlling program flow
7. **Error Handling**: `try-except` blocks for graceful error management
8. **Comments & Documentation**: Making code readable and maintainable

## 🌐 How to Upload to GitHub

### Step 1: Create a GitHub Repository
1. Go to [GitHub](https://github.com) and log in
2. Click the **"+"** icon → **"New repository"**
3. Repository name: `CodeAlpha_BasicChatbot`
4. Description: *"A simple rule-based chatbot for CodeAlpha Python internship"*
5. Keep it **Public**
6. Click **"Create repository"**

### Step 2: Initialize Git in Your Project Folder
Open terminal in your project folder and run:
```bash
git init
git add .
git commit -m "Initial commit: Basic rule-based chatbot"
```

### Step 3: Connect to GitHub and Push
Replace `YOUR_USERNAME` with your GitHub username:
```bash
git remote add origin https://github.com/YOUR_USERNAME/CodeAlpha_BasicChatbot.git
git branch -M main
git push -u origin main
```

### Step 4: Verify
Refresh your GitHub repository page. You should see all your files uploaded!

## 👨‍💻 About the Developer

This project was created as part of the **CodeAlpha Python Programming Internship** to demonstrate fundamental Python programming skills and problem-solving abilities.

## 📜 License

This project is open-source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this project and add more features such as:
- More conversation topics
- Personality traits
- Time-based greetings
- User name memory
- Conversation history

## 📞 Contact

For questions or feedback about this project, please reach out through GitHub issues.

---

**Happy Coding! 🚀**

*Made with ❤️ for CodeAlpha Python Programming Internship*
