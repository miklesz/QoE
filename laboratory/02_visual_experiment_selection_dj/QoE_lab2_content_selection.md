# QoE Laboratorium 2: Selekcja materiału do eksperymentu subiektywnego

**autorzy instrukcji:** dr inż. dr n. prawn. Dawid Juszka, dr hab. inż. Lucjan Janowski, prof. AGH  

## Cele zajęć

1. Nabycie umiejętności użycia narzędzi grupy `ffmpeg` na potrzeby realizacji kursu.
2. Selekcja sekwencji wideo do eksperymentu subiektywnego. Musimy pobrać, przeglądnąć sekwencje, wybrać fragmenty, dobrać odpowiednie parametry wizualne. 



**Wymagania:**  
- Zainstalowany pakiet **FFmpeg** (zawiera `ffmpeg`, `ffprobe`, `ffplay`)  
- Dostępne pliki testowe:  
  - `sample.mp4` (lub `input.mp4`)  
  - surowa sekwencja YUV, np. `foreman.yuv` 300 frames (CIF: 352x288, 4:2:0) - pobierz stąd: https://hlevkin.com/hlevkin/TestVideo/foreman.yuv

---
## 0. ROZPOCZNIJ POBIERANIE!
0.1. Wejdź na stronę: http://download.opencontent.netflix.com.s3.amazonaws.com/index.html?prefix=Netflix_test_conditions/

0.2. Pobierz kilka sekwencji z rozszerzeniem .yuv


## 1. Podstawowe informacje teoretyczne

### 1. Czym jest kodek?

**Kodek (ang. *coder-decoder*)** to algorytm kompresji i dekompresji danych audio lub wideo.  
Kodek definiuje sposób, w jaki sygnał jest przekształcany w postać binarną, tak by zminimalizować objętość danych przy zachowaniu akceptowalnej jakości.

Przykłady kodeków:
| Typ | Przykłady kodeków | Opis |
|------|--------------------|------|
| **Wideo** | H.264 / AVC, H.265 / HEVC, VP9, AV1 | Kompresja obrazu klatka po klatce i międzyklatkowa |
| **Audio** | AAC, MP3, Opus, PCM | Kompresja stratna lub bezstratna sygnału dźwiękowego |

---

### 2. Czym jest kontener?

**Kontener (format pliku)** to „opakowanie”, które przechowuje jeden lub więcej strumieni (wideo, audio, napisy) wraz z metadanymi (czas, tytuł, kodeki itp.).  
Nie definiuje on sposobu kompresji, tylko strukturę zapisu danych.

Przykłady kontenerów:
| Kontener | Rozszerzenie | Typowe kodeki |
|-----------|---------------|----------------|
| **MP4** | `.mp4` | H.264 + AAC |
| **MKV** | `.mkv` | dowolne (np. H.265 + FLAC) |
| **AVI** | `.avi` | starszy format, H.263, MPEG-4 |
| **MOV** | `.mov` | Apple QuickTime |
| **WEBM** | `.webm` | VP8/VP9 + Opus/Vorbis |

### 3. Czym jest format YUV?

**YUV** to *surowy format danych wideo* (tzw. „raw video”), zawierający jedynie wartości jasności i koloru dla każdej klatki obrazu.

Składa się z trzech składowych:
- **Y** — luminancja (jasność),
- **U i V** — chrominancja (informacja o kolorze).

Format YUV **nie zawiera żadnych nagłówków ani metadanych** — są to wyłącznie dane pikseli zapisane klatka po klatce.

Aby poprawnie odczytać taki plik, należy **ręcznie podać parametry wideo**, m.in.:
- rozdzielczość (`-video_size`),
- format próbkowania (`-pix_fmt`, np. `yuv420p`, `yuv422p`, `yuv444p`),
- liczbę klatek na sekundę (`-framerate`).

**Przykład odtwarzania surowej sekwencji YUV:**

```bash
ffplay -video_size 352x288 -pix_fmt yuv420p -framerate 30 foreman.yuv
```

---

### 4. Czym jest format Y4M (YUV4MPEG2)?

**Y4M** to rozszerzony format YUV, który zawiera **nagłówek tekstowy z metadanymi**.
Nagłówek opisuje:
- rozdzielczość,
- liczbę klatek na sekundę,
- format próbkowania kolorów,
- kolejność pól (dla sygnałów z przeplotem).

Dzięki temu formatowi Y4M programy takie jak FFmpeg, FFplay czy inne narzędzia mogą odczytać plik **bez konieczności ręcznego określania parametrów**.

**Przykład odtwarzania sekwencji Y4M:**

```bash
ffplay foreman_cif.y4m
```

---

### 5. Porównanie formatów YUV i Y4M

