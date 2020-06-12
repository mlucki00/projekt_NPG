import smtplib, ssl, time

class Contact:
    def __init__(self, name, surname, email, group):
        self.name = name
        self.surname = surname
        self.email = email
        self.group = group

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

def addContact(contacts):
        name = input("Podaj swoje imię: ")
        surname = input("Podaj swoje nazwisko: ")
        email = input("Podaj adres email: ")
        group = input("Podaj grupę: ")
        
        if " " in name:
            print("Błąd. Zła składnia imienia")
            return contacts, 0
        
        elif " " in surname:
            print("Błąd. Zła składnia nazwiska")
            return contacts, 0
        
        elif " " in email:
            print("Błąd. Zła składnia emaila")
            return contacts, 0
        
        elif " " in group:
            print("Błąd. Zła składnia grupy")
            return contacts, 0
        
        else:
            contacts.append(Contact(name, surname, email, group)
            contacts.sort(key=alphabeticalorder)
            for id, c in enumerate(contacts):
                if c.name==name_ and c.surname==surname_ and c.email==email_ and c.group==group_:
                    result_id = id
        return contacts, result_id


def findcontact(name_, surname_, contacts):
    result = -1
    for id,c in enumerate(contacts):
        if c.name==name_ and c.surname==surname_:
            result = id
    return result


def sendmail(mail):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "projeknpg@gmail.com"
    receiver_email = mail
    password = "zaliczenie_projektu2020"
    print("podaj temat maila")
    subject = input()
    print("podaj tresc maila")
    content = input()
    message = """\
    {}

    {}""".format(subject, content)

    print("Trwa wysylanie...")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("Wyslano")

def main():
    return 0


main()
