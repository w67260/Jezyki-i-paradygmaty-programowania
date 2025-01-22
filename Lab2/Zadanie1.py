import re


def Zadanie1(text):
    paragrafy = len(list(filter(lambda x: x == '/n', text)))

    #Sposób 2
    #paragrafy = [p for p in text.strip().split('/n') if p]
    #iloscParagrafow = len(paragrafy)

    zdania = len(list(filter(lambda x: x == '.' or x == '?' or x == '!', text)))

    #Sposób 2
    #zdania = re.split(r'[.?!]+',text)
    #zdania = [tekst.strip() for tekst in zdania if tekst.strip()]
    #iloscZdan = len(zdania)

    slowa = len(list(filter(lambda x: x == ' ' or x == '\n', text)))

    return {
        "Liczba akapitów": paragrafy,
        "Liczba zdań": zdania,
        "Liczba słów": slowa
    }


tekst = "Python to język programowania wysokiego poziomu ogólnego przeznaczenia. Posiada rozbudowany pakiet bibliotek standardowych."
wyniki = Zadanie1(tekst)

for klucz, wartosc in wyniki.items():
    print(f"{klucz}: {wartosc}")