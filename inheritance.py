#Kalıtım, nesne yönelimli proglamlamada bir sınıfın (parent/base class) özelliklerini ve metodlarını başka bir sınıfa (child/derived class) aktarmasını sağlayan mekanizmadır.
#Kod tekrarlarını önler.
#Daha düzenli ve yönetilebilir bir yapı oluşturulur.

class Animal:
    def __init__(self,name):
        self.name = name
    
    def make_sound(self):
        print("Some generic animal sound.")
    
    
#Child Class (Derived Class)
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"
    

dog = Dog("Enik")
cat = Cat("Pamuk")

dog.make_sound()
cat.make_sound()

        