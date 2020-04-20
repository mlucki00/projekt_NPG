

class Contact:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email


def loadContacts():
    contacts = []

    try:
        with open('ksiazka.txt') as f:
            for x in f:
                arr = x.split()
                name = arr[0]
                surname = arr[1]
                email = arr[2]
                contacts.append(Contact(name, surname, email))
            f.close()
    except IOError:
        f = open('ksiazka.txt','x')
        f.close()

    return contacts


def closeProgram(array):
    try:
        with open('ksiazka.txt',"w") as f:
            content = ""
            for x in array:
                content +="{} {} {}\n".format(x.name, x.surname, x.email)
            f.write(content)
            f.close()
    except IOError:
        print("nie moglem zapisac danych")



def main():

    return 0

main()
