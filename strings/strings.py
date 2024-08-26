def learning_strings():
    as_arrays = "Strings are arrays"
    print(as_arrays[1])
    
    #looping through a string
    for x in "banana":
        print(x)
    
    # String length 
    print(len(as_arrays))
    
    #Check string( To check if a certain phrase or character is present in a string, we can use the keyword in.)
    txt = "I am going to build my mental fortitude and become the best version of myself "
    print("build" in txt) # biuld is in txt so output is True
    
    
    # method 2 using if 
    if "build" in txt:
        print("Yes 'build ' is present. ")
      
        
    # To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
    
    print("Hello" not in txt) # since Hello is not present in txt so output is True
    
    # we can use if statement here too
    if "Hello" not in txt:
        print("No 'Hello' is NOT present ")
        
# slicing strings 
    
    b = "hello, world"
    print(b[:5]) # slicing fron the start 
     
    print(b[2:]) # slicing from the end 
    
# modify strings 
    a = "Hello world"
    a = a.upper() # Upper case 
    print(a)
    a = a.lower # modify to lower case 
    print(a)
    
# remove whitespace 
    wht = "Hello , world!"
    print(wht.strip())
    
# replace string 

    hi = "going to replace"
    print(hi.replace("g","r"))
    
# Split string 
    a = "isko,split"
    print(a.split(",")) # retirns ['isko', ' split']
    
# string formatting 
    age = 12 
    txt = f"myageis{age}"
    print(txt)
#placeholders and modifiers 
    position = 69 
    txt = f"the most overrated position is {position:.2f}"
    print(txt)
    
    

learning_strings()
    
    