| Cecha | **YUV (raw)** | **Y4M (YUV4MPEG2)** |
|--------|----------------|----------------------|
| Zawiera nagłówek? |  Nie | Tak |
| Zawiera metadane (rozdzielczość, fps)? | Nie | Tak |
| Wymaga ręcznego określenia parametrów? | Tak | Nie |
| Kompatybilność z narzędziami | Wymaga opcji `-video_size`, `-pix_fmt` | Automatycznie rozpoznawany |
| Typowy rozmiar pliku | Minimalny (brak nagłówków) | Nieco większy (nagłówek tekstowy) |
| Zastosowanie | surowe dane z kamer, testy kodeków | wymiana danych między programami, analiza, kodowanie |
---

### 3. Strategie kompresji i sterowanie jakością

#### Stały bitrate (CBR — Constant Bitrate)
- Stała liczba bitów na sekundę.
- Prosty do przewidzenia rozmiar i przepływność, kosztem jakości w trudnych scenach.  
**Zastosowanie:** transmisje w czasie rzeczywistym, systemy o stałej przepustowości.

#### Zmienny bitrate (VBR — Variable Bitrate)
- Bitrate zależny od złożoności sceny.  
- Lepsza jakość przy tej samej średniej przepływności.  
**Zastosowanie:** zapisy archiwalne, dystrybucja treści offline.

#### Stały współczynnik kwantyzacji (CQP / CRF)
- Kompresja sterowana poziomem jakości, nie przepływnością.  
- Parametr **CRF** (dla H.264/H.265) określa „jakość docelową”:  
  - `CRF=18` → bardzo dobra jakość,  
  - `CRF=28` → gorsza jakość, mniejszy plik.  
**Zastosowanie:** archiwizacja materiałów, analiza wpływu strat kompresji.

#### Inne tryby:
| Tryb | Opis |
|------|------|
| **2-pass encoding** | Dwukrotne kodowanie dla precyzyjnego bitrate’u |
| **Lossless** | Kompresja bezstratna (`-qp 0` lub `-crf 0`) |
| **Constant Quality (CQ)** | Stała jakość, zmienny bitrate, używane np. w NVENC |

---

## Narzędzia pakietu FFmpeg

| Narzędzie | Funkcja |
|------------|----------|
| **ffprobe** | Analiza parametrów i metadanych plików |
| **ffplay** | Odtwarzanie materiałów, podgląd filtrów |
| **ffmpeg** | Konwersja, przetwarzanie i kompresja multimediów |

---

## Zestaw zadań laboratoryjnych do ćwiczenia obsługi narzędzi z pakietu FFmpeg

### Zadanie 1. Analiza pliku i statystyk klatek (FFprobe)

**Cel:** Poznanie struktury strumieni, metadanych i właściwości technicznych.

#### Podstawowe:
1. Wyświetl informacje o pliku:
   ```bash
   ffprobe sample.mp4
   ```
2. Uzyskaj tylko kluczowe dane w formacie JSON:
   ```bash
   ffprobe -v quiet -print_format json -show_format -show_streams sample.mp4
   ```
3. Odpowiedz:
   - Jakie są kodeki wideo i audio?
   - Jaki jest bitrate i długość filmu?

#### Zaawansowane:
1. Analiza ramek:
   ```bash
   ffprobe -select_streams v:0 -show_frames -show_entries frame=pkt_pts_time,pkt_size -of csv sample.mp4 | head -n 10
   ```
2. Oblicz średni rozmiar klatki (np. `awk '{sum+=$2} END {print sum/NR}'`).
3. Sprawdź czy bitrate jest stały, czy zmienny.

---

### Zadanie 2. Odtwarzanie sekwencji nieskompresowanej YUV (FFplay)

**Cel:** Zrozumienie sposobu prezentacji surowych danych wideo.

#### Podstawowe:
1. Odtwórz sekwencję YUV:
   ```bash
   ffplay -video_size 352x288 -pixel_format yuv420p -framerate 30 foreman.yuv
   ```
2. Zmień liczbę klatek na sekundę:
   ```bash
   ffplay -video_size 352x288 -pix_fmt yuv420p -framerate 10 foreman.yuv
   ```

#### Zaawansowane:
1. Zastosuj filtr skalujący:
   ```bash
   ffplay -video_size 352x288 -pix_fmt yuv420p -vf scale=704:576 foreman.yuv
   ```
2. Dodaj filtr wizualny (np. negatyw, jasność):
   ```bash
   ffplay -video_size 352x288 -pix_fmt yuv420p -vf "eq=contrast=1.2:brightness=0.05" foreman.yuv
   ```
3. Podgląd histogramu:
   ```bash
   ffplay -i sample.mp4 -vf "histogram"
   ```

---

### Zadanie 3. Wycinanie sekwencji (FFmpeg)

