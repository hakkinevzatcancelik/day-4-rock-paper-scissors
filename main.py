import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
oyun_pos = [rock , paper , scissors]

gamer_secim = int(input(' Hamlenizi seçin. Taş için "0" ,Kağıt için "1",Makas için "2" '))
if gamer_secim >= 3 or gamer_secim < 0:
    print("Geçersiz bir sayı girdiniz!!")
else:
    print(oyun_pos[gamer_secim])
    
    bilgisayar_secim = random.randint(0 , 2)
    print(f"Bilgisayarın seçimi")

    print(oyun_pos[bilgisayar_secim])

    if gamer_secim == 0 and bilgisayar_secim == 2:
        print("Siz kazandınız!")
    
    elif bilgisayar_secim == 2 and gamer_secim ==2:
        print("Bilgisayar kazandı!")
        
    elif bilgisayar_secim > gamer_secim:
        print("Bilgisayar kazandı!")
    
    elif bilgisayar_secim == gamer_secim:
        print("Berabere sonuçlandı.")
    else:
        print("Siz kazandınız!")