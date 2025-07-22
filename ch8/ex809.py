# 8-9. Messages:
# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(),
# which prints each text message.


def show_messages(messages):
    for message in messages:
        print(message)


messages = [
    "Hello world",
    "I'm learning Python",
    "The third message",
    "Maybe one more for fun",
]

show_messages(messages)