**Cel:** Nauka segmentacji materiału wideo.

#### Podstawowe:
1. Wycięcie fragmentu 5 sekund od pozycji 3 s:
   ```bash
   ffmpeg -ss 3 -t 5 -i sample.mp4 -c copy clip.mp4
   ```
2. Sprawdź długość wycinka:
   ```bash
   ffprobe -show_entries format=duration -v quiet -of csv="p=0" clip.mp4
   ```

#### Zaawansowane:
1. Wycinanie z dokładnością klatkową (rekompresja):
   ```bash
   ffmpeg -ss 3 -to 8 -i sample.mp4 -c:v libx264 -preset fast -crf 23 cut_reencoded.mp4
   ```
2. Wycinek z pliku YUV:
   ```bash
   ffmpeg -f rawvideo -video_size 352x288 -pix_fmt yuv420p -framerate 30 -i foreman.yuv -ss 1 -t 2 -c:v rawvideo output_cut.yuv
   ```
3. Usuwanie fragmentu (np. 5–10 s) i łączenie pozostałych części — poprzez listę `concat`.

---

### Zadanie 4*. Kompresja sekwencji (FFmpeg)

**Cel:** Porównanie strategii kodowania i wpływu parametrów na jakość i rozmiar.

#### 4.1. Kompresja CBR – stały bitrate
```bash
ffmpeg -i sample.mp4 -c:v libx264 -b:v 1M -minrate 1M -maxrate 1M -bufsize 2M output_cbr.mp4
```

#### 4.2. Kompresja VBR – zmienny bitrate
```bash
ffmpeg -i sample.mp4 -c:v libx264 -b:v 1M -maxrate 1.5M -bufsize 3M output_vbr.mp4
```

#### 4.3. Kompresja CRF – stały współczynnik kwantyzacji
```bash
ffmpeg -i sample.mp4 -c:v libx264 -preset slow -crf 23 output_crf.mp4
```

#### 4.4. Kompresja z ustalonym parametrem QP
```bash
ffmpeg -i sample.mp4 -c:v libx264 -qp 25 output_qp25.mp4
```

#### 4.5. (Zaawansowane) Dwupasowe kodowanie
```bash
ffmpeg -y -i sample.mp4 -c:v libx264 -b:v 1M -pass 1 -an -f null /dev/null
ffmpeg -i sample.mp4 -c:v libx264 -b:v 1M -pass 2 -c:a aac output_2pass.mp4
```

#### 4.6. (Opcjonalne) Kompresja bezstratna
```bash
ffmpeg -i sample.mp4 -c:v libx264 -crf 0 output_lossless.mp4
```

**Porównaj:**  
- rozmiary plików,  
- subiektywną jakość,  
- bitrate i parametry (użyj `ffprobe`).

---

### Zadanie 5*. Analiza wyników

1. Porównaj parametry zakodowanych plików:
   ```bash
   ffprobe -v error -show_entries stream=codec_name,bit_rate,width,height,duration -of default=noprint_wrappers=1 output_*.mp4
   ```
2. Zestaw wyniki w tabeli:
   | Tryb | Średni bitrate | Rozmiar [MB] | Ocena jakości |
   |------|----------------|---------------|----------------|
   | CBR  |                |               |                |
   | VBR  |                |               |                |
   | CRF  |                |               |                |
   | QP   |                |               |                |

---

# Instrukcje do wykonania przed następnymi zajęciami -  krok po kroku

## 1. Szukanie sekwencji

Proszę wyszukać sekwencję do wykonywania testów subiektywnych. Powinny być nieskompresowane w formacie yuv. 

Odtwarzanie można zrobić z wykorzystaniem `ffplay`

lub programu dostępnego tu: `https://github.com/IENT/YUView`

## 2. Wycinanie sekwencji

`ffmpeg -s 1920x1080 -pix_fmt yuv420p -i input.yuv -ss 00:00:10 -t 5 output.yuv`

## 3. Kompresja sekwencji

stały bitrate:

`ffmpeg -i input.yuv -c:v libx264 -b:v 2000k output_cbr.mp4`

stała przepływność:

`ffmpeg -i input.yuv -c:v libx264 -crf 23 output_crf23.mp4`

stały współczynnik kwantyzacji: 

`ffmpeg -i input.yuv -c:v libx264 -qp 30 output_qp30.mp4`

## 4. Wybranie sekwencji

Do dalszej pracy potrzebujemy wybrać do ośmiu sekwencji. To trzeba uzgodnić pomiędzy grupami. 

# Wynik

Mamy 5 sekwencji skompresowanych na 5 różnych sposobów. Wybieramy sekwencje dla dalszej pracy - to trzeba uzgodnić pomiędzy grupami.
