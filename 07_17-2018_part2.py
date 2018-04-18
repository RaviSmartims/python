char = input()
if ord(char)>=65 and ord(char)<=90:
    print("You have entered the uppercase letter.")
    if char in ("A", "E", "I", "O", "U"):
        print("The letter is vowel.")
    else:
        print("The letter is consonant")
elif ord(char)>=97 and ord(char)<=122:
    print("You have entered the lowercase letter.")
    if char in ("a", "e", "i", "o", "u"):
        print("The letter is vowel.")
    else:
         print("The letter is consonant")
else:
    print("You did not enter the alphabet.")




    
sp = 30
cp = 50
if sp>cp:
    print("Congragulations")
    print("You have a profit of", sp-cp,"Rupees")
elif cp> sp :
    print("Oops!")
    print("You have made a loss of", cp-sp, "Rupees")
else:
    print("You didnt make or loss money")
         
           

        
    
