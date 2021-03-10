from SearchInDictionary import checkText
import re

# filtering the text as follows: 
# 1- Delete the extra word that have no signs in ArSL such as: prepositions, relative pronouns, punctuation marks
# 2- Converting written numbers in text to digits
# 3- put a mark of compound word that have on sign in ArSL and collect them in one index

# parameter: the tokenized_text: which contains the list of word.
#            the morphological_result: which contains the analyzed feature that extracted from the words.

def filteringText(text,tokenized_text,moropholgical_result,sock):

      # read the compound word file 
    compound_words_file = open('compound word.txt', 'r', encoding="utf8",) 
    
    # declare the  prepositions, relative pronouns, punctuation marks, numbers
   
    asma_mosola = ["الذي" , "التي" , "اللذان" , "اللتان" , "الذين" , "اللتان" ,  "اللاتي" ,  "اللواتي" ,  "اللائي"]
    punctuation_marks = ["." , ":" ,  "،", "؟"]
   
    
    # list for the indexes of compword
    compWord_indexes=[]
   
    text = " ".join(tokenized_text)
    # list of text after filtering
    filtering_result = []  
   
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
         if(text[counter] != " ") :
             counter2=counter
             for index in compWord_indexes:
                 
                 if index[0]== counter:
                    filtering_result.append((text[index[0]:index[1]], 1))
                    counter+= len(text[index[0]:index[1]])
                    break
             if counter2==counter:
                 
                 temp_words+=(text[counter]) #collect the character of evry word
                 
         else:
             filtering_result.append((temp_words, 0))  
             temp_words=""
         counter+=1
             
             
    if temp_words!="":
        filtering_result.append((temp_words, 0)) 
        
    #--------------------------------------------------------------------------------------------------------------------    
        
    deleted_index_num = 0 
    counter = 0
    deleted_indexes_morph=[]
    deleted_indexes_filter=[]
    shift_index = 0
    while counter < len(filtering_result):
        
        word = filtering_result[counter]
        
        if word[1] == 0:
            
            if word[0] in asma_mosola or word[0] in punctuation_marks:
                print("delete this:", filtering_result[counter])
                deleted_indexes_morph.append(counter)
                deleted_indexes_filter.append(counter)
     
        else:
            deleted_index_num = len(word[0].split())-1
            for index in range(counter ,counter+deleted_index_num):
                deleted_indexes_morph.append(index)
        counter +=1
        
        
        
    #------------------------------------------------------------------------------------------------------
   
    # each iteration delete the indexe that stored in "delete_index" list from "moropholgical_result" list.
    shift_index = 0
    for index in deleted_indexes_morph:
        del moropholgical_result[index - shift_index]
        shift_index += 1
        
    shift_index = 0
    for index in deleted_indexes_filter:
        del filtering_result[index - shift_index]
        shift_index += 1
        
    print(moropholgical_result) 
    print(filtering_result)
    restructureText(filtering_result, moropholgical_result ,sock)
  
    
# function to restructure the text into ArSL structure based on some rules  
# parameter: the filtering_result: which contains the list of word after filtering.
#            the morphological_result: which contains the analyzed feature that extracted from the words.
     
def restructureText(filtering_result, moropholgical_result ,sock):
        
    counter=0
    
    # list of text after restructuring
    restructured_text =[]
    
    # loop through all the words to produce final restructuring result
    for word in filtering_result: 
        
        # skip the compound words because there are no need to restructure them.
        if word[1]==1:
            restructured_text.append(word)
            counter+=1
            continue
        
        # assign the moropholgical_result to features variables
        features= moropholgical_result[counter]
        
        # filter the lemam to delete extra character 
        lemma=  re.sub("[^أ-ي ٱآ]","",features['lex']) 
        
        # add "مثل" word to express about "ك"
        if (re.sub("[^ك+_]","",features['atbtok'])) == 'ك+_' :
            restructured_text.append(("مثل",0))
         
        # check if the POS equals noun or adjectiv or demonstrative pronoun to add appropriate word depend on the features and cases  
        if  features['pos']== 'noun' or features['pos']== 'adj' or features['pos']== 'pron_dem':
            if features['num']== 's': # s= singular
                 if features['gen']== 'f' and lemma != word[0] and features['rat']=='r' or features['rat']=='y': # r,y = rational
                        restructured_text.append((lemma,0))
                        restructured_text.append(("أنثى",0))
                        
                 else: # else if gen = male
                      restructured_text.append((lemma,0))

    
   # ********************************************************

            elif features['num']== 'd': # d= dual
                if features['gen']== 'f' and re.search( 'ة', lemma ) == None and (features['rat']=='r' or features['rat']=='y'): # r,y = rational , ex. the word "شمس" is female but not rational
                      

                      restructured_text.append((lemma,0))
                      restructured_text.append(("2",3))
                      restructured_text.append(("أنثى",0))

                      
                else:  # else if gen = male
                    restructured_text.append((lemma,0))
                    restructured_text.append(("2",2))
            # ********************************************************

            elif features['num']== 'p': # p = plural
                if features['gen']== 'f' and re.search( 'ة', lemma ) == None and features['rat']=='r' or features['rat']=='y':  # r,y = rational
                  restructured_text.append((lemma,0))
                  restructured_text.append(("كثير",0))
                  restructured_text.append(("أنثى",0))
                  
                else:  # else if gen = male
                    restructured_text.append((lemma,0))
                    restructured_text.append(("كثير",0))
       
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        # check if the POS equals verb to add appropriate word depend on the features and cases 
        elif features['pos']== 'verb':
            if features['asp']== 'i': # i = imperfect (which means present or future tenses)
               if features['per']== '1' and features['num']== 'p': # per= person , 1 = first person (which means we or I) ,p = plural
                  restructured_text.append(("نحن",0))
                  
            #check if the verb start with 'سـ' letter to distinguish between the present and future
               if features['prc1']!= 'sa_fut': #sa_fut = 'سـ' future letter
                  restructured_text.append((lemma,2))
               else:
                  restructured_text.append((lemma,2))
                  restructured_text.append(("قريب",0))
                  
            else: # other verb types 
                  restructured_text.append((lemma,2))
                            
        #check for Interrogative names (أسماء الاستفهام)                
        elif features['pos']=='adv_rel' or features['pos']=='pron_rel' or features['pos']=='adv_interrog' or features['pos']=='pron_interrog' or features['pos']=='part_interrog' :
            restructured_text.append(("استفهام",0))
            restructured_text.append((lemma,0))
            
             #check for the digit
        elif features['pos']=='digit': 
            restructured_text.append((re.sub("[^0-9]","",word[0]),3))  
            
            #check for the arabic letters
        elif features['pos']=='abbrev': 
            restructured_text.append((lemma,4))
        elif features['pos'] =='prep':
            continue
            #any other type of pos
        else:
           restructured_text.append((lemma,0))
        counter+=1
                
                           
                
  
    print(restructured_text)
    
    checkText(restructured_text ,sock)

 



            
    
    
    
