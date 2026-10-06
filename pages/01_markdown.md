# Markdown, Colab oraz GitHub

Na poączątek poznamy trzy narzędzia, które rozwiązują trzy różne problemy:

| Narzędzie | Do czego służy? |
| --- | --- |
| **Markdown** | do prostego zapisywania uporządkowanego tekstu, dokumentacji i raportów |
| **Google Colab** | do łączenia tekstu, kodu, obliczeń i wyników w jednym notebooku |
| **GitHub** | do przechowywania projektu, śledzenia zmian i współpracy |

Te trzy elementy bardzo dobrze ze sobą współpracują. Podstawą wszędzie jest przygotowanie opisu w kodzie Markdown. Do tego dochodzić będą obliczenia w Colabie, a następnie przechowanie źródła i wyniki w repozytorium GitHub.

---

# Markdown

## Co to jest Markdown?

**Markdown** to prosty język znaczników służący do formatowania zwykłego tekstu.

Najczęściej zapisujemy go w plikach z rozszerzeniem:

~~~text
.md
~~~

Przykłady:

~~~text
README.md
raport.md
notatki.md
~~~

Plik Markdown jest zwykłym plikiem tekstowym. Można go otworzyć praktycznie w każdym edytorze. Specjalne znaki, takie jak `#`, `*`, `-` czy `$`, informują program wyświetlający dokument, jak ma wyglądać tekst.

# Dlaczego Markdown jest tak istotny?

Za każdym razem rozmawiając z chatem AI tak naprawdę rozmawiamy z plikiem Markdown. AI potrafi interpretować składnię Markdown i generować raporty w tym formacie.

Dlatego też jak skopiujesz output to ma on całą masę znaczników (np. `#`, `*`, `-`, czy `$`), które są potrzebne do poprawnego renderowania.

Github (archiwum programistyczne) zawiera opisy również w Markdown. Podobnie Google Colab (środkowisko programistyczne pythona) potrafią renderować Markdown. Dzięki temu możemy przygotować raport, który będzie wyglądał dobrze zarówno w przeglądarce, jak i w notebooku.

Warto od razu rozróżnić dwie rzeczy:

- **źródło Markdown** — tekst, który wpisujemy do pliku,
- **wyrenderowany dokument** — wygląd tego tekstu po interpretacji składni Markdown.

Na GitHubie możemy przełączać się między widokiem źródła i wyrenderowanym dokumentem.

Podobnie edytory kodu jak VS Code, PyCharm czy Jupyter Notebook potrafią renderować Markdown w osobnym oknie podglądu.

## Zanim zaczniemy pisać w Markdown zobacz przykładowy plik Markdown

Raport na temat ciała na sprężynie: 

- [„Ciało na sprężynie”](examples/01_markdown/raport_cialo_na_sprezynie.md).

## Nagłówki

Nagłówki budują strukturę dokumentu. Im więcej znaków `#`, tym niższy poziom nagłówka.

Źródło:

~~~markdown
# Tytuł dokumentu

## Główna sekcja

### Podsekcja
~~~

Efekt:

> # Tytuł dokumentu
>
> ## Główna sekcja
>
> ### Podsekcja

W praktyce jeden dokument powinien mieć jeden główny nagłówek `#`.

Dalsze części dokumentu organizujemy za pomocą `##`, `###` itd.

---

## Pogrubienie, kursywa i przekreślenie

Źródło:

~~~markdown
**tekst pogrubiony**

*tekst pochylony*

~~tekst przekreślony~~

***tekst pogrubiony i pochylony***
~~~

Efekt:

**tekst pogrubiony**

*tekst pochylony*

~~tekst przekreślony~~

***tekst pogrubiony i pochylony***

Wyróżnień warto używać oszczędnie. Jeśli wszystko jest pogrubione, nic nie jest naprawdę wyróżnione.

---

## Akapit i nowa linia

Nowy akapit tworzymy przez pozostawienie pustej linii.

Źródło:

~~~markdown
To jest pierwszy akapit.

To jest drugi akapit.
~~~

Efekt:

To jest pierwszy akapit.

To jest drugi akapit.

To ważna zasada: w Markdown pojedyncze naciśnięcie Enter nie zawsze oznacza nowy akapit.

---

## Listy punktowane

Źródło:

~~~markdown
- Markdown
- Colab
- GitHub
~~~

Efekt:

- Markdown
- Colab
- GitHub

Listy można zagnieżdżać:

~~~markdown
- GitHub
  - repozytorium
  - Issues
  - historia zmian
- Colab
  - tekst
  - kod
  - wyniki
~~~

Efekt:

- GitHub
  - repozytorium
  - Issues
  - historia zmian
- Colab
  - tekst
  - kod
  - wyniki

---

## Listy numerowane

Źródło:

~~~markdown
1. przygotuj dane,
2. wykonaj obliczenia,
3. zapisz wynik,
4. opisz wynik.
~~~

Efekt:

1. przygotuj dane,
2. wykonaj obliczenia,
3. zapisz wynik,
4. opisz wynik.

Listy numerowane są szczególnie przydatne przy opisie procedury lub instrukcji.

---

## Checklisty

GitHub obsługuje listy zadań.

Źródło:

~~~markdown
- [x] utworzono notebook
- [x] wykonano obliczenia
- [ ] sprawdzono wynik
~~~

Efekt:

- [x] utworzono notebook
- [x] wykonano obliczenia
- [ ] sprawdzono wynik

Checklisty bardzo dobrze nadają się do krótkich list kontrolnych w dokumentacji i GitHub Issues.

---

## Linki

