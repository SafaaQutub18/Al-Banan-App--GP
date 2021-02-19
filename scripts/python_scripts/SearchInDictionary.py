

import pandas as pd

cWord_file = pd.read_csv('compoundWords_Dictionary.csv',delimiter=',')
letters_file = pd.read_csv('letters_Dictionary.csv',delimiter=',' )
digit_file = pd.read_csv('digit_Dictionary.csv', delimiter=',' )
words_file = pd.read_csv('words_Dictionary.csv',delimiter=';')


def splitWordToLetters(word):
    list_of_letters = list(word)
    print(list_of_letters)
    for letters in list_of_letters:
         x = letters_file[letters_file['letteres'].str.match(letters)]
         print(x['letter_id'])
         letter_id = x['letter_id']
         print(letter_id)


def textChecker(restructured_text):
    
    for word in restructured_text:
        if(word[1] == 0):
            x = words_file[words_file['words'].str.match(word[0])]
            if words_file['words'].str.match(word[0]).any():
                word_id = x['words_id'][0]
            else:
              
                splitWordToLetters(word[0])
            
    #for i in range(len(cw)) : 
        
        #print(cw.loc[i, "cw"], cw.loc[i, "cw_id"])


textChecker([("كثير",0)])

