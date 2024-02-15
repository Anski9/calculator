


#pyydetään 1+ 2- 3* 4/ 5 vaihto tai 6 lopetus
import math

def luvunpyytaja():
    while True:
        try:
            luku = int(input("Anna luku: " ))
            luku = int(luku)
            return luku 
        except Exception:
            print("Virheellinen syöte!")

def valitse():
    while True:
        try:
            luku = int(input("Tee valinta (1-8): ")) 
            luku = int(luku)
            return luku 
        except Exception:
            print("Virheellinen syöte!")

def main():
    luku1 = luvunpyytaja()
    luku2 = luvunpyytaja()
    while True:
        print("(1) +")
        print("(2) -")
        print("(3) *")
        print("(4) /")
        print("(5)sin(luku1/luku2)")
        print("(6)cos(luku1/luku2)")
        print("(7)Vaihda luvut")
        print("(8)Lopeta")
        print(f"Valitut luvut: {luku1} {luku2}")
        
        valinta = valitse()
        if valinta == 1:
            print(f"Tulos on: {luku1 + luku2}")
        elif valinta == 2:
            print(f"Tulos on: {luku1 - luku2}")
        elif valinta == 3:
            print(f"Tulos on: {luku1 * luku2}")
        elif valinta == 4:
            print(f"Tulos on: {luku1 / luku2}")
        elif valinta == 5:
            print(f"Tulos on: {math.sin(luku1 / luku2)}")
        elif valinta == 6:
            print(f"Tulos on: {math.cos(luku1 / luku2)}")
        elif valinta == 7:
            luku1 = luvunpyytaja()
            luku2 = luvunpyytaja()
        elif valinta == 8:
            exit()
            
        else:
            print("Valintaa ei tunnistettu.")
#pääkoodi    
if __name__ == "__main__":  
    main()
    

    