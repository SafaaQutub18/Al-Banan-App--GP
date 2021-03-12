from SearchInDictionary import checkText
import re


# function to restructure the text into ArSL structure based on some rules  
# parameter: the text_with_marks: which contains the list of words with there marks after filtering.
#            the morphological_result: which contains the analyzed feature that extracted from the words. 
def restructureText(text_with_marks, moropholgical_result ,sock):
     
    print("--------------------------------------------------------")
    
    # declare the relative pronouns list to delete them.
    asma_mosola = ["الذي" , "التي" , "اللذان" , "اللتان" , "الذين" , "اللتان" ,  "اللاتي" ,  "اللواتي" ,  "اللائي"]
    
    counter = 0
    
    # list for collect the indexes of words that should be deleted from the text_with_marks list and moropholgical_result list
    deleted_indexes=[]
    
    # loop through every words in text_with_marks list
    while counter < len(text_with_marks):
        word = text_with_marks[counter]
        
        # check if the word not compound words
        if word[1] == 0:
            if word[0] in asma_mosola:
                deleted_indexes.append(counter) # add the index of word to delete it, if it is one of asma_mosola list
        counter += 1        
        
    # *****************************************************
   
    # each iteration delete the indexe that stored in "delete_index" list from "moropholgical_result" list and "text_with_marks" list.
    shift_index = 0
    for index in deleted_indexes:
        del moropholgical_result[index - shift_index]
        del text_with_marks[index - shift_index]
        shift_index += 1
    
    
#--------------------------------------------------------------------------------------------    
   
   
    counter=0
    # list of text_with_marks after restructuring
    restructured_text =[]
    
    # loop through all the words to produce final restructuring result
    for word in text_with_marks: 
        
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
                 if features['gen']== 'f' and lemma != word[0] and( features['rat']=='r' or features['rat']=='y'): # r,y = rational
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
                    restructured_text.append(("2",3))
                    
            # ********************************************************

            elif features['num']== 'p': # p = plural
                if features['gen']== 'f' and re.search( 'ة', lemma ) == None and (features['rat']=='r' or features['rat']=='y'):  # r,y = rational
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
            
        #check for the prep
        elif features['pos'] =='prep':
            counter+=1
            continue # skip it because there is no corresping sign in ArSL.
           
        else: #any other type of pos
           restructured_text.append((lemma,0))
           
        counter+=1

    
    print(restructured_text)
    
    # call "checkText" function to search the words in dictionary
    checkText(restructured_text ,sock)

