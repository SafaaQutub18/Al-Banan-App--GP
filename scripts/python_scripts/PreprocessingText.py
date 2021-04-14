
from MoropholgicalAnalyzer import extractMorphFeatures
import re
import unicodedata as ud

# filteringText function  put a mark of compound word that have one sign in ArSL and collect them in one index to prevent any change on them
# parameter text that received from speech 

def filteringText(text,sock):
    
    # read the compound word file 
    compound_words_file = open('compound word.txt', 'r', encoding="utf8",) 
    
    # delete punctuation_marks from the text
    text= ''.join(c for c in text if not ud.category(c).startswith('P'))
    print(text)

    # list for the indexes of compword
    compWord_indexes=[]
   
    # list of text after put a mark of compound word
    text_with_marks = [] 

    # tokanized text to word 
    text_list = [] 

    
    # loop through the lines of file   
    for line in compound_words_file :
        
        # loop to search the compound words in text and store the start and end indexes
        for m in re.finditer(line.strip() , text):
            #print("jhhugghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            if line.strip()=='': # break if arrive to end of lines
                break
            compWord_indexes.append(m.span()) # store the start-end indexes of compWord
    
            
# ******************************************************************************************
    
    # A temporary variable inside the loop to collect the character of the word
    temp_words=""
    
    # counter of while loop 
    counter = 0
    
    # counter of for loop 
    temp_counter = 0
     
    # loop through every char in text
    while counter < len(text): 
        
        # check if the text not space 
         if text[counter] != " ":
             
             # store the counter temporary 
             temp_counter=counter
             
             # loop through indexes of compound words
             for index in compWord_indexes:
                 
                 # check if the first index of compound word equal counter to put mark as compound word
                 if index[0] == counter:
                    
                    # add the compound word to text_with_marks list with 1 number as mark 
                    text_with_marks.append((text[index[0]:index[1]], 1))
                    
                    # add the compound word to text list 
                    text_list.append(text[index[0]])
                    
                    # increase counter to skip the ompound word
                    counter+= len(text[index[0]:index[1]])
                    break
             # check if there are no change to counter after exist from the loop, that means is not find compound word  
             if temp_counter==counter:
                temp_words+=(text[counter]) #collect the characters of every word
         else:
             # add the word to text_with_marks list with 0 number as mark
             text_with_marks.append((temp_words, 0))
             
             # add the word to text list
             text_list.append(temp_words)
             temp_words=""
         counter+=1      
         
    # add last word of text because while loop end befor the add last word of text        
    if temp_words!="":
        text_with_marks.append((temp_words, 0)) 
        text_list.append(temp_words)
        
    #print(text_with_marks)
    extractMorphFeatures(text_list,text_with_marks,sock)
        