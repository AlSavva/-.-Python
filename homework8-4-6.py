# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
# склад. А также класс «Оргтехника», который будет базовым для классов-
# наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных
# типов. В классах-наследниках реализовать параметры, уникальные для каждого
# типа оргтехники.

def random_storage():
    from random import randint
    brand_list_print = ['hp', 'canon', 'epson', 'samsung']
    brand_list_scanner = ['hp', 'brother', 'epson', 'minolta']
    brand_list_copier = ['xerox', 'canon', 'epson', 'kyocera']
    my_storage = Storage()
    for i in range(1, 7):
        i = randint(0, 3)
        my_storage.add_product(
            Printer(brand_list_print[i], randint(100, 2000), 'laser'),
            randint(5, 11))
        i = randint(0, 3)
        my_storage.add_product(
            Scanner(brand_list_scanner[i], randint(100, 2000), 'laser'),
            randint(5, 11))
        i = randint(0, 3)
        my_storage.add_product(
            Copier(brand_list_copier[i], randint(100, 2000), 'laser'),
            randint(5, 11))
    print(my_storage)
    return my_storage


class StorageError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:

    def __init__(self, store_dict={}):
        self.store_dict = store_dict
        int_report = {}
        self.int_report = int_report

    def __str__(self):
        output = ''
        for name, prod in self.store_dict.items():
            output += f'{name}:\n'
            for brand, count in prod.items():
                output += f'\t{brand} {count}\n'
        return f'Storage condition:\n{output}'

    def out_prod_report(self):
        output = ''
        for where, what in self.int_report.items():
            output += f'{where}:\n'
            for type, brand in what.items():
                output += f'\t{type}:\n'
                for item, count in brand.items():
                    output += f'\t\t{item} {count}\n'
        return f'Storage out-product report:\n{output}'

    def add_product(self, product, count):

        if product.name not in self.store_dict:
            self.store_dict[product.name] = {}
            self.store_dict[product.name][product.brand] = count
        elif product.brand not in self.store_dict[product.name]:
            self.store_dict[product.name][product.brand] = count
        else:
            self.store_dict[product.name][product.brand] += count

    def product_out(self, product, count, where):
        try:
            if product.name not in self.store_dict:
                raise StorageError(f'StorageError! "{product.name}" '
                                   f'out of storage!')
            elif product.brand not in self.store_dict[product.name]:
                raise StorageError(f'StorageError! '
                                   f'{product.name} "{product.brand}" '
                                   f'out of storage!')
            elif self.store_dict[product.name][product.brand] - count < 0:
                raise StorageError(f'StorageError! '
                                   f'{product.name} "{product.brand}" '
                                   f'You need {count}, but '
                                   f'storage balance only'
                                   f' {self.store_dict[product.name][product.brand]}!')
            else:
                self.store_dict[product.name][product.brand] -= count
                if where not in self.int_report:
                    self.int_report[where] = {}
                    self.int_report[where][product.name] = {}
                    self.int_report[where][product.name][product.brand] = count
                elif product.name not in self.int_report[where]:
                    self.int_report[where][product.name] = {}
                    self.int_report[where][product.name][product.brand] = count
                elif product.brand not in self.int_report[where][product.name]:
                    self.int_report[where][product.name][product.brand] = count
                else:
                    self.int_report[where][product.name][
                        product.brand] += count
        except StorageError as err:
            print(err)


class OfficeEquipment:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
        self.dict_tech = {"Name": self.name, "Brand": self.brand,
                          "Price": self.price}

    @property
    def info(self):
        return f'{self.dict_tech}'


class Printer(OfficeEquipment):
    def __init__(self, brand, price, types, name='printer'):
        super().__init__(name, brand, price)
        self.name = name
        self.types = types
        self.dict_tech = {"Name": self.name, "Brand": self.brand,
                          "Price": self.price, "Type": self.types}


class Scanner(OfficeEquipment):
    def __init__(self, brand, price, resolution, name='scanner'):
        super().__init__(name, brand, price)
        self.name = name
        self.resolution = resolution
        self.dict_tech = {"Name": self.name, "Brand": self.brand,
                          "Price": self.price, "Resolution": self.resolution}


class Copier(OfficeEquipment):
    def __init__(self, brand, price, copy_speed, name='copier'):
        super().__init__(name, brand, price)
        self.name = name
        self.copy_speed = copy_speed
        self.dict_tech = {"Name": self.name, "Brand": self.brand,
                          "Price": self.price, "Copy speed": self.copy_speed}


m = random_storage()  # Создали склад с рандомным наполнением

a = OfficeEquipment('computer', 'hp', 1200)
it = OfficeEquipment('slave', 'spartakus', 300)
pr = Printer('canon', 1200, 'laser')
sc = Scanner('epson', 1000, '1200/980')
cop = Copier('xerox', 3500, '50p/s')
ap = Printer('hp', 3500, 'struyny')
print(pr.info)
print(a.info)
print(pr.name)
product_type = pr.__class__.__name__
print(product_type)
print(m.store_dict)
m.add_product(sc, 2)
print(r"Добавили на склад Scanner('epson', 1000, '1200/980') 2 шт.")
m.add_product(pr, 3)
print(r"Добавили на склад Printer('canon', 1200, 'laser') 3 шт.")
m.add_product(it, 300)
print(r"Добавили на склад OfficeEquipment('slave', 'spartakus', 300) 300 шт.")
print('Печатаем состояние склада')
print(m)
print(r"Забираем со склада Printer('canon', 1200, 'laser') 3 шт. в отдел buh")
m.product_out(pr, 3, 'buh')
print(
    r"Забираем со склада Printer('canon', 1200, 'laser') 2 шт. в отдел office")
m.product_out(pr, 2, 'office')
print('Печатаем словарь выбывших товаров')
print(m.int_report)
print(
    r"Забираем со склада Scanner('epson', 1000, '1200/980') 200 шт. в отдел buh")
m.product_out(sc, 200, 'buh')
print(
    r"Забираем со склада OfficeEquipment('slave', 'spartakus', 300) 9 шт. в отдел it")
m.product_out(it, 9, 'it')
print(m)

print(m.out_prod_report())
