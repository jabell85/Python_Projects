#Madlib game generator

#Loop will come back to this point once it has ran
comeback = 1
while (comeback < 10):
#All question that will be ask which user fills out
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun_2 = input("Choose another noun: ")
    place = input("Choose a place: ")
    adjective = input("Choose an adjective(Describing word): ")
    noun_3 = input("Choose the last noun: ")

#Display the story based on the inputs of the user
    print("------------------------------------------")
    print("Be Kind to your", noun , "-footed", p_noun)
    print("For a duck may be someone's", noun_2 , ",")
    print("Be Kind to your", p_noun , "in", place)
    print("Where the weather is always", adjective , "." )
    print("You may think that is the", noun_3 , ",")
    print("Well it is!")
    print("------------------------------------------")

#Loop back to "comeback = 1"
    comeback = comeback + 1 
