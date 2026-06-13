# Projekt Zaliczeniowy - Narzędzia i Pracownia

Repozytorium zaliczeniowe zawierające aplikację konsolową napisaną w języku Python oraz pliki z zajęć zrealizowane w trakcie semestru. 

## Dane Autora
* **Imię i Nazwisko:** [Szymon Kulesza]
* **Numer indeksu:** [13179]
* **Kierunek:** Informatyka Stosowana

---

## Opis Repozytorium

Struktura projektu prezentuje się następująco:
* `kalkulator_treningowy.py` – główny kod źródłowy autorskiej aplikacji. Skrypt podzielony jest na funkcje i wykorzystuje mechanizmy obsługi wyjątków.
* `/pliki_z_zajec/` – katalog zawierający notatki tekstowe z zajęć teoretycznych:
  * *Narzędzia - Wykład 5.txt* (Tematyka testowania oprogramowania, klasyfikacja testów).
  * *Narzędzia - Wykład 6.txt* (Narzędzia developerskie, Git, GitHub).

---

## Instrukcja i Opis Aplikacji

**Zaawansowany Kalkulator Treningowy** to program wspierający planowanie diety i treningów. Aplikacja opiera się na popularnych, udowodnionych naukowo wzorach matematycznych. 

### Funkcjonalności:
1. **Analiza Sylwetki (Moduł 1):** * Liczy BMI (Body Mass Index) oraz klasyfikuje wynik.
   * Szacuje BMR na podstawie wzoru Mifflina-St Jeora.
   * Liczy TDEE z uwzględnieniem poziomu aktywności.
   * Sugeruje rozkład makroskładników (celując w ok. 2.05g białka na kg masy ciała dla osób celujących w rekompozycję sylwetki).
2. **Kalkulator Siłowy (Moduł 2):** * Wylicza szacunkowe jedno powtórzenie maksymalne (1RM) ze wzoru Epleya na podstawie podanego ciężaru roboczego i ilości wykonanych powtórzeń.

### Wymagania techniczne
* Środowisko: **Python 3.6+**
* Biblioteki: Wyłącznie moduły wbudowane w standardową bibliotekę języka.

### Uruchomienie krok po kroku

1. Sklonuj repozytorium na dysk lokalny poleceniem:
   `git clone <link-do-repozytorium>`
   *(Ewentualnie pobierz jako plik ZIP i rozpakuj).*
2. Uruchom wiersz poleceń i przejdź do katalogu głównego projektu.
3. Wywołaj plik poleceniem:

```bash
python kalkulator_treningowy.py
