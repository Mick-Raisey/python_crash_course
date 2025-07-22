# 8-10.
# Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.


def send_messages(messages, sent_messages):
    """Simple function to move messages from one list to another"""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


messages = [
    "Hello world",
    "I'm learning Python",
    "The third message",
    "Maybe one more for fun",
]

sent_messages = []
send_messages(messages, sent_messages)

print("\n----- Messages to send -----")
print(messages)
print("\n----- Sent messages -----")

print(sent_messages)
