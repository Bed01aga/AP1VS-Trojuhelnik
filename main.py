import math
import turtle

"""
@authors Ilia Zakharov, Pavel Sakalou, Polina Popova, Aliaksei Sidoryk
"""

def start():
    """Funkce se žádá na uživatele zadat s klávesnici souřadnici bodů vrcholů."""
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    return x, y


def check(sss):
    """Funkce určuje, zda trojúhelník se zvolenými vrcholí existuje (Součet dvou délek MUSÍ být větší než třetí strana)."""
    if (sss[0] + sss[1]) < sss[2] or (sss[1] + sss[2]) < sss[0] or (sss[2] + sss[0]) < sss[1]:
        raise SystemExit("Your triangle can`t exist")
    else:
        return True


def obvod(sss):
    """Tato funkce vypočítá obvod trojúhelníku (Součet všech stran ze seznamu stran)"""
    return sss[0] + sss[1] + sss[2]


def obsah(sss, per):
    """Z Heronového vzorce funkce vypočita obsah trojúhelníku"""
    return math.sqrt(per*(per-sss[0])*(per-sss[1])*(per-sss[2]))


def check_prav(sss):
    """Funkce určuje, zda trojúhelník je pravoúhlý a oznamuje o tom uživatele"""
    if (sss[0]**2 == sss[1]**2 + sss[2]**2) or (sss[1]**2 == sss[2]**2 + sss[0]**2) or (sss[2]**2 == sss[0]**2 + sss[1]**2):
        print("Trojuhelnik je pravouhly")
        return True
    else:
        print("Trojuhelnik neni pravouhly")
        return False


def uhly(sss):
    """Tato funkce vypočítá hodnotu úhlů trojúhelníka ve stupních"""
    uhel1 = math.degrees(math.acos((sss[0]**2 + sss[2]**2 - sss[1]**2) / (2*sss[0]*sss[2])))
    uhel2 = math.degrees(math.acos((sss[0]**2 + sss[1]**2 - sss[2]**2) / (2*sss[0]*sss[1])))
    uhel3 = math.degrees(math.acos((sss[1]**2 + sss[2]**2 - sss[0]**2) / (2*sss[1]*sss[2])))
    return uhel1, uhel2, uhel3


if __name__ == '__main__':
    """Hlavní část programu"""
    point1 = start()
    point2 = start()
    point3 = start()
    list_strana = [((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5,
                   ((point3[0] - point2[0]) ** 2 + (point3[1] - point2[1]) ** 2) ** 0.5,
                   ((point1[0] - point3[0]) ** 2 + (point1[1] - point3[1]) ** 2) ** 0.5]
    """Vypočet stran trojúhelníku a vytvoření seznamu"""
    print("Nasi Strany: "+str(list_strana))
    check(list_strana)
    p = obvod(list_strana) / 2
    print("Obvod je: "+str(obvod(list_strana)))
    print("Obsah je: "+str(obsah(list_strana, p)))
    check_prav(list_strana)
    print(uhly(list_strana))
    uholky = uhly(list_strana)
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
