from abc import ABC, abstractmethod
import keyboard
from database.repository import delete_contact, update_contact, add_contact, show, show_all


def input_with_default(prompt_, default_):
    print(prompt_, end="\n")
    keyboard.write(default_)
    return input()


class IReply(ABC):
    @abstractmethod
    def reply(self):
        pass


class Contacts_Visuals(IReply):
    def show_all(self, *_):
        for each in show_all():
            each = each.to_mongo().to_dict()
            print(f"Fullname: {each.get('fullname')}")
            print(f"    Email: {each.get('email')}")
            print(f"    Phone: {each.get('cell_phone')}")
            if each.get('address'):
                print(f"    Address: {each.get('address')}")

    def show_contact(self, data):
        contact = show(data.strip())
        if not contact:
            print("No contact was found!")
        else:
            print(f"Fullname: {contact.get('fullname')}")
            print(f"    Email: {contact.get('email')}")
            print(f"    Phone: {contact.get('cell_phone')}")
            if contact.get('address'):
                print(f"    Address: {contact.get('address')}")

    def reply(self):
        pass


class ManipulateContacts(IReply):
    def update_contact(self, fullname: str):
        contact = show(fullname.strip())
        if contact:
            print(f"Redacting contact {contact.get('fullname')}:")
            fullname_ = input_with_default("Fullname: ", contact.get("fullname"))
            email = input_with_default("Email: ", contact.get("email"))
            phone = input_with_default("Phone: ", contact.get("cell_phone"))
            address = input_with_default("Address: ",
                                         [contact.get("address") if contact.get("address") is not None else "None"])
            if address == "" or address == "None":
                address = None
            update_contact(fullname.strip(), fullname_=fullname_, email=email, phone=phone, address=address)
        else:
            print("No contact was found!")
    def remove_contact(self, fullname):
        if fullname.strip() == "":
            print("Can`t delete an '' contact! Enter help to get help")
        else:
            if input("Are you sure? y/n: ").lower() == "y":
                delete_contact(fullname.strip())
            else:
                print("Operation canceled")

    def add_contact(self, _):
        print(f"Creating new contact:")
        fullname = input("Fullname: ")
        email = input("Email: ")
        phone = input("Phone: ")
        address = input("Address: ")
        if address == "" or address == " ":
            address = None
        add_contact(fullname, email, phone, address)
        print("Contact created")

    def reply(self):
        pass


def help_me(_):
    print("""
    hello: hello,
    good bye: closes app,
    add contact: adds a contact,
    delete contact [contact fullname]: deletes a contact
    show contact [contact fullname]: shows a certain contact
    show all: shows all contacts
    help: Shows this list"""
          )


visuals = Contacts_Visuals()
ch4nge = ManipulateContacts()
#
# if __name__ == '__main__':
#     ch4nge = ManipulateContacts()
#     ch4nge.add_contact("e")
# my = Contacts_Visuals()
# my.show_all()
# my.show_contact("Jerry Thompson")
