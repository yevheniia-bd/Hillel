def tous_les_nombres() -> list:
    list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
    for n in list_of_six:
        if n % 5 == 0 and n < 150:
         print(n)
tous_les_nombres()


