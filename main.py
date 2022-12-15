"""Trojúhelník."""
import math
import turtle

"""
Ilia Zakharov, Pavel Sakalou, Polina Popova, Aliaksei Sidoryk
"""


def start():
    """Funkce se žádá na uživatele zadat s klávesnici souřadnici bodů vrcholů.

    Parametry(Parameters)
    ---------------------
    Žadné parametry

    Vrátí(Returns)
    --------------
    `x` : Vrátí souřadnice x vrcholy v typu `float`;
    `y` : Vrátí souřadnice y vrcholy v typu `float`

    """
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    return x, y


def seznam_stran(bod1, bod2, bod3):
    """Tato funkce vypočítá strany trojúhelníka.

    Parametry(Parameters)
    ---------------------
    `bod1` :
        Parametr `bod1` je souřadnice `x` a `y` prvního bodu, typ `list`;
    `bod2` :
        Parametr `bod2` je souřadnice `x` a `y` druhého bodu, typ `list`;
    `bod3` :
        Parametr `bod3` je souřadnice `x` a `y` třetího bodu, typ `list`

    Vrátí(Returns)
    --------------
    `list_strana` :
    Parametr `list_strana` je seznam všech stran trojúhelníka, typ `list`

    """
    global list_strana
    list_strana = [((bod2[0] - bod1[0]) ** 2 +
                    (bod2[1] - bod1[1]) ** 2) ** 0.5,
                   ((bod3[0] - bod2[0]) ** 2 +
                    (bod3[1] - bod2[1]) ** 2) ** 0.5,
                   ((bod1[0] - bod3[0]) ** 2 +
                    (bod1[1] - bod3[1]) ** 2) ** 0.5]


def check(sss):
    """Funkce určuje, zda trojúhelník se zvolenými vrcholí existuje.

    (Součet dvou délek MUSÍ být větší než třetí strana).

    Parametry(Parameters)
    ---------------------
    `sss` :
        Parametr `sss` je seznam všech stran trojúhelníka, typ `list`

        Vrátí(Returns)
        --------------
        `SystemExit()` :
            Funkce vrátí `SystemExit()` pokud neexistuje trojúhelníka
            s uvedenými vrcholy;
        `True` :
            Funkce vrátí `True` pokud trojúhelník s uvedenými vrcholy existuje

    """
    if (sss[0] + sss[1]) < sss[2] or (sss[1] + sss[2]) < sss[0] \
            or (sss[2] + sss[0]) < sss[1]:
        raise SystemExit("Your triangle can`t exist")
    else:
        return True


def obvod(sss):
    """Tato funkce vypočítá obvod trojúhelníku.

    (Součet všech stran ze seznamu stran)

        Parametry(Parameters)
        ---------------------
        `sss` :
            Parametr `sss` je seznam všech stran trojúhelníka, typ `list`

        Vrátí(Returns)
        --------------
        Součet všech stran ze seznamu stran

    """
    return sss[0] + sss[1] + sss[2]


def obsah(sss, per):
    """Z Heronového vzorce funkce vypočita obsah trojúhelníku.

    Parametry(Parameters)
        ---------------------
        `sss` :
            Parametr `sss` je seznam všech stran trojúhelníka, typ `list`;
        `per` :
            Parametr `per` je pulka obvodu trojúhelníka, typ `float`

        Vrátí(Returns)
        --------------
        Obsah

    """
    return math.sqrt(per*(per-sss[0])*(per-sss[1])*(per-sss[2]))


def check_prav(sss):
    """Funkce určuje, zda trojúhelník je pravoúhlý a oznamuje o tom uživatele.

    Parametry(Parameters)
        ---------------------
        `sss` :
            Parametr `sss` je seznam všech stran trojúhelníka, typ `list`

        Vrátí(Returns)
        --------------
        `True` :
        Funkce vrátí `True` pokud trojúhelník
        s uvedenými vrcholy je pravoúhlý, typ `boolean`;
        `False` :
        Funkce vrátí `False` pokud trojúhelník
        s uvedenými vrcholy není pravoúhlý, typ `boolean`

    """
    if (sss[0]**2 == sss[1]**2 + sss[2]**2) or \
            (sss[1]**2 == sss[2]**2 + sss[0]**2) or\
            (sss[2]**2 == sss[0]**2 + sss[1]**2):
        print("Trojuhelnik je pravouhly")
        return True
    else:
        print("Trojuhelnik neni pravouhly")
        return False


def uhly(sss):
    """Tato funkce vypočítá hodnotu úhlů trojúhelníka ve stupních.

    Parametry(Parameters)
        ---------------------
        `sss` :
            Parametr `sss` je seznam všech stran trojúhelníka, typ `list`

        Vrátí(Returns)
        --------------
        `uhel1` :
            Hodnota prvního úhlu ve stupních, typ `float`;
        `uhel2` :
            Hodnota druhého úhlu ve stupních, typ `float`;
        `uhel3` :
            Hodnota třetího úhlu ve stupních, typ `float`

    """
    uhel1 = math.degrees(math.acos((sss[0]**2 + sss[2]**2 - sss[1]**2) /
                                   (2*sss[0]*sss[2])))
    uhel2 = math.degrees(math.acos((sss[0]**2 + sss[1]**2 - sss[2]**2) /
                                   (2*sss[0]*sss[1])))
    uhel3 = math.degrees(math.acos((sss[1]**2 + sss[2]**2 - sss[0]**2) /
                                   (2*sss[1]*sss[2])))
    return uhel1, uhel2, uhel3


def trojuhelnik_printer():
    """Funkce pomoci knihovny Turtle kreslí obrázek trojúhelníku.

    Parametry(Parameters)
        ---------------------
        Žadné parametry

        Vrátí(Returns)
        --------------
        Obrazek trojúhelníku

    """
    t = turtle.Turtle()
    t.color('red')
    t.forward(list_strana[0])
    t.right(180)
    t.left(uholky[1])
    t.color('blue')
    t.forward(list_strana[1])
    t.right(180)
    t.left(uholky[2])
    t.color('black')
    t.forward(list_strana[2])
    t.right(180)
    t.left(uholky[0])
    turtle.exitonclick()


if __name__ == '__main__':
    point1 = start()
    point2 = start()
    point3 = start()
    seznam_stran(point1, point2, point3)
    print("Nasi Strany: "+str(list_strana))
    check(list_strana)
    p = obvod(list_strana) / 2
    print("Obvod je: "+str(obvod(list_strana)))
    print("Obsah je: "+str(obsah(list_strana, p)))
    check_prav(list_strana)
    print(uhly(list_strana))
    uholky = uhly(list_strana)
    trojuhelnik_printer()
