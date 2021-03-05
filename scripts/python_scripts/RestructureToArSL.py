from SearchInDictionary import checkText
import re

# filtering the text as follows: 
# 1- Delete the extra word that have no signs in ArSL such as: prepositions, relative pronouns, punctuation marks
# 2- Converting written numbers in text to digits
# 3- put a mark of compound word that have on sign in ArSL and collect them in one index

# parameter: the tokenized_text: which contains the list of word.
#            the morphological_result: which contains the analyzed feature that extracted from the words.

def filteringText(tokenized_text,moropholgical_result,sock):
    # read the compound word file 
    compound_words_file = open('compound word.txt', 'r', encoding="utf8",) 
    
    # declare the  prepositions, relative pronouns, punctuation marks, numbers
   
    asma_mosola = ["الذي" , "التي" , "اللذان" , "اللتان" , "الذين" , "اللتان" ,  "اللاتي" ,  "اللواتي" ,  "اللائي"]
    punctuation_marks = ["." , ":" ,  "،", "؟"]
    numbers = [('واحد',1), ('اثنين',2),('ثلاثة',3),('اربعة', 4),('خمسة', 5),('ستة', 6),('سبعة',7),('ثمانية', 8),('تسعة',9),('عشرة',10)
,('صفر',0), ('اثنان',2),('ثلاث',3),('اربع', 4),('خمس', 5),('ست', 6),('سبع',7),('ثمان', 8),('تسع',9),('عشر',10)]
    
    # list of text after filtering
    filtering_result = [] 
    
    # counter of while loop 
    counter = 0
    
    # counter of nested for loop 
    counter2=0
    
    # A temporary variable to store the word and check the next word to determine if these words are compound words or not 
    temp_compound_words=[]
    
    # list for collect the indexes that should deleted from the moropholgical_result list 
    delete_index = []
    
    # loop through the text word by word
    while counter < len(tokenized_text):
 
        # check if text contains asma_mosola  or punctuation_marks or part of speech is preposetion to delete it
        if tokenized_text[counter] in asma_mosola or tokenized_text[counter] in punctuation_marks or moropholgical_result[counter]['pos'] =='prep':
            delete_index.append(counter)
            counter+=1
            continue
        
        # loop to replace each text number to digit
        for num in numbers:
            if tokenized_text[counter] == num[0]:
               moropholgical_result[counter]['lex'] = str(num[1])
               moropholgical_result[counter]['pos'] = 'digit'
               tokenized_text[counter] = str(num[1])
               break
        
        # start from the beginning of file
        compound_words_file.seek(0)  
        
        # loop through the lines of file 
        for line in compound_words_file:
            
            # assign the number of words in a line 
            word_num= len(line.split())
            counter2 = 0
            
            # loop through the words of lines
            for word_in_line in line.split():
                
                # prevent counter from out of range exeption 
                if(counter == (len(tokenized_text))):
                   break
               # check the first word of the line and break if it is not match with tokenized_text[counter]
                if counter2 == 0 :
                    if word_in_line!=tokenized_text[counter]:
                        break
                    
                # check if the word in file match with the word in "tokenized_text" list
                if word_in_line==tokenized_text[counter]:
                    #collect each word of the compound words.
                    temp_compound_words.append(word_in_line) 
                    
                    # check if temp_compound_words contains more than one word, then add the indexes of the word after the first word to delete_index list
                    if len(temp_compound_words) > 1:
                       delete_index.append(counter)
                    counter+=1
                counter2+=1
            
            # check if word_num equal the temp_compound_words 
            if word_num == len(temp_compound_words):
                break
                
            # after finishing each line check if there are compound word stored 
            # in temp_compound_words, to skip the rest of lines. 
            if len(temp_compound_words) !=0:
                    break
        
        # check if the temp_compound_words not empty then add full compound word in the 
        # filtering_result list with 1 mark , else add the word in filtering_result list with '0' mark. 
        if len(temp_compound_words) > 1:
            
            # special case for "السلام عليكم ورحمة الله وبركاته" compound word to make it equals to "السلام عليكم"
            if " ".join(temp_compound_words) == "ورحمة الله وبركاته":
                
                # add index of "ورحمة" before the index of "الله وبركاته" to delete them, because index of "رحمة" not stored in line 69
                delete_index.insert(len(delete_index)-2, counter-2)
                temp_compound_words=[]
                continue
            
            else:
                # add compound words to filtering result
                filtering_result.append((" ".join(temp_compound_words), 1))
                temp_compound_words=[]
                
        # special case if word matched with part of compound word
        elif len(temp_compound_words) == 1:
            filtering_result.append((tokenized_text[counter-1], 0))
            temp_compound_words=[]
        else: 
            # add non compound word to filtering result
            filtering_result.append((tokenized_text[counter], 0))
            counter+=1

#------------------------------------------------------------------------------------------------------
    
    # each iteration delete the indexe that stored in "delete_index" list from "moropholgical_result" list.
    shift_index = 0
    for index in delete_index:
        del moropholgical_result[index - shift_index]
        shift_index += 1
    
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
      
            #any other type of pos
        else:
           restructured_text.append((lemma,0))
        counter+=1
                
                           
                
  
    print(restructured_text)
    
    checkText(restructured_text ,sock)

 



            
    
    
    
#filteringCopoundWord(['صفاء', 'السلام', 'عليكم','عشاء', 'ورحمة', 'الله', 'وبركاته', 'كيف حالك', 'نهنى', 'صباح', 'الخير', 'السلام', 'عليكم'])