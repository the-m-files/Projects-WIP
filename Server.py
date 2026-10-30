import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 5000))
s.listen()
print("Server established")

client, adress = s.accept()
while True:

    Uinput = input("Type to send to client >>>")

    raw_data = client.recv(1024)

    decoded_data = raw_data.decode()

    print(f"{adress}>>> {decoded_data}")

    client.sendall((Uinput).encode("utf-8"))
    if decoded_data == "Close_Con":
        client.sendall(("Close_Con").encode("utf-8"))
        break

s.close()
print("server closed")