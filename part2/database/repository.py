from part2.database.models import Contact


def add_contact(fullname: str, email_: str, phone_: str, address_=None):
    new_contact = Contact(fullname=fullname, email=email_, cell_phone=phone_, address=address_).save()


def delete_contact(fullname: str):
    contact = Contact.objects(fullname=fullname)
    contact.delete()


def update_contact(fullname: str, fullname_: str, email: str, phone: str, address):
    contact = Contact.objects(fullname=fullname)
    contact.update(fullname=fullname_, email=email, cell_phone=phone, address=address)


def show_all():
    contact = Contact.objects()
    return contact


def show(data):
    contact = Contact.objects(fullname=data).first()
    if contact:
        return contact.to_mongo().to_dict()
    else:
        return None

if __name__ == '__main__':
    # add_contact("mama", "papa@gmail.com", "390", "street")
    # delete_contact("Haley Harper")
    # update_contact("Joseph Rogers", "haoe", "anoethao", "tnheao", "haoetn")
    # for each in show_all():
    #     print(each.to_mongo().to_dict())  # .get('email')
    # print(show("Sara Rogers"))
    pass