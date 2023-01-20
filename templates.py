from dataclasses import dataclass

@dataclass
class Transaction:
    student:dict = None
    event: dict = None
    product: dict = None
    quantity: int = None
    datetime: any = None
    def format_transaction(self):
        x = {"student": self.student, "event": self.event, "product": self.product, "quantity": self.quantity, "datetime": self.datetime}
        return x


@dataclass
class Student:
    id:str=None
    name:str=None
    email:str = None
    address:dict=None
    def format_dict(self):
        dict = {"id":self.id, "name": self.name, "email":self.email, "address":self.address}
        return dict

@dataclass
class Address:
    street:str =None
    house:str=None #house numbers sometimes include letter eg 12b
    postal_code:str=None
    def format_dict(self):
        dict = {"street": self.street, "house":self.house, "postal_code": self.postal_code}
        return dict
@dataclass
class Product:
    name:str=None
    price:float=None
    barcode:str=None
@dataclass
class Event:
    date:str=None
    location:str=None
