"""
Konwersja temperatury
Napisz program, który konwertuje temperature z stopni Celsjusza na Fahrenheita.
Uzyj zmiennej typu float dla temperatury w Celsjuszach i zastosuj odpowiedni wzór do konwersji.
"""
def func(zmienna1):
    zmienna2 = (2 * zmienna1) + 30
    return zmienna2

print(func(10))

"""
Kalkulator BMI:
Stwörz prosty kalkulator BMI. Uzyj zmiennych typu float dla wagi (w kg) i wzrostu (w metrach). 
Oblicz BMI i wyswietl wynik zaokraglony do dwöch miejsc po przecinku.
"""
def bmiCalc(waga, wzrost):
    bmi = waga / wzrost
    print(type(waga), type(wzrost))
    print(round(bmi,2))


bmiCalc(65.0, 1.75)

"""
Formatowanie stringu:
Utwörz zmienne zawierajace imie, nazwisko i wiek osoby. Uzyj formatowania stringu, aby wyswietlié zdanie: 
"Nazywam sie (imiel (nazwisko] i mam (wiek] lat."
"""
imie = "Adam"
nazwisko = "Majewski"
wiek = 68
print("Nazywam się " + imie + " " + nazwisko +" i mam " + str(wiek) + " lat.")

"""
Obliczanie rabatu:
Zadeklaruj zmienne reprezentujace cene produktu i procent rabatu. 
Oblicz cene po rabacie i wyswietl ja, zaokraglajac do dwóch miejsc po przecinku.
"""
def obliczCene(cenaProd, rabat):
    koszt = cenaProd
    final = (cenaProd * rabat)
    print("Cena po rabacie: " + str(koszt - final) )

cenaProd = 100.00
rabat = 0.10

obliczCene(cenaProd, rabat)

"""
Sprawdzanie podzielnosci:
Utwórz dwie zmienne catkowitoliczbowe. Sprawdz, czy pierwsza liczba jest podzielna przez druga bez 
reszty i wyswietl odpowiedni komunikat.
"""
def dzielenieCalkowite(zmienna1, zmienna2):
    print(zmienna1%zmienna2)

dzielenieCalkowite(12,33)

"""
Manipulacja stringiem:
Zadeklaruj zmienna zawierajaca dowolne zdanie. Policz i wyswietl liczbe stow w tym zdaniu 
(zaktadajac, ze stowa sa oddzielone pojedynczymi spacjami).
"""
zdanie = "Każda klapa ma swojego starszego brata"
x = zdanie.count(" ") - 1
print(x)

"""
Kalkulator czasu:
Napisz program, ktory konwertuje podana liczbe minut na godziny i minuty.
Na przyktad, 145 minut powinno byc wyswietlone jako "2 godziny i 25 minut".
"""
czasMin = 234334
minuty = int(czasMin%60)
godziny = czasMin/60
print(str(int(godziny)) + " i " + str(minuty) + " minut")

"""
Porównywanie liczb:
Utwórz trzy zmienne z róznymi wartosciami liczbowymi. Uzyj operatorów porównania, 
aby znalezc i wyswietlic najwieksza z nich.
"""
def porownaj(li1, li2, li3):
    if li1 > li2 and li1 > li3:
        print(li1)
    else:
        if  li2 > li3 and li2 > li1:
            print(li2)
        else:
            if li3 > li1 and li3 > li2:
                print(li3)

porownaj(3,2,1)

"""
Obliczanie pola trójkata:
Zadeklaruj zmienne reprezentujace diugosé podstawy i wysokosé trójkata.
Oblicz i wyswietl pole trójkata, uzywajac odpowiedniego wzoru.
"""

def obliczPoleTrojkata(podstawa, wysokosc):
    pole = (podstawa * wysokosc) / 2
    return int(pole)

wynik = obliczPoleTrojkata(10,20)
print(wynik)

"""
Manipulacja stringiem z uzyciem indeksów:
Utwórz zmienna zawierajaca dowolne stowo. Wyswietl to stowo od tytu, 
uzywajac indeksowania i krokow
"""
# Utworzenie zmiennej zawierającej dowolne słowo
slowo = "Python"

# Wyświetlenie słowa od tyłu
odwrocone_slowo = slowo[::-1]

# Wyświetlenie wyniku
print(odwrocone_slowo)






