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

def editcontact(contacts, id):
    print("Podawaj poszczegolne dane do edycji bez uzywania spacji\n\n")
    print("Podaj imie: ")
    name_ = input()
    print("Podaj nazwisko: ")
    surname_ = input()
    print("Podaj email")
    email_ = input()
    print("Podaj grupe")
    group_ = input()
    lista = [name_,surname_,email_,group_]
    for string in lista:
        for char in string:
            if char == " ":
                napis = "Bledny format w wyrazie: {}. Kontakt nie zostal edytowany".format(string)
                print(napis)
                return contacts
    contacts[id].name = name_
    contacts[id].surname = surname_
    contacts[id].email = email_
    contacts[id].group = group_
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
                if c.name==name and c.surname==surname and c.email==email and c.group==group:
                    result_id = id
        return contacts, result_id


def findcontact(name_, surname_, contacts):
    result = -1
    for id,c in enumerate(contacts):
        if c.name==name_ and c.surname==surname_:
            result = id
    return result
                            
                            
def scrollcontacts(contacts):
    id = 0
    while 1>0:
        #Pusta tablica
        if len(contacts) == 0:
            print("Brak kontaktow. Aby dodac kontakt kliknij 1. Aby zamknac program kliknij 0")
            choice = input()

            #Dodanie kontaktu
            if choice == "1":
                contacts, id = addcontact(contacts)
            #Zamkniecie programu
            elif choice == "0":
                closeprogram(contacts)
                return 0
            #Inne wejscie
            else:
                print("Nie ma takiej opcji")
            time.sleep(1.0)

        #Istnieja kontakty
        else:
            #Wypisanie kontaktu
            c = contacts[id]
            details = "{} {} {} {}\n".format(c.name, c.surname, c.email, c.group)
            print(details)
            options = " Aby dodac kontakt wcisnij 1\n aby usunac kontakt wcisnij 2\n aby wyslac maila wcisnij 3\n aby edytowac kontakt wcisnij 4\n aby wyszukac kontakt wcisnij 5\n aby zobaczyc nastepny kontakt wcisnij w\n aby zobaczyc poprzedni kontakt wcisnij q\n aby wylaczyc program wcisnij 0"
            print(options)
            choice = input()

            #Dodanie kontaktu
            if choice == "1":
                contacts, id = addcontact(contacts)
                c = contacts[id]
                time.sleep(2.0)


            #Usuniecie kontaktu


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
