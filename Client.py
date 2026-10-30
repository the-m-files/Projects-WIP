import socket

csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

csock.connect(("172.26.32.1", 5000))

# while True:
#     csock.sendall(("This message was sent by the client").encode("utf-8"))
#     response = csock.recv(1024)

#     print(response.decode("utf-8"))
#     decoded_data = response.decode("utf-8")
#     if decoded_data == "Close_Con":
#         break


while True:
    message = input("Type to send to server >>> ")

    csock.sendall(message.encode("utf-8"))

    response = csock.recv(1024)
    print(response.decode("utf-8"))

    if message == "Close_Con":
        break

csock.close()
