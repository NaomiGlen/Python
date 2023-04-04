def be_cheerful(name="Ms. Nibbles", repeat=2): #repeat=x will repeat the function call that many times 
    print(f"Good morning {name}\n" * repeat) #\n will run the repeat on a new line instead of all on the same line

be_cheerful("Naomi")
be_cheerful(repeat=4,name="Boonie Bear")#(4,"Boonie Bear") will break the code because it is expecting a string.