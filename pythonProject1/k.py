import socket
import threading

nazwy_uzytkownikow=[]
def wyslijtabdost(socket):
    if(nazwy_uzytkownikow.__sizeof__()>0):
        tablica=""
        for x in nazwy_uzytkownikow:
            if(nazwy_uzytkownikow.index(x)%2==0):
                tablica+=f"{x}\n"
        socket.send(tablica.encode('utf-8'))

def wyslij(cl, message):
    cl.send(message.encode('utf-8'))


def myfunction(cls):
    z_kim_polaczyc=0
    if nazwy_uzytkownikow.__contains__(cls) is False:
        wyslij(cls, "NAME")
        nick = cls.recv(1024).decode('utf-8')
        while nazwy_uzytkownikow.__contains__(nick):
            wyslij(cls, "podaj inny nick")
            nick = cls.recv(1024).decode('utf-8')
        nazwy_uzytkownikow.extend([nick])
        nazwy_uzytkownikow.extend([cls])
        print(nick)
        wyslijtabdost(cls)
        wyslij(cls,"podaj z kim chcesz sie polaczyc")
        z_kim=cls.recv(1024).decode('utf-8')
        while bool(nazwy_uzytkownikow.__contains__(z_kim)) == False:
            wyslij(cls,"podany uzytkownik nie istnieje podaj nazwe jeszcze raz")
            z_kim = cls.recv(1024).decode('utf-8')
        wyslij(cls,f"|{z_kim}|")
        z_kim_kto.extend([z_kim])
        z_kim_polaczyc = nazwy_uzytkownikow.index(z_kim)



    port_docelowy =nazwy_uzytkownikow.__getitem__(int(z_kim_polaczyc)+1)

    try:
            while True:

                data = cls.recv(1024)
                text = data.decode('utf-8')
                if (text == ""):
                    break
                if text=="?123?":
                    wyslij(cls,"podaj z kim chcesz sie polaczyc")
                    wyslijtabdost(cls)
                    z_kim_lot = cls.recv(1024).decode('utf-8')
                    while bool(nazwy_uzytkownikow.__contains__(z_kim_lot)) == False:
                        wyslij(cls, "podany uzytkownik nie istnieje podaj nazwe jeszcze raz")
                        z_kim_lot = cls.recv(1024).decode('utf-8')#dostajemy nick z kim chcemy sie polaczyc
                    wyslij(cls, z_kim_lot)
                    wyslij(cls, f"|{z_kim_lot}|")
                    index_aktualnego_klienta=nazwy_uzytkownikow.index(cls)-1
                    index_aktualnego_klienta=int(index_aktualnego_klienta/2)
                    z_kim_kto[index_aktualnego_klienta]=z_kim_lot
                    z_kim_polaczyc=nazwy_uzytkownikow.index(z_kim_kto.__getitem__(index_aktualnego_klienta))+1
                    port_docelowy=nazwy_uzytkownikow.__getitem__(int(z_kim_polaczyc))
                    continue
                print(f"Otrzymane dane od {nazwy_uzytkownikow.__getitem__(nazwy_uzytkownikow.index(cls)-1 )}: {text}")

                print("koniec myfunction")
                wyslij(port_docelowy, f"{nazwy_uzytkownikow.__getitem__(nazwy_uzytkownikow.index(cls)-1 )}:{text}")
    except:
        index_cls=int(nazwy_uzytkownikow.index(cls))
        nazwy_uzytkownikow.__delitem__(index_cls)
        nazwy_uzytkownikow.__delitem__(index_cls-1)


z_kim_kto = []

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = '127.0.0.1'
    server_port = 55556
    server_socket.bind((server_address, server_port))
    server_socket.listen(5)

    while True:
        print("Czekam na połączenie...")
        client_socket, client_address = server_socket.accept()

        xd = threading.Thread(target=myfunction, args=(client_socket,))
        xd.start()
        server_socket.close()


if __name__ == "__main__":
    main()
