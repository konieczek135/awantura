def dodaj_cudzyslowy_i_przecinki(plik_wejsciowy, plik_wyjsciowy, cudzyslow='"', przecinek=','):
    """
    Dodaje cudzysłowy i przecinki do każdej linii pliku, usuwając wcześniej wszystkie istniejące cudzysłowy.

    Args:
        plik_wejsciowy (str): Nazwa pliku wejściowego.
        plik_wyjsciowy (str): Nazwa pliku wyjściowego.
        cudzyslow (str, optional): Znak cudzysłowu do dodania. Defaults to '"'.
        przecinek (str, optional): Znak przecinka do dodania. Defaults to ','.
    """

    with open(plik_wejsciowy, 'r', encoding='utf-8') as wejscie, open(plik_wyjsciowy, 'w', encoding='utf-8') as wyjscie:
        for linia in wejscie:
            linia = linia.rstrip().replace(cudzyslow, '')  # Usuwamy wszystkie cudzysłowy
            nowa_linia = f"{cudzyslow}{linia}{cudzyslow}{przecinek}\n"
            wyjscie.write(nowa_linia)

# Przykład użycia:
plik_wejsciowy = "plik.txt"
plik_wyjsciowy = "nowy_plik.txt"
dodaj_cudzyslowy_i_przecinki(plik_wejsciowy, plik_wyjsciowy)