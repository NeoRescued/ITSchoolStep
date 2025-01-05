#task1
class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def display_info(self):
        return (f"Модель: {self.model}\n"
                f"Рік випуску: {self.year}\n"
                f"Виробник: {self.manufacturer}\n"
                f"Об'єм двигуна: {self.engine_volume} л\n"
                f"Колір: {self.color}\n"
                f"Ціна: {self.price} USD")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Ціна оновлена: {self.price} USD")

car = Car("Toyota Camry", 2022, "Toyota", 2.5, "Чорний", 35000)
print(car.display_info())
car.update_price(34000)

#task2
class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        return (f"Назва: {self.title}\n"
                f"Рік видання: {self.year}\n"
                f"Видавець: {self.publisher}\n"
                f"Жанр: {self.genre}\n"
                f"Автор: {self.author}\n"
                f"Ціна: {self.price} USD")

    def change_genre(self, new_genre):
        self.genre = new_genre
        print(f"Жанр оновлено: {self.genre}")

book = Book("Війна і мир", 1869, "Видавництво А", "Роман", "Лев Толстой", 20)
print(book.display_info())
book.change_genre("Історичний роман")

#task3
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        return (f"Назва стадіону: {self.name}\n"
                f"Дата відкриття: {self.opening_date}\n"
                f"Країна: {self.country}\n"
                f"Місто: {self.city}\n"
                f"Місткість: {self.capacity} місць")

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity
        print(f"Місткість оновлено: {self.capacity} місць")

stadium = Stadium("Олімпійський", "1980-05-01", "Україна", "Київ", 70000)
print(stadium.display_info())
stadium.update_capacity(80000)