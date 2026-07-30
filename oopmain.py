import csv
class Item:
    pay_rate = 0.8
    all=[]

    def __init__(self,name: str,price:float ,quantity=0):
        assert price >= 0, "Price must be positive"
        assert quantity >= 0, "Quantity must be positive"
        self.name = name
        self.quantity = quantity
        self.price = price

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price* self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("scratch.csv",'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name= str(item.get('name')),
                price= float(item.get('price')),
                quantity= int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        if isinstance (num,float):
            return num.is_integer()
        elif isinstance (num,int):
            return True


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})')"


class Phone(Item):

    def __init__ (self,name: str,price:float, broken_phones =0, quantity=0):
        super().__init__(
            name,price,quantity
        )

        assert broken_phones >= 0, f"Broken phones {broken_phones} must be positive."

        self.broken_phones = broken_phones



phone1 = Phone("jscPhonev10",500,5,1)

print(Item.all)
print(Phone.all)
