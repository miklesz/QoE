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

Celem zajęć jest wybranie sekwencji wideo do testu subiektywnego. Musimy ściągnąć, przeglądnąć sekwencje, wybrać fragmenty, dobrać odpowiednie parametry wizualne. 

# Instrukcje krok po kroku

## Szukanie sekwencji

Proszę wyszukać sekwencję do wykonywania testów subiektywnych. Powinny być nie skompresowane w formacie yuv. 

Odtwarzanie można zrobić z wykorzystaniem 

`ffplay -f rawvideo -pixel_format yuv420p -video_size 1920x1080 input.yuv`

lub programu dostępnego tu: `https://github.com/IENT/YUView`

## Wycinanie sekwencji

`ffmpeg -s 1920x1080 -pix_fmt yuv420p -i input.yuv -ss 00:00:10 -t 5 output.yuv`

## Kompresja sekwencji

stały bitrate:

`ffmpeg -i input.yuv -c:v libx264 -b:v 2000k output_cbr.mp4`

stała przepływność:

`ffmpeg -i input.yuv -c:v libx264 -crf 23 output_crf23.mp4`

stały współczynnik kwantyzacji: 

`ffmpeg -i input.yuv -c:v libx264 -qp 30 output_qp30.mp4`

## Wybranie sekwencji

Do dalszej pracy potrzebujemy wybrać do ośmiu sekwencji. To trzeba uzgodnić pomiędzy grupami. 

# Wynik

Mamy 5 sekwencji skompresowanych na 5 różnych sposobów. Wybieramy sekwencje dla dalszej pracy - to trzeba uzgodnić pomiędzy grupami. 