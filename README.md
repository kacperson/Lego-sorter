# Lego-sorter
Program klasyfikujący klocki oparty o uczenie maszynowe.

## Działanie
- Podajemy klocek przed kamerę 
- Algorytm rozpoznaje klocek 
- wypluwa dane (gdzie się znajduje i w jakiej ilości)
- podać ilość klocków z tego rodzaju do dodania
- dodaje do bazy danych i do szafeczki
- po dodaniu X kolejnych klocków algorytm uczy się od nowa
- proces się zapętla

### 1. Umieszczenia klocka
Klocek pojawiający się przed kamerą aktywuje kamerę (porównywanie obrazów w czasie rzeczywistym).
Jeżeli obraz się będzie różnić to po około sekundzie program zrobi zdjęcie i doda je do bazy danych.
Podczas usuwania klocka sprzed kamery program wykryje zmianę obrazu i odczeka 5 s.

### 2. Rozpoznawanie klocka
Algorytm CNN

### 3. Dane na temat klocka
ID klocka
Miejsce gdzie się znajduje

### 4. Dodawanie klocka
Podanie ilości dostępnych klocków

### 5. Sprawdzanie dostępności klocków
