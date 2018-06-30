def task1():
    sentence =["ASK", "NOT", "WHAT", "YOUR", "COUNTRY", "CAN", "DO", "FOR", "YOU", "ASK", "WHAT", "YOU", "CAN", "DO", "FOR", "YOUR", "COUNTRY"]
    while True:
        print("Which word to find?")
        word = input()
        if word.upper() in sentence:
           for i in range (len(sentence)):
                if word.upper() == sentence[i]:
                    position =(i)
                    print(i)
           
        if not word.upper() in sentence:
            print("Not in sentence!")

def task2_3():
    sentence = ["ASK", "NOT", "WHAT", "YOUR", "COUNTRY", "CAN", "DO", "FOR", "YOU", "ASK", "WHAT", "YOU", "CAN", "DO", "FOR", "YOUR", "COUNTRY"]
    global word_list
    word_list = []
    global position_list
    position_list = []
    ## Gives position in list
    for i, word in enumerate(sentence, start=1):
    ## If the word is not in the word_list   
        if word not in word_list:
    ## Add the word to the list        
            word_list.append(word)
    ## Variable = a string with the length of the word list minus 1 to start at 0
            to_print = str(len(word_list) - 1)
            position_list.append(to_print) 

    ## Else print the position of the word
        else:
            to_print = str(word_list.index(word))
            position_list.append(to_print) 

    ## Extra line, prints out the words being added to the list
##    print()    
##    print(word_list)
##    print()
##    print(position_list)
    for i in range(0,len(position_list)):
        word_list[i]
        print(word_list[i])


def write_to_file():
    out_file = open("WORDLIST"+".txt", "wt")
    out_file.write(str(word_list))
    out_file.close()
    out_file = open("POSITION"+".txt", "wt")
    out_file.write(str(position_list))
    out_file.close()
    in_file = open("WORDLIST"+".txt")
    read_text = in_file.read()
    print (read_text)
    in_file.close()
    in_file = open("POSITION"+".txt")
    read_text = in_file.read()
    print (read_text)
    in_file.close()
    
    
    

task2_3()
#write_to_file()
