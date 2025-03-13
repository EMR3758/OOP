#__init__ metodu,bir sınıfın yapıcı(constructor) metodududur.Bir sınıfın yeni bir örneği(instance) oluşturulduğunda otomatik olarak çağrılır ve nesnenin başlangıç durumunu ayarlamak için kullanılır.

class Araba:
    def __init__(self,marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil 
        
    def bilgileri_göster(self):
        return f"{self.yil}     {self.marka}    {self.marka}"

#Nesne oluşturma 
araba1=Araba("Toyota","Corolla",2018)

print(araba1.bilgileri_göster())