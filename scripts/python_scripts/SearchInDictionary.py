from Connect_withCs import representSign

import pandas as pd



# read 
compWord_file = pd.read_csv('compoundWords_Dictionary.csv',delimiter=',')
letters_file = pd.read_csv('letters_Dictionary.csv',delimiter=',' )
digits_file = pd.read_csv('digit_Dictionary.csv', delimiter=',' )
words_file = pd.read_csv('words_Dictionary.csv',delimiter=',')


sign_id=0


def textChecker(restructured_text):
    
    
    for word in restructured_text:
        
        if word[1] == 0:
            
            df_word=words_file[words_file.words.eq(word[0])]
            
            if words_file.words.eq(word[0]).any():
                word_id = df_word['words_id'].iloc[0]
                print(word_id)
                #sock.sendall(word_id.encode("UTF-8"))
                representSign(word_id)
            else:
                splitWordToLetters(word[0])
                
                
        elif word[1] == 1:
            df_compWord=compWord_file[compWord_file.compWord.eq(word[0])]
            compWord_id = df_compWord['compWord_id'].iloc[0]
            print(compWord_id)
            #sock.sendall(compWord_id.encode("UTF-8"))
            representSign(compWord_id)
                
        elif word[1] == 2: 
            splitDigit(word[0])
        elif word[1] == 3: 
            df_letter= letters_file[letters_file.letteres.eq(word)]
            letter_id = df_letter['letter_id'].iloc[0]
            #sock.sendall(letter_id.encode("UTF-8"))

            representSign(letter_id) 
                    
            
def splitWordToLetters(word,sock):
    print("inside letter")
    list_of_letters = list(word)
    for letter in list_of_letters:
         print("inside letter and for")
        #data frame letter which containe row from the table 
         df_letter= letters_file[letters_file.letteres.eq(letter)]
         letter_id = df_letter['letter_id'].iloc[0]
         #ock.sendall(letter_id.encode("UTF-8"))
         representSign(letter_id)
         print(letter_id)
         
def splitDigit(digits,sock):
    list_of_digits = list(digits)
    for digit in list_of_digits:
         #data frame letter which containe row from the table 
         df_digit = digits_file[digits_file['digits'].astype(str).str.match(digit)]
         digit_id = df_digit['digit_id'].iloc[0]
         #sock.sendall(digit_id.encode("UTF-8"))
         representSign(digit_id) 




