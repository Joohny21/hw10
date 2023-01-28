from part2.database.models import Contact
from faker import Faker

fake = Faker()


def add_contacts():
    for _ in range(20):
        new_contact = Contact(fullname=fake.name(), email=fake.email(), cell_phone=fake.phone_number(),
                              address=fake.address()).save()
    return None


if __name__ == '__main__':
    add_contacts()
