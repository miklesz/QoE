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

Zebranie danych subiektywnych. 

# Instrukcje krok po kroku

## Korekta dla rocznika 2025/26

Proszę skompresować, jeżeli jeszcze nie są skompresowane, sekwencje źródłowe z parametrami:
* `ffmpeg -y -i sample_sparks.mp4 -vf "scale=256:144:force_original_aspect_ratio=decrease:flags=lanczos,pad=256:144:(ow-iw)/2:(oh-ih)/2,format=yuv420p" -c:v libx264 -preset slow -b:v 200k -maxrate 200k -bufsize 400k out_sampleSparks_256x144_200k.mp4`
* `ffmpeg -y -i out_sampleSparks_256x144_200k.mp4 -vf "scale=1280:720:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -qp 10 -pix_fmt yuv420p test_sampleSparks_256x144_200k_to_720p.mp4`

W teście zostanie użyty plik `test_sampleSparks_256x144_200k_to_720p.mp4`

Podany przykład to najniższa jakość. Musimy jeszcze dodać wyższe jakości:
* `ffmpeg -y -i sample_sparks.mp4 -vf "scale=480:270:force_original_aspect_ratio=decrease:flags=lanczos,pad=480:270:(ow-iw)/2:(oh-ih)/2,format=yuv420p" -c:v libx264 -preset slow -b:v 400k -maxrate 400k -bufsize 800k out_sampleSparks_480x270_400k.mp4`
* `ffmpeg -y -i out_sampleSparks_480x270_400k.mp4 -vf "scale=1280:720:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -qp 10 -pix_fmt yuv420p test_sampleSparks_480x270_400k_to_720p.mp4`

* `ffmpeg -y -i sample_sparks.mp4 -vf "scale=640:360:force_original_aspect_ratio=decrease:flags=lanczos,pad=640:360:(ow-iw)/2:(oh-ih)/2,format=yuv420p" -c:v libx264 -preset slow -b:v 1000k -maxrate 1000k -bufsize 2000k out_sampleSparks_640x360_1000k.mp4`
* `ffmpeg -y -i out_sampleSparks_640x360_1000k.mp4 -vf "scale=1280:720:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -qp 10 -pix_fmt yuv420p test_sampleSparks_640x360_1000k_to_720p.mp4`

* `ffmpeg -y -i sample_sparks.mp4 -vf "scale=960:540:force_original_aspect_ratio=decrease:flags=lanczos,pad=960:540:(ow-iw)/2:(oh-ih)/2,format=yuv420p" -c:v libx264 -preset slow -b:v 1400k -maxrate 1400k -bufsize 2800k out_sampleSparks_960x540_1400k.mp4`
* `ffmpeg -y -i out_sampleSparks_960x540_1400k.mp4 -vf "scale=1280:720:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -qp 10 -pix_fmt yuv420p test_sampleSparks_960x540_1400k_to_720p.mp4`

* `ffmpeg -y -i sample_sparks.mp4 -vf "scale=1280:720:force_original_aspect_ratio=decrease:flags=lanczos,pad=1280:720:(ow-iw)/2:(oh-ih)/2,format=yuv420p" -c:v libx264 -preset slow -b:v 2000k -maxrate 2000k -bufsize 4000k out_sampleSparks_1280x720_2000k.mp4`
* `ffmpeg -y -i out_sampleSparks_1280x720_2000k.mp4 -vf "scale=1280:720:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -qp 10 -pix_fmt yuv420p test_sampleSparks_1280x720_2000k_to_720p.mp4`

Ta komenda pokazuje czemu zmieniamy rozdzielczość przy bardzo niskim bitracie:
* `ffmpeg -y -i sample_sparks.mp4 -vf "scale=1280:720:force_original_aspect_ratio=decrease:flags=lanczos,pad=1280:720:(ow-iw)/2:(oh-ih)/2,format=yuv420p" -c:v libx264 -preset slow -b:v 400k -maxrate 400k -bufsize 800k out_sampleSparks_1280x720_400k.mp4`
* `ffmpeg -y -i out_sampleSparks_1280x720_400k.mp4 -vf "scale=1280:720:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -qp 10 -pix_fmt yuv420p test_sampleSparks_1280x720_400k_to_720p.mp4`


## Uruchomienie eksperymentu

Proszę uruchomić oprogramowanie do eksperymentu, zgodnie z procedurą przygotowaną w zeszłym tygodniu. 

## Wykonanie testu

Każda osoba powinna przeprowadzić test dla każdej z grup. 

## Integracja wyników 

Proszę wszystkie wyniki zebrać w jeden plik danych, gdzie poza kolumnami z pliku zapisanego przez oprogramowanie do testów mamy kolumny:
`grup_name; E; h; bitrate; resolution; SRC; size`
gdzie:
* `grup_name` to unikalna nazwa jaką sobie nadaje dana grupa
* `E` oraz `h` to wynik uzyskany dla SRC
* `bitrate` oraz `resolution` to parametry kompresji
* `SRC` to nazwa sekwencji źródłowej, tej którą kompresowaliśmy.
* `size` to rozmiar pliku po kompresji

Proszę też zadbać, żeby każda osoba miała unikalne ID takie samo w całym pliku. 

# Wynik

Mamy plik z danymi, jeden na całą grupę w którym wiemy jakie ID ma każdy z was. Dla każdej sekwencji mamy tyle odpowiedzi ile osób w laboratorium. Znamy zarówno dane kompresji jak i dane sekwencji źródłowej (SRC).