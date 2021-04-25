# ################################## HW4 ################################## #
"""
Pokyny:
- Deadline odevzdani: 1. 12. 23:59
- Odevzdejte jediny soubor
- Muzete si vytvaret pomocne funkce, pokud chcete.
    - V teto uloze to je doporuceno
- V pripade, ze chcete vytvaret vlastni testy, vkladete je na prislusne misto
    na konci souboru.
    - Pred odevzdanim vlastni modifikace smazte.
- Piste srozumitelny kod, pouzivejte vhodne nazvy promennych a funkci.
- Dodrzujte standard pep8.
    - Budu kontrolovat a strhavat body za jeho nedodrzeni.
- Nemente hlavicky pripravenych funkci.
- Pripadne nejasnosti muzete resit v diskuznim foru. Pokud by ale mela otazka
    obsahovat kusy kodu, nebo neco, co by mohli ostatni studenti opsat, tak
    napiste radeji email.
- Pokud nevite, jak nejaky priklad vyresit kompletne, napiste do komentare,
    co vasemu reseni chybi.
- Neopisujte. Nestoji to za to. Dostanete zaporne body a budete muset ulohu
    stejne vypracovat sami.

Zadani:
Vytvorte program hrajici hru "Padajici piskvorky" uzivatele proti pocitaci
(na planu zadane velikosti). Tato variace piskvorek se hraje na dvourozmernem
hracim planu. Hra je podobna klasickym piskvorkam s tim rozdilem, ze pokud
jste na tahu, nevolite konkretni ctverecek, do ktereho byste umistili svuj
symbol, ale sloupec. Symbol v danem sloupci spadne dolu (nejvice, co to jde).
Vyhrava ten, kdo posklada 4 sve symboly v rade, sloupci nebo diagonale.

Zadani:
Vasim ukolem je implementovat:
1) Funkci show_state(state), ktera vypise dany plan na standardni vystup.
Plan je reprezentovan seznamem seznamu stejne delky, ktere obsahuji znaky
X (krizek), O (kolecko) nebo mezera pro neobsazene pole.
>> state = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'O'],
         [' ', ' ', ' ', ' ', 'X'], [' ', 'O', ' ', ' ', 'X']]
>> show_state(state)

        O
        X
  O     X
- - - - -
0 1 2 3 4

2) Funkci strategy(state, symbol), ktera pro dany plan a symbol vrati pozici
(sloupec) tahu pocitace. Neni nutne aby byla nejak sofistikovana, muze
vracet nahodny sloupec v danem rozsahu.

>> state = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'X', ' ']]
>> strategy(state, 'O')
2

3) Funkci tictactoe(rows, cols, human_starts=True), ktera umoznuje hrat hru
padajicich piskvorek na planu o danem poctu radku a sloupcu. Muzete
predpokladat, ze zadana velikost planu je rozumna (alespon 4 a mene nez 26
sloupcu a radku). Parametr human_starts urcuje, zda zacina hrac nebo pocitac.
Vypis prubehu hry by mel vypadat stejne, jako v nasledujicich prikladech.
Funkce kontroluje, zda jsou tahy zadane hracem a pocitacem platne a pokud
nejsou, vyzve ho k novemu zadani. Pro hru pocitace volejte vyse uvedene
funkce show_state(state) a strategy(state, symbol). Nezapomente, ze hra muze
skoncit i remizou

Priklad hry, v nemz zacina hrac:

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 5

          X
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 9

          X       O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 6

          X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 5

          O
          X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 4

          O
        X X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 7

          O
        X X X O   O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 3

          O
      X X X X O   O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9
Vyhral jsi!

Bodovani:
- Funkce tictactoe(rows, cols, human_starts=True) musi korektne provadet hru
    hrace a pocitace, kontrolovat zadane tahy hrace a urcit vyhru. Vypis se
    musi shodovat s vyse uvedenymi ukazkami.
- Zakladni variantou strategy je funkce, ktera dodrzuje pravidla, ale jinak
    hraje nahodne. Pokud vas program bude hrat "inteligentne" (napriklad ukonci
    hru, pokud bude mit moznost), ziskate bonusove body. Cim inteligentneji,
    tim vice bodu. V kazdem pripade napiste do komentare strucne vysvetleni,
    jak moc inteligentne program hraje. Kvalita tohoto popisu je take dulezita.

Nekolik tipu:
- Nez zacnete psat kod, rozmyslete si (nejlepe si i nakreslete) dekompozici
    problemu na jednodussi funkce. Jinak se v tom ztratite. Problem lze
    rozlozit ruzne, priklady uzitecnych funkci: is_won(state) nebo
    valid_move(move, state), ale v prubehu reseni by vas pak mely napadnout
    jeste dalsi. Kdykoliv zjistite, ze mate v programu duplicitni kod,
    zbavte se ho (napr. prave pomoci nove pomocne funkce). A vsechny funkce
    by mely zustat dostatecne kratke a prehledne.
- Zacnete variantou s nahodnymi tahy, rozumne chovani pridejte az potom.
    Pri dobre dekompozici by rozsirovani nemel byt problem.
- Zkuste si tuto hru parkrat zahrat (s nekym nebo i sami se sebou), pomuze
    vam to lepe pochopit, jak by mel pocitac optimalne hrat.
"""

