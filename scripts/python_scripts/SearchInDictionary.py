
import pandas as pd


#Read each Dictionary files  
compWord_file = pd.read_csv('compoundWords_Dictionary.csv',delimiter=',')
letters_file = pd.read_csv('letters_Dictionary.csv',delimiter=',' )
digits_file = pd.read_csv('digit_Dictionary.csv', delimiter=',' )
words_file = pd.read_csv('words_Dictionary.csv',delimiter=',')
verb_words_file = pd.read_csv('verbs_Dictionary.csv',delimiter=',')


# function used for searching for the word in dictionary files, if it exists the sign id will be returned 
# otherwise the system calls the “splitWordToLetters” or “splitDigit” functions to return the id of each letter or digit.
def checkText(restructured_text ,sock):
    #print("checkText", restructured_text)
    # loop through the restructured_text list     
    for word in restructured_text: 
        #print("search", word)
        if word[1] == 0: # check for words
            df_word=words_file[words_file.words.eq(word[0])]
            
            # check if the word exist, return the word id 
            if not df_word.empty:
                word_id = df_word['words_id'].iloc[0]
                print(word_id)
                word_id = (str(word_id)+", ")
                
                # send the word id to c# video listener script
                sock.sendall(word_id.encode("UTF-8"))
                
            else: # the word not exist, split word to letters
                splitWordToLetters(word[0] ,sock)
                
              
        elif word[1] == 1: # check for compound words
            print("jdszgfvjdsfhkjsvhk")
            # search for compound words and return the compound words id
            df_compWord=compWord_file[compWord_file.compWord.eq(word[0])]
            compWord_id = df_compWord['compWord_id'].iloc[0]
            print(compWord_id)
            compWord_id=(str(compWord_id)+", ")
            
            # send the compound words id to c# video listener script
            sock.sendall(compWord_id.encode("UTF-8"))
            
        elif word[1] == 2: # check for verbs
            df_verb=verb_words_file[verb_words_file.verb_words.eq(word[0])]
            
            # check if the verb exist, return the verb id 
            if not df_verb.empty:
                verb_id = df_verb['verb_id'].iloc[0]
                print(verb_id)
                verb_id = (str(verb_id)+", ")
                
                # send the verb id to c# video listener script
                sock.sendall(verb_id.encode("UTF-8"))
                
            else: # the verb not exist, split verb to letters
                splitWordToLetters(word[0] ,sock)   
                
        elif word[1] == 3: # check for digits
            df_digit= digits_file[digits_file.digits.eq(word[0])]
            
            if not df_digit.empty:
                digit_id = df_digit['digit_id'].iloc[0]
                print(digit_id)
                digit_id = (str(digit_id)+", ")
                
                # send the digit id to c# video listener script
                sock.sendall(digit_id.encode("UTF-8"))
                
            else: # the digit not exist, split digit 
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