Źródło:

~~~markdown
[GitHub](https://github.com/)
~~~

Efekt:

[GitHub](https://github.com/)

Zamiast wklejać długi adres do strony, warto umieścić go pod czytelną nazwą.

---

## Obrazy

Obraz osadzamy podobnie jak link, ale na początku dodajemy znak `!`.

Źródło:

~~~markdown
![Wykres zależności y od x](wykres.png)
~~~

Jeżeli plik `wykres.png` znajduje się w tym samym folderze co dokument Markdown, GitHub wyświetli obraz w miejscu tej instrukcji.

Jeżeli plik znajduje się w podfolderze `files`, używamy ścieżki:

~~~markdown
![Wykres zależności y od x](files/wykres.png)
~~~

Efekt:
![Wykres zależności y od x](files/wykres.png)

Tekst w nawiasach kwadratowych jest opisem obrazu. Warto go uzupełniać — pomaga zrozumieć zawartość także wtedy, gdy obraz nie może zostać wyświetlony.

W projektach przechowywanych w repozytorium zwykle wygodniej używać **ścieżek względnych** niż pełnych adresów internetowych.

---

## Tabele

Źródło:

~~~markdown
| Narzędzie | Typ pliku | Zastosowanie |
| --- | --- | --- |
| Markdown | .md | dokumentacja |
| Colab | .ipynb | obliczenia |
| GitHub | repozytorium | historia projektu |
~~~

Efekt:

| Narzędzie | Typ pliku | Zastosowanie |
| --- | --- | --- |
| Markdown | `.md` | dokumentacja |
| Colab | `.ipynb` | obliczenia |
| GitHub | repozytorium | historia projektu |

Tabele są dobre do krótkich zestawień. Jeśli w komórkach pojawiają się długie akapity tekstu, zwykle lepiej wrócić do zwykłych sekcji i list.

---

## Kod w tekście

Nazwy plików, komendy i bardzo krótkie fragmenty kodu warto oznaczać pojedynczym backtickiem.

Źródło:

~~~markdown
Uruchom plik `analiza.py` i sprawdź wartość zmiennej `wynik`.
~~~

Efekt:

Uruchom plik `analiza.py` i sprawdź wartość zmiennej `wynik`.

---

## Bloki kodu

Większy fragment kodu umieszczamy w osobnym bloku.

Źródło:

~~~~markdown
```python
x = 5
y = x**2
print(y)
```
~~~~

Podanie nazwy języka, np. `python`, `bash`, `html` czy `json`, pozwala GitHubowi kolorować składnię.

W raporcie technicznym dobrze jest pokazać krótki fragment kodu, który jest istotny dla opisywanego wyniku. Nie trzeba kopiować do raportu całego programu.

---

## Cytaty

Źródło:

~~~markdown
> Wynik należy zawsze sprawdzić przed jego wykorzystaniem.
~~~

Efekt:

> Wynik należy zawsze sprawdzić przed jego wykorzystaniem.

Cytaty można wykorzystać także do krótkiego wyróżnienia komentarza lub uwagi.

---

## Matematyka

GitHub potrafi renderować wzory matematyczne.

Krótki wzór umieszczamy wewnątrz pojedynczych znaków dolara.

Źródło:

~~~markdown
Energia spoczynkowa dana jest wzorem $E=mc^2$.
~~~

Efekt:

Energia spoczynkowa dana jest wzorem $E=mc^2$.

Dłuższy wzór umieszczamy w osobnym bloku.

Źródło:

~~~markdown
$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$
~~~

Efekt:

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

Macierze zapisujemy wielowierszowo:

~~~markdown
$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}
$$
~~~

Efekt:

$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}
$$

---

## Zrzut ekranu i transkrypcja do Markdown

Czasem informacja istnieje tylko jako obraz: zrzut ekranu programu, zdjęcie tabeli, komunikat błędu albo fragment zeskanowanego dokumentu. AI może pomóc przepisać zawartość obrazu do tekstu. Taki proces nazywamy tutaj **transkrypcją**.

Przykładowy workflow:

1. zachowujemy oryginalny obraz,
2. prosimy AI o **przepisanie jego zawartości do kodu markdown**
3. zapisujemy wynik w pliku tekstowym lub Markdown,
4. porównujemy transkrypcję z obrazem,
5. poprawiamy ewentualne błędy.

Największej ostrożności wymagają:

- liczby,
- wzory,
- nazwy plików,
- adresy,
- fragmenty kodu,
- komunikaty błędów.

Transkrypcja wygenerowana przez AI jest **wersją roboczą**, dopóki człowiek jej nie sprawdzi.

---

## Poprawne formatowanie matematyki w Markdown

W materiałach tego kursu polecamy stosowanieprostego zestawu reguł formatowania matematyki przygotowanego specjalnie tak, aby pliki dobrze renderowały się na GitHubie: 

* [hints.md](hints.md)

Pracując z chatem AI i domagając się kodu markdowna, warto załaączać ten plik jako kontekst, aby AI od razu generowało poprawny kod w Markdown.

Różne systemy: przeglądarkowe chaty AI, Edytor Visual Studio,, Colab i GitHub, mogą różnie renderować wzory matematyczne!

Częstym błędem jest używanie w kodzie Markdown znaków `\[]` i `\]` zamiast `$ $` do oznaczania wzorów matematycznych. Wtedy GitHub nie renderuje wzoru, a Colab renderuje go poprawnie.

---

## Dobre materiały o Markdown

- [GitHub Docs — Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [GitHub Docs — Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
- [Markdown Guide — Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Markdown Guide — Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
