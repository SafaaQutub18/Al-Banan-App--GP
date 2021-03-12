
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
<<<<<<< HEAD
    
    # tokanized text to word 
    text_without_marks = [] 
=======
    text = [] 
>>>>>>> 393230048af6ccb147111cd1d8c60a4a4ffafe1f
   
    # loop through the lines of file   
    for line in compound_words_file :
        # loop to search on the compound words in text and store the start and end indexes
        for m in re.finditer(line.strip() , text):
            if line.strip()=='': # break if arrive to end of lines
                break
            compWord_indexes.append(m.span()) # store the start-end indexes of compWord
    
    
   # A temporary variable inside the loop to collect the character of the word
    temp_words=""
    # counter of while loop 
    counter = 0
   # counter of for loop 
    counter2 = 0
    
    # loop throw evry char in text
    while counter < len(text):  
         if text[counter] != " ":
             counter2=counter
             for index in compWord_indexes:
                 
                 if index[0] == counter:
                    text_with_marks.append((text[index[0]:index[1]], 1))
                    text.append(text[index[0]])
                    counter+= len(text[index[0]:index[1]])
                    break
             if counter2==counter:
                 temp_words+=(text[counter]) #collect the character of evry word
         else:
             text_with_marks.append((temp_words, 0))
             text.append(temp_words)
             temp_words=""
         counter+=1        
             
    if temp_words!="":
        text_with_marks.append((temp_words, 0)) 
        text.append(temp_words)
    
    extractMorphFeatures(text, text_with_marks,sock)
        