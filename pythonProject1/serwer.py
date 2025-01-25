import socket
import threading

users={}
def send_avaliable_users(cls):
    global users
    tab_text=""
    tab_text.join(users.keys())
    send_message(cls,"czemu to nie dziala")
def send_message(cls,message):
    cls.send(message.encode('utf-8'))
def get_message(cls):
    return cls.recv(1024).decode('utf-8')


def menage_messages(message:str):
    message.split("|")
def register_user(message,cls):
    send_message(cls,"please sen me your nick")

    while users.__contains__(message):
        send_message(cls,"this name is occupied, write another name")
        message=get_message(cls)
    users[message]=cls
    send_avaliable_users(cls)
    print(message)

def main_prgram(cls):
    while True:
        thread = threading.Thread(target=register_user,args=(get_message(cls),cls,))
        thread.start()
        thread.join()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = '127.0.0.1'
    server_port = 555
    server_socket.bind((server_address, server_port))
    server_socket.listen(5)


    while True:
        print("Czekam na połączenie...")
        client_socket, client_address = server_socket.accept()

        xd = threading.Thread(target=main_prgram, args=(client_socket,))
        xd.start()


if __name__ == "__main__":
    main()