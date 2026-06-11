def oblicz_bmi(waga: float, wzrost_cm: float) -> float:
    """Oblicza wskaźnik BMI."""
    wzrost_m = wzrost_cm / 100
    return waga / (wzrost_m ** 2)


def ocen_bmi(bmi: float) -> str:
    """Zwraca słowną interpretację wskaźnika BMI."""
    if bmi < 18.5:
        return "Niedowaga"
    elif bmi < 25:
        return "Waga prawidłowa"
    elif bmi < 30:
        return "Nadwaga"
    else:
        return "Otyłość"


def oblicz_bmr(waga: float, wzrost_cm: float, wiek: int, plec: str) -> float:
    """Oblicza BMR (Basal Metabolic Rate) ze wzoru Mifflina-St Jeora."""
    if plec.upper() == 'M':
        return (10 * waga) + (6.25 * wzrost_cm) - (5 * wiek) + 5
    else:
        return (10 * waga) + (6.25 * wzrost_cm) - (5 * wiek) - 161


def oblicz_tdee(bmr: float, aktywnosc: int) -> float:
    """Oblicza TDEE (Całkowitą Przemianę Materii) na podstawie mnożników aktywności."""
    # 1: Siedzący, 2: Lekka (1-2x w tyg), 3: Umiarkowana (3-4x w tyg), 4: Wysoka
    mnozniki = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725}
    return bmr * mnozniki.get(aktywnosc, 1.2)


def oblicz_makro(tdee: float, waga: float):
    """Szacuje rozkład makroskładników z naciskiem na wysoką podaż białka (~2g/kg)."""
    bialko = waga * 2.05
    kalorie_bialko = bialko * 4
    tluszcze = (tdee * 0.25) / 9
    kalorie_tluszcze = tluszcze * 9
    weglowodany = (tdee - kalorie_bialko - kalorie_tluszcze) / 4
    return bialko, tluszcze, weglowodany


def oblicz_1rm(ciezar: float, powtorzenia: int) -> float:
    """Szacuje ciężar na jedno powtórzenie maksymalne (1RM) wzorem Epleya."""
    if powtorzenia == 1: return ciezar
    return ciezar * (1 + powtorzenia / 30)


def wyswietl_menu():
    print("\n" + "=" * 40)
    print("   ZAAWANSOWANY KALKULATOR TRENINGOWY")
    print("=" * 40)
    print("1. Analiza sylwetki (BMI, BMR, TDEE i Makro)")
    print("2. Kalkulator siłowy (Szacowanie 1RM)")
    print("3. Wyjście z programu")
    print("=" * 40)


def main():
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję (1-3): ").strip()

        if wybor == '1':
            try:
                print("\n--- ANALIZA SYLWETKI ---")
                waga = float(input("Podaj wagę [kg]: ").replace(',', '.'))
                wzrost = float(input("Podaj wzrost [cm]: ").replace(',', '.'))
                wiek = int(input("Podaj wiek [lata]: "))
                plec = input("Podaj płeć [M/K]: ").strip().upper()

                if plec not in ['M', 'K']:
                    print("Błąd: Płeć musi być oznaczona literą M lub K.")
                    continue

                print("Oceń aktywność fizyczną w tygodniu:")
                print("1 - Brak (praca siedząca)")
                print("2 - Lekka (trening 1-2x w tyg)")
                print("3 - Umiarkowana (trening 3-4x w tyg, np. siłownia, siatkówka)")
                print("4 - Wysoka (trening 5+ razy w tyg)")
                aktywnosc = int(input("Wybór (1-4): "))

                bmi = oblicz_bmi(waga, wzrost)
                bmr = oblicz_bmr(waga, wzrost, wiek, plec)
                tdee = oblicz_tdee(bmr, aktywnosc)
                bialko, tluszcze, wegle = oblicz_makro(tdee, waga)

                print("\n--- TWOJE WYNIKI ---")
                print(f"BMI: {bmi:.2f} ({ocen_bmi(bmi)})")
                print(f"BMR (Spoczynkowa przemiana materii): {bmr:.0f} kcal")
                print(f"TDEE (Całkowite zapotrzebowanie): {tdee:.0f} kcal")
                print(f"Sugerowane makro: {bialko:.0f}g Białka | {tluszcze:.0f}g Tłuszczy | {wegle:.0f}g Węglowodanów")

            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane! Używaj cyfr.")

        elif wybor == '2':
            try:
                print("\n--- KALKULATOR SIŁOWY (1RM) ---")
                ciezar = float(input("Podaj obciążenie [kg]: ").replace(',', '.'))
                powtorzenia = int(input("Podaj liczbę wykonanych powtórzeń: "))

                if powtorzenia <= 0 or ciezar <= 0:
                    print("Błąd: Wartości muszą być większe od zera!")
                    continue

                maks = oblicz_1rm(ciezar, powtorzenia)
                print(f"\nTwój szacunkowy ciężar maksymalny na 1 powtórzenie to: {maks:.1f} kg")
            except ValueError:
                print("Błąd: Wprowadzono nieprawidłowe dane!")

        elif wybor == '3':
            print("Zamykanie programu. Udanych treningów!")
            break
        else:
            print("Nieprawidłowy wybór. Wpisz 1, 2 lub 3.")


if __name__ == "__main__":
    main()