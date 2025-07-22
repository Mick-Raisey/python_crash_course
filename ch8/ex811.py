# 8-11. Archived Messages: Start with your work from Exercise 8-10.
# Call the func tion send_messages() with a copy of the list of messages.
# After calling the function,
# print both of your lists to show that the original list has retained its messages.


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
send_messages(messages[:], sent_messages)

print("\n----- Messages to send -----")
print(messages)
print("\n----- Sent messages -----")

print(sent_messages)
