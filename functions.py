import imapclient
import imaplib
import fileinput
import multiprocessing
import threading
import eel

eel.init('front')


@eel.expose
def dummy(data):
    print("Hello from eel", data)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}


@eel.expose
def add2List(email2add):
    try:
        if email2add != "":
            f = open("./assets/data/emails2remove.txt", "a+")
            f.write(email2add)
            f.write("\n")
            f.close()
            return(email2add + " added to the list.\n")
        else:
            return("You need to fill all entries.\n")

    except Exception as e:
        return("Ha ocurrido un error [ERROR]" + e + " .\n")


@eel.expose
def removeFromList(email2remove):
    try:
        if email2remove != "":
            with fileinput.FileInput("./assets/data/emails2remove.txt", inplace=True, backup='.bak') as f:
                for line in f:
                    print(line.replace(email2remove, ""), end='')

            return(email2remove + " removed from the list.\n")
        else:
            return("You need to fill all entries.\n")

    except Exception as e:
        return("Ha ocurrido un error [ERROR]" + e + " .\n")


@eel.expose
def readList():
    # Open a file: file
    file = open("./assets/data/emails2remove.txt", mode='r')
    # read all lines at once
    all_of_it = file.read()
    # close the file
    file.close()

    return all_of_it


"""
def callCleaner(email, passwd):

    try:
        if email != "" and passwd != "":
            process = threading.Thread(target=cleaner, args=(email, passwd,))
            process.start()
            return "Error"
        else:
            return("You need to fill all entries.\n")

    except Exception as e:
        return("Ha ocurrido un error [ERROR]" + e + " .\n")
"""


@eel.expose
def cleaner(email, passwd):
    total_Deleted = 0
    fileList = open("./assets/data/emails2remove.txt", "r")

    # Hace una llamada a un servidor de IMAP para establecer las conexiones, en este caso se utiliza gmail
    i = imapclient.IMAPClient('imap.gmail.com')

    # Conexiones con distintas cuentas
    try:
        if email != "" and passwd != "":
            i.login(email, passwd)
            # Selecciona la carpeta de INBOX y cualquier archivo
            i.select_folder('INBOX', readonly=False)

            # Recorre la lista de correos anterior
            for mail in fileList.read().split('\n'):
                if mail != "":
                    # Recoge el id del correo recivido de la lista anterior devolviendo otra lista de ids del mensaje
                    uids = i.search(['FROM', mail])
                    # Recorremos la lista de ids obtenida
                    for uid in uids:
                        # Borra el mensaje con el id recogido anteriormente
                        i.delete_messages([uid])
                        # Muestra por consola el id del mensaje borrado (Nota, es posible que se pueda mostrar el nombre del mensaje borrado en vez del id)
                        print('Deleted--->'+str(uid)+".\n")
                        # Aumenta la variable de totals de correos borrados
                        total_Deleted += 1

            # Desconectamos del servidor
            i.logout()

            # Muestra por consola el total de correos eliminados
            return(str(total_Deleted) + " e-mails has been removed.\n")
        else:
            return("You need to fill all entries.\n")

    except Exception as e:

        return("Ha ocurrido un error [ERROR]" + str(e) + " .\n")


eel.start('index.html', size=(1300, 900))