from random import randint


# Funkce generuje prvni prazdny herni plan.
def generate_state(rows, cols):
    state = []

    for i in range(rows):
        row = [" "] * cols
        state.append(row)

    return state


# Funkce zajistuje, ze i a j jsou v rozmezi daneho state.
def is_in_range(state, i, j):
    x = len(state)
    y = len(state[0])

    if i <= x and i >= 0:
        if j <= y and j >= 0:
            return True

    return False


# Funkce upravuje dany state tak, ze na posledni prazdne misto v danem sloupci vlozi bud 0 nebo X.
def insert_to_column(state, current_col, is_human, chr):
    j = current_col

    for i in reversed(range((len(state)))):
        if state[i][j] == " ":
            if is_human:
                state[i][j] = chr
                return state

            else:
                state[i][j] = chr
                return state

        else:
            if i == 0:
                print("Sloupecek uz je plny. Vyberte jiny.")

                if is_human:
                    human_plays(state)
                    return state

                if not is_human:
                    strategy(state)
                    return state


# Funkce, ktera vrati sloupecek, do ktereho chce hrat clovek.
def human_plays(state, chr):
    human_column = int(input("Zadejte cislo sloupecku, do ktereho chcete hrat:"))
    return human_column


# Funkce kontroluje, zda pc nebo clovek vyhral, popripade jestli nedoslo k zaplneni planku.
def win(state, char, last_col):
    count = 0
    j = last_col
    start_j = j
    i = 0
    start_i = 0

    for x in range((len(state))):
        if state[x][j] == char:
            i = x
            start_i = i

    # sloupecek
    for x in range(0, 4):
        if state[i][j] == char:
            count += 1
            i = i - 1

    if count == 4:
        return True

    # radek
    count = 0
    i = start_i
    j = start_j

    if is_in_range(state, i, j - 1):
        while state[i][j - 1] == char:
            j = j - 1

        for x in range(0, 4):
            if state[i][j] == char:
                j = j + 1
                count += 1

    if count == 4:
        return True

    # diagonala
    count = 0
    i = start_i
    j = start_j

    if is_in_range(state, i, j):
        while state[i - 1][j - 1] == char:
            j = j - 1
            i = i - 1

        for x in range(0, 4):
            if state[i][j] == char:
                j = j + 1
                i = i + 1
                count += 1

        if count == 4:
            return True

    # diagonala
    count = 0
    i = start_i
    j = start_j

    if is_in_range(state, i - 1, j + 1):
        while state[i - 1][j + 1] == char:
            j = j + 1
            i = i - 1

        for x in range(0, 4):
            if state[i][j] == char:
                j = j - 1
                i = i + 1
                count += 1

    if count == 4:
        return True

    return False


#  Funkce vypise dany plan na standardni vystup. Plan je reprezentovan seznamem
#  seznamu stejne delky, ktere obsahuji znaky X (krizek), O (kolecko) nebo
#  mezera pro neobsazene pole.

# :param state:  Seznam seznamu obsahujici znaky X, 0, a mezera
def show_state(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], end=" ")
        print()

    for k in range(len(state)):
        print("-", end=" ")

    print()

    for l in range(len(state)):
        print(l, end=" ")

    print()


# Funkce pro dany plan state a symbol chr vrati pozici (sloupec) tahu
# pocitace.

#    :param state:  Seznam seznamu obsahujici znaky X, 0, a mezera
#    :param chr:    Znak, ktery se ma vlozit
#    :return:       Sloupec, do ktereho se ma vlozit znak chr
def strategy(state, chr):
    computers_column = randint(0, len(state))
    return computers_column


# Funkce umoznuje hrat hru padajicich piskvorek na planu o danem poctu radku
# a sloupcu.
#   :param rows:    Pocet radku (4..25)
#   :param cols:    Pocet sloupcu (4..25)
#   :param human_starts: True, pokud zacina hrac, False jinak
def tictactoe(rows, cols, human_starts=True):
    end = False
    state = generate_state(rows, cols)
    show_state(state)
    while not end:
        if human_starts:
            human_column = human_plays(state, "X")
            insert_to_column(state, human_column, True, "X")
            show_state(state)
            if win(state, "X", human_column):
                end = True

            computer_column = strategy(state, "O")
            insert_to_column(state, computer_column, False, "O")
            show_state(state)
            if win(state, "O", computer_column):
                end = True


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

# Zde muzete vkladat vlastni testy

tictactoe(6, 6)
if __name__ == '_r_main__':
    tictactoe(6, 6)
    pass
