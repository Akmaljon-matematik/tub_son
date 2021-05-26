
"""k-o'rindagi tub sonni topadigan programma
tuzuvchi: Oqboyev Akmaljon
sana:20.05.2020"""
import math
def k_tartibdagi_tub_son():
    try:
        k = int(input("Nechanchi nomerdagi tub sonni bilmoqchisiz? -->", ))#foydalanuvchi tamonidan kiritiladigan tartib raqami
        a = 1
        i = 2
        if k==1:
            print("1-tub son=2")
        elif k==2:
            print("2-tub son=3")
        else:
            while i<=k:
                b = 1
                a+=2
                a1 = int(math.sqrt(a))
                for n in range(2, a1+1):
                    b=b*(a%n)
                if b==0:
                    i=i
                else:
                    i=i+1
        print(k, "- tub son =", a)
    except:
        return print("Natural son kiriting!")



k_tartibdagi_tub_son()

