def main():
    alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    cryptogram = ("""VZ FRYSVFU NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY 
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF 
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR""")
    print()
    print ("The original cryptogram for assignment 2 is :")
    print()
    print (cryptogram)
    print()
    def crypto():
        try:
            return int(input("""How many places would you like to move the script? 
If decyphering for assignment 2, Q2, chamber of strings, the answer is 13! Press enter for more options."""))
        except ValueError:
            print("A number is required to move the script.")
            print()
            fin = input("Would you like to quit? Y/N  ")
            if fin == ("y") or ("Y"):
                quit()
            else:
                main()
            main()
    key = crypto()
    solve(alpha, cryptogram, key * (-1))
    main()

def solve(abc, message, key):
    cypherText = ""
    for letter in message:
        if letter in abc:
            movescript = (abc.find(letter) + key * 2) % 52
            cypherText += abc[movescript]
        else:
            cypherText += letter
    print()
    print("The decyphered script is: ")
    print()
    print(cypherText)
    return cypherText

main()
