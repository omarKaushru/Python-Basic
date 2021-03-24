from tech_product import Tech


class Laptop(Tech):
    def __init__(self, name, price, weight, color, ram, cpu, storage):
        super().__init__(name, price, weight, color)
        self.ram = ram
        self.cpu = cpu
        self.storage = storage

    def set_double_price(self):
        self.price = 2 * self.price

    def change_specs(self, ram, storage):

        if ram > self.ram or storage > self.storage:
            self.price = self.price + 10000

        self.ram = ram
        self.storage = storage

    def __str__(self):
        return f'Name: {self.name}\n Price:{self.price}\n Weight: {self.weight}\n'\
               f'Color: {self.color}\n RAM: {self.ram}\n CPU: {self.cpu}\n'\
               f'Storage: {self.storage}\n'



