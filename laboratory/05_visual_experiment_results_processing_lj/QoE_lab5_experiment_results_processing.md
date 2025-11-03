---
title: "Wybranie sekwencji"
author: "Lucjan Janowski"
date: 2025
format:
  html:
    theme: cosmo
    toc: true
  pdf:
    documentclass: article
    number-sections: true
  docx: default
---

# Cel zajęć

Opracowanie wyników testów przeprowadzonych na poprzednich zajęciach.

# Instrukcje krok po kroku

## Wczytanie danych

Proszę zebrać dane z eksperymentów wszystkich grup. Celem jest integracja wszystkich wyników. Powinniśmy otrzymać plik w którym may co najmniej kolumny: Eksperyment/grupa; tester; film; ocena. Bardzo istotne jest, żeby zarówno nazwy filmów jak i numery testerów były jednoznaczne i spójne. To znaczy, jeżeli jedna osoba wykonała trzy eksperymenty, w każdym z eksperymentów powinna mieć ten sam numer. Jeżeli wykorzystaliśmy ten sam film źródłowy, ale wycięte klatki nie są zgodne co do jednej, to należy przypisać im różne nazwy, jak są zgodne co do klatki, to nazwy powinny być te same. 

Na koniec mamy dane w postaci kolumn i wierszy, gdzie kolumny to zmienne lub kilka zmiennych razem, a wiersze to pomiary. Najważniejsze w tym punkcie to świadomość, że mamy jednoznaczność, czyli, że tester id 5 w każdym wierszu w którym występuje to ta sama osoba. To samo dla każdej inne zmiennej. Z drugiej strony, osoba, która raz ma przypisane ID = 5, jest zawsze opisana przez ID = 5.

## Dodanie wszystkich zmiennych

Dane wczytane w poprzednim kroku mogą mieć pewne kolumny w których jest więcej niż jedna zmienna. Najczęściej w postaci nazwy pliku. Proszę użyć narzędzi wyrażeń regularnych, żeby rozdzielić wszystkie zmienne na osobne kolumny. 

Na koniec mamy wszystkie interesujące nas zmienne. 

## Analiza korelacji

Dla każdego testera obliczamy wartość korelacji jego odpowiedzi, ze średnią wszystkich innych odpowiedzi. Należy przeanalizować otrzymany wynik i ew. usunąć testerów, których oceniamy jako nierzetelni. Pamiętajmy, że próg 0.75, jest ok dla klasycznych testów i 160 odpowiedzi. Niższa korelacja dla krótszych testów jest naturalnym zjawiskiem wynikającym z czystej losowości.

## Analiza pytania badawczego 

Na koniec powinniśmy otrzymać wnioski co do pytania badawczego. W zależności od tego co badamy, możemy podać wpływ h i E na jakość, wpływ bitratu na jakość lub podobne.
