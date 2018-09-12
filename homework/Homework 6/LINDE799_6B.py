#Erik Lindeman (LINDE799)
#CSCI 1133
#Homework 6 Problem B

#Makes a list of all the blacklisted words
global BORING
BORING = ["to","the","and","i","of","he","she","a","ill","ive","but","by","we","whose",
        "how","go","such","this","me","can","shes","hes","have","has","had","an","did","so","to","well","on","him","well","or",
        "be","as","those","there","are","do","too","if","it","at","what","that","you","will","in","with","not",
        "for","is","my","o","her","his","am"]

def parse_string(new_sentence):
    #creates empty dictionary to store all unique words
    d = {}
    #splits the sentence into each word, seperated by spaces
    word_list = new_sentence.split(" ")
    #Goes through every word in the list
    for x in range(0,len(word_list)):
        word = word_list[x]
        #if the word isn't already in the dictionary, add it to it.  Otherwise, just increase the count of it in the dictionary
        if not(word in BORING or word == ""):
            if(word in d):
                d[word] +=1
            else:
                d[word] = 1
    #For every item in D, Display how many there are first with X's, then with *'s.
    for item in d:
        count = d[item]
        #See how many counts of 5 there are
        x = count//5
        #After the counts of 5 are taken out, how many counts of 1 are left?
        asterisk = count%5
        #Print the item name
        print(item,end="")
        #print the number of 5's only if it's greater than 0
        if(x>0):
            for y in range(x):
                print("  X",end=" ")
        #print the number of 1's only if it's greater than 0
        if(asterisk>0):
            for y in range(asterisk):
                print("  *",end=" ")
        #Janky way to start a new line after this
        print("")

def main():
    #Input a sentence
    sentence = input("Input a sentence: ")
    new_sentence = ""
    #For every character in the string, only put include it if it's a space or letter (takes out special characters)
    for x in sentence:
        if(x.isalpha() or x == " "):
            new_sentence+=x
    #Makes the letters lowercase
    new_sentence = new_sentence.lower()
    #Runs the function with this new changed sentence
    parse_string(new_sentence)

if  __name__  == '__main__':
    main()
