from mongoengine import Document, StringField, connect

connect(db='web7', host='mongodb+srv://test:BybtDZ1GFpulQIoH@cluster0.khjhand.mongodb.net/?retryWrites=true&w=majority')


class Contact(Document):
    fullname = StringField(max_length=120, nullable=False, required=True)
    email = StringField(max_length=120, nullable=True)
    cell_phone = StringField(max_length=120, nullable=True)
    address = StringField(max_length=120, nullable=True)
