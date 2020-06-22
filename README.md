# glosowa_lacznosc
Projekt z głosowej łaczniości z komputerem
======
**Inżynieria Biomedyczna, specjalność: Informatyka i Elektronika Medyczna**
**Projekt: Głosowa łączność z komputerem**

Zespół III:
Cieśla Agnieszka,
Czuchra Jakub,
Gałaszewicz Natalia,
Mędrala Radosław,
Mikos Weronika,
Nazimek Michał,
Typer Wiktoria,
Szymczyk Adrianna,
Winiarski Szymon

======

Opis
Projekt miał na celu stworzenie programu rozpoznającego komendy mówione przez człowieka. Wybrano komendy, które mogłyby zostać użyte do zarządzania i sterowania np. inteligentnym domem:
otwórz
okno
drzwi
garaż
zamknij

Pliki źródłowe projektu są zamieszczone w repozytorium https://github.com/szymwin/glosowa_lacznosc

1. Pierwszy podejście do rozwiązania problemu:
plik projektu: JUP_PROJECT.ipynb 
Problem rozwiązano bazując na widocznym w pliku algorytmie rozpoznawania mowy. Zaimportowano odpowiednie pliki audio w których obecne są wypowiadane przez różne osoby komendy. Każdemu ze słów przyporządkowano osobny numer identyfikujący. Próbki poddano algorytmowi uczenia maszynowego (https://medium.com/@ageitgey/machine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a). Rezultaty tej metody nie były jednak wystarczające zadowalające ze względu na zbyt mały zbiór danych.

2. Drugie podejście do rozwiązania problemu:
plik projektu: SpecRec.ipynb
W drugim podejściu do rozwiązania problemu bazowane na artykule
https://towardsdatascience.com/how-to-apply-machine-learning-and-deep-learning-methods-to-audio-analysis-615e286fcbbc
Wszystkie dane zebrane są na frameworku comet individual (link:
https://www.comet.ml/typerw/specrec/19a8cb8c0d694930a6ba5f9f587db1f9?experiment-tab=chart&showOutliers=true&smoothing=0&view=Default%20view&xAxis=step ) tu umieszczane są wszystkie nagrania, wykresy zebrane w trakcie trenowania modelu.
Storzono model potrafiący rozpoznawac komendy. Pliki zostały najpierw przeprocesowane w bibliotece librosa (oryginalne wyniki można zaobserwowawać na wykresie audio pomarańczowym (plik original_audio.png), natomiast przeprocesowane znajdują się na niebieskim wykresie (plik librosa_audio.png). W trakcie przeprocesowania plików został zmniejszony bit rate, usunięty efekt stereo oraz pliki zostały poddane próbkowaniu z częstotliwością 40 punktów na plik. Następne przygotowano dane do modelu zmieniając dane tekstowe na dane numeryczne. W tym podejściu wykorzystywane były poprawne wyniki z pierwszego podejścia do wykonania projektu. Kolejnym krokiem było dokonanie preprocessingu w bibliotece Python’a do uczenia maszynowego - sklearn. Pliki podzielono na zbiór treningowy oraz testowy, a następnie przystąpiono do trenowania modelu na 100 epokac
h w wyniku czego otrzymano następujące precyzje:
Pre-training Accuracy - 25%
Training Accuracy: 87.50%
Testing Accuracy: 81.25%

Jeśli chcemy sprawdzić plik to go dodajemy w “file to check” jak na screen1.png.
Jak można zauważyć, skuteczność rozpoznawania mowy wzrosła wraz z uczeniem. Podane wyniki można także zaobserwować na załączonych plikach screen1.png i screen2.png: gdzie skuteczność rozpoznawania mowy przez komputer wynosi aż 99% co niewątpliwie wskazuje na poprawność działania programu.  
Podczas projektu zostały wykorzystane następujące technologie:

- jupiter notebook - oba podejścia
- framework comet - drugie podejście
- biblioteki: tensorflow, sklearn
