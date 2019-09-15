def nameExist(dict, input):
    if input in dict:
        return True
    else:
        False


def addPersonToAddressbok():
    name = input("Namn: ")
    phone = phonenumberValidation()
    email = emailValidation()
    age = input("Ålder: ")
    p = Person(name, phone, email, age)
    person_info = {"Namn": p.person_name, "Telefonnummer": p.person_number, "Email": p.person_email, "Ålder": p.person_age}

    return person_info


def emailValidation():
    email = input("Epost: ")
    list_with_char = list(email)
    if not (list_with_char.count('@') == 1 and list_with_char.count(".") >= 1):
        raise ValueError('Error\nE-mail måste innehålla ETT "@"-tecken och minst en punkt.')


def phonenumberValidation():
    phone_number = input("Telefonnummer: ")
    list_with_char = list(phone_number)
    for character in list_with_char:
        character = str(character)
        if not character.isdecimal():
            raise ValueError('Error\nTelefon-nummer får endast innehålla siffror')


def ageValidation():
    age = input("Ålder: ")
    number = str(age)
    if number.isdecimal():
        number = int(number)
        return number
    else:
        raise ValueError('Error\nAnge ålder i positivt heltal.')


class Person:

    def __init__(self, person_name, person_number, person_email, person_age):
        self.person_name = person_name
        self.person_number = person_number
        self.person_email = person_email
        self.person_age = person_age


class Addressbok:

    Phonebook = {}

    def __init__(self, person_name, person_info):
        self.person_name = person_name
        self.person_info = person_info
        Addressbok.Phonebook[person_name] = person_info


if __name__ == "__main__":
    loop = True

    while loop:
        name_input = input("Sök efter ett namn i adressboken: ")
        try:
            if nameExist(Addressbok.Phonebook, name_input):
                print(Addressbok.Phonebook[name_input], "\n")

            elif name_input.strip() == "":
                print("Programmet avslutas")
                loop = False

            elif not nameExist(Addressbok.Phonebook, name_input):
                print(f"Hittade inte {name_input}, ny person läggs till adressboken...\n")
                Addressbok.Phonebook[name_input] = addPersonToAddressbok()
        except ValueError as error:
            print(error)
