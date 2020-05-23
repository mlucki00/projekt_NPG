

class Contact:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

def alphabeticalorder(obj):
    result :str = obj.name+obj.surname
    return result

def loadcontacts():
    contacts = []
    try:
        with open('ksiazka.txt') as f:
            for x in f:
                arr = x.split()
                name = arr[0]
                surname = arr[1]
                email = arr[2]
                group = arr[3]
                contacts.append(Contact(name, surname, email, group))
            f.close()
    except IOError:
        f = open('ksiazka.txt','x')
        f.close()

    contacts.sort(key=alphabeticalorder)
    return contacts


def closeprogram(contacts):
    try:
        with open('ksiazka.txt',"w") as f:
            content = ""
            for x in contacts:
                content +="{} {} {} {}\n".format(x.name, x.surname, x.email, x.group)
            f.write(content)
            f.close()
    except IOError:
        print("nie moglem zapisac danych")



def main():

    return 0


main()
