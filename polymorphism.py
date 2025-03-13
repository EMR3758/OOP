class Hayvan:
    def ses_cikar(self):
        raise NotImplementedError("Bu metod alt sınıflar tarafından çağırılmalıdır.")

class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav"

class Köpek(Hayvan):
    def ses_cikar(self):
        return "Hav Hav"
    
#Polymorphism kullanımı
hayvanlar = [Kedi(), Köpek()]

for hayvan in hayvanlar:
    print(hayvan.ses_cikar())