
import pandas as pd


#Read files of each Dictionaries and 
compWord_file = pd.read_csv('compoundWords_Dictionary.csv',delimiter=',')
letters_file = pd.read_csv('letters_Dictionary.csv',delimiter=',' )
digits_file = pd.read_csv('digit_Dictionary.csv', delimiter=',' )
words_file = pd.read_csv('words_Dictionary.csv',delimiter=',')
verb_words_file = pd.read_csv('verbs_Dictionary.csv',delimiter=',')

sign_id=0


def checkText(restructured_text ,sock):
        
    for word in restructured_text:        
        if word[1] == 0: # check for words
            df_word=words_file[words_file.words.eq(word[0])]
            
            if words_file.words.eq(word[0]).any():
                word_id = df_word['words_id'].iloc[0]
                print(word_id)
                word_id = (str(word_id)+", ")
                sock.sendall(word_id.encode("UTF-8"))
                
            else:
                splitWordToLetters(word[0] ,sock)
                
        elif word[1] == 1: # check for compound words
            df_compWord=compWord_file[compWord_file.compWord.eq(word[0])]
            compWord_id = df_compWord['compWord_id'].iloc[0]
            print(compWord_id)
            compWord_id=(str(compWord_id)+", ")
            sock.sendall(compWord_id.encode("UTF-8"))
            
        elif word[1] == 2: # check for verbs
            df_verb=verb_words_file[verb_words_file.verb_words.eq(word[0])]
            
            if verb_words_file.verb_words.eq(word[0]).any():
                verb_id = df_verb['verb_id'].iloc[0]
                print(verb_id)
                verb_id = (str(verb_id)+", ")
                sock.sendall(verb_id.encode("UTF-8"))
                
            else:
                splitWordToLetters(word[0] ,sock)   
                
        elif word[1] == 3: # check for digits
            splitDigit(word[0],sock)
            
        elif word[1] == 4: # check for letters
            df_letter= letters_file[letters_file.letteres.eq(word[0])]
            letter_id = df_letter['letter_id'].iloc[0]
            letter_id =(str(letter_id)+", ")
            sock.sendall(str(letter_id).encode("UTF-8"))
            
                    
            
def splitWordToLetters(word,sock):
    list_of_letters = list(word)
    for letter in list_of_letters:
        #data frame letter which containe row from the table 
         df_letter= letters_file[letters_file.letteres.eq(letter)]
         letter_id = df_letter['letter_id'].iloc[0]
         print(letter_id)
         letter_id =(str(letter_id)+", ")
         sock.sendall(letter_id.encode("UTF-8"))
         #representSign(letter_id)
         
def splitDigit(digits,sock):
    list_of_digits = list(digits)
    for digit in list_of_digits:
         #data frame letter which containe row from the table 
         df_digit = digits_file[digits_file['digits'].astype(str).str.match(digit)]
         digit_id = df_digit['digit_id'].iloc[0]
         print(digit_id)
         digit_id =(str(digit_id)+", ")
         sock.sendall(digit_id.encode("UTF-8"))
         #representSign(digit_id) 


