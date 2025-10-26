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

Przygotowanie pełnego eksperymentu, który może zostać przeprowadzony na kolejnych zajęciach.  

# Instrukcje krok po kroku

## Wybranie sekwencji

Proszę pobrać filmy możliwie lekkie ze strony opencontent.netflix.com Proponuję Chimera. Należy przekształcić nagranie na format YUV, jeżeli nie jest w tym formacie i podzielić na 5 sekundowe sekwencje.  

Dla każdego filmu chcemy policzyć współczynnik SI/TI oraz E i h. Dla różnych filmów ten sam sposób kompresji, dla przykładu stały bitrate, powoduje różną wizualną jakość. W teście powinniśmy mieć sekwencje zarówno łatwe jak i trudne w kompresji. Tradycyjnie badane jest to z wykorzystaniem współczynnika SI/TI spatial/temporal information. Te parametry można policzyć z wykorzystaniem pakietu ffmpeg.

Nowsze i lepsze metryki lepiej oddają skomplikowanie sekwencji. Takie metryki to między innymi VCA (Video Complexity Analyzer) dostępny tu: https://github.com/cd-athena/VCA

Proszę dla otrzymanych filmów policzyć zarówno wartości SI/TI jak i E i h. Pozwoli to na wybranie różnorodnych sekwencji.

## Wybranie oprogramowania do testu

Proszę wyszukać jakieś oprogramowanie do przeprowadzania testów subiektywnych. Proponuję skorzystać ze strony: https://vqeg.github.io/software-tools/tools/#subjective-test-software Musimy być wstanie odtwarzać sekwencje z dysku i pozwalać po odtworzeniu udzielić odpowiedzi. Ważne, żeby przeanalizować ograniczenia danego oprogramowania. 

## Kompresja sekwencji

Proszę przypomnieć sobie teorię i kod z poprzednich zajęć. My skupimy się na kompresji z określonym crf

`ffmpeg -i input.yuv -c:v libx264 -crf 23 output_crf23.mp4`

Musimy zmieniać rozdzielczość. Sekwencje skompresowane bardzo silnie dla wysokiej rozdzielczości np. 0.25 Mbit/s dla rozdzielczości 4k, nie będą dobrze działać. Ich jakość, jeżeli zaczniemy od zmniejszenia rozdzielczości, kompresji, a następnie przywrócimy oryginalną rozdzielczość, otrzymana jakość będzie lepsza. Tu komenda do zmiany rozdzielczości z kompresją:

`ffmpeg -s:v 1920x1080 -r 30 -pix_fmt yuv420p -f rawvideo -i input_1920x1080.yuv -vf "scale=1280:720:flags=lanczos" -c:v libx264 -crf 22 -preset slow -pix_fmt yuv420p output_1280x720_h264_crf22.mp4`

Dla niektórych programów do prowadzenia testów musimy rozkodować sekwencję przed ich wyświetleniem testerowi. Tu przykład takiej dekompresji wraz ze zmianą rozdzielczości:

`ffmpeg -i input_compressed.mp4 -vf "scale=2560:1440:flags=lanczos" -pix_fmt yuv420p -vsync 0 -f rawvideo output_2560x1440.yuv`

## Wybranie parametrów kompresji

Tym razem musimy już dobrać dokładnie parametry kompresji. Tu wybieramy jedną z czterech wersji:

1. Eksperyment zbalansowany - pokazujemy zarówno dobre jak i złe sekwencje. 
2. Eksperyment wysokiej jakości - najgorsza sekwencja to sekwencja o jakości średniej.
3. Eksperyment niskiej jakości - poza sekwencjami źródłowymi, max to średnia jakość.
4. Eksperyment o stałych przepustowościach, bez względu na materiał źródłowy.

Każdy eksperyment powinno się dać wykonać w 20 minut, żeby na laboratorium za tydzień wykonać każdy z eksperymentów. Koniecznie eksperymenty muszą dzielić sekwencje źródłowe.

# Wynik

Mamy działający eksperyment. Skompresowane sekwencje i mamy oprogramowanie do wykonania testu. Jesteśmy gotowi do przeprowadzenia eksperymentu.