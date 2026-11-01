"""Test script to demonstrate chatbot functionality."""

from chatbot import get_bot_response, display_welcome_message, display_help

def simulate_conversation():
    """Simulate a sample conversation with the chatbot."""
    
    # Display welcome message
    display_welcome_message()
    
    # Test cases: (user_input, expected_behavior)
    test_messages = [
        "hello",
        "what is your name",
        "how are you",
        "HELLO",  # Test case insensitivity
        "  hi  ",  # Test with extra spaces
        "help",
        "where are you from",  # Unknown command
        "bye"
    ]
    
    for message in test_messages:
        print(f"You: {message}")
        response = get_bot_response(message)
        
        if response is None:
            display_help()
        else:
            print(f"Bot: {response}\n")

if __name__ == "__main__":
    print("=" * 50)
    print("CHATBOT TEST - Sample Conversation")
    print("=" * 50)
    print()
    simulate_conversation()
    print("\n" + "=" * 50)
    print("✅ Test completed successfully!")
    print("=" * 50)
