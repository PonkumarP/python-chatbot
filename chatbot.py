"""
Basic Rule-Based Chatbot
========================
A simple console-based chatbot that responds to predefined messages.
Created for CodeAlpha Python Programming Internship.

Author: [Your Name]
Date: 2026-10-29
"""

def display_welcome_message():
    """Display a welcome message when the chatbot starts."""
    print("=" * 50)
    print("🤖 Welcome to Python Bot! 🤖")
    print("=" * 50)
    print("I'm here to chat with you!")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit the chat.\n")


def display_help():
    """Display all the commands that the chatbot understands."""
    print("\n📋 Here are the commands I understand:")
    print("  - hello         : I'll greet you")
    print("  - hi            : A simple greeting")
    print("  - how are you   : Ask about my well-being")
    print("  - what is your name : Know my name")
    print("  - help          : Show this help message")
    print("  - bye           : Exit the chat\n")


def get_bot_response(user_message):
    """Generate a response based on the user's message.
    
    Parameters:
        user_message (str): The message typed by the user
        
    Returns:
        str: The bot's response to the user's message
    """
    # Convert the message to lowercase for case-insensitive matching
    message = user_message.lower().strip()
    
    # Check the message and return appropriate response
    if message == "hello":
        return "Hi! How can I help you?"
    
    elif message == "hi":
        return "Hello!"
    
    elif message == "how are you":
        return "I'm fine, thanks! How about you?"
    
    elif message == "what is your name":
        return "I'm Python Bot. Nice to meet you!"
    
    elif message == "help":
        # Return None to indicate we should call display_help() instead
        return None
    
    elif message == "bye":
        return "Goodbye! Have a great day! 👋"
    
    else:
        # Default response for unknown messages
        return "Sorry, I don't understand that message. Type 'help' to see available commands."


def start_chatbot():
    """Main function to run the chatbot."""
    # Display welcome message at the start
    display_welcome_message()
    
    # Keep the conversation running until user says bye
    chatting = True
    
    while chatting:
        # Get user input
        user_input = input("You: ")
        
        # Check if user entered something
        if not user_input.strip():
            print("Bot: Please type something! 😊\n")
            continue
        
        # Get the bot's response
        response = get_bot_response(user_input)
        
        # If response is None, it means we need to show help
        if response is None:
            display_help()
        else:
            # Display the bot's response
            print(f"Bot: {response}\n")
            
            # Check if user said bye to exit the loop
            if user_input.lower().strip() == "bye":
                chatting = False


if __name__ == "__main__":
    try:
        start_chatbot()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nBot: Chat interrupted. Goodbye! 👋")
    except Exception as e:
        # Handle any unexpected errors
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the chatbot.")
