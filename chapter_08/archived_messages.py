messages = ['hello world', 'hi there', 'ola']

def send_messages(messages_to_send, sent_messages):
    while messages_to_send:
        message = messages_to_send.pop()
        print(message)
        sent_messages.append(message)

sent_messages = []

send_messages(messages[:], sent_messages)

print('messages are: ', messages)
print('sent messages are: ', sent_messages)
