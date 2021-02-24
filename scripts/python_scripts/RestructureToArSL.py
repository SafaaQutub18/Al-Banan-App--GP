from SearchInDictionary import textChecker
import re
# filtering the compound word and word in text. 
# parameter: the tokenized_text: which contains the list of word.
#            the morphological_result: which contains the analyzed feature that extracted from the words.


 

def filteringText(tokenized_text,moropholgical_result,sock):
    # read the compound word file 
    compound_word_file = open('compound word.txt', 'r', encoding="utf8",) 
    
    jarr_letters = ["من", "عن", "على",  "حتي", "حتى", "في","الي" , "الى", "إلي", "إلى"] 
    asma_mosola = ["الذي" , "التي" , "اللذان" , "اللتان" , "الذين" , "اللتان" ,  "اللاتي" ,  "اللواتي" ,  "اللائي"]
    punctuation_marks = ["." , ":" ,  "،", "؟"]
    filtering_result = [] 
    counter = 0
    
    temp_compound_word=[]
    delete_index = []
    
    # loop through the text word by word
    while counter < len(tokenized_text):
 
        # check if text contains asma_mosola or jarr_letters to delete it
        if tokenized_text[counter] in asma_mosola or tokenized_text[counter] in jarr_letters or tokenized_text[counter] in punctuation_marks:
            delete_index.append(counter)
            counter+=1
            continue
        
        # start from the beginning of file
        compound_word_file.seek(0)  
        
        # loop through the lines of file 
        for line in compound_word_file:
            
            # loop through the words of lines
            for word_in_line in line.split():
                
                #prevent counter from out of range exeption 
                if(counter == (len(tokenized_text))):
                   break
               
                # check if the word in file match with the word in "tokenized_text" list
                if word_in_line==tokenized_text[counter]:
                    
                    #collect each word of the compound_word.
                    temp_compound_word.append(word_in_line) 
                    
                    # add the indexes of the word after the first word of compound word  to deleted
                    if len(temp_compound_word) > 1:
                       delete_index.append(counter)
                    counter+=1 
              
                    
            # after finishing each line check if there are compound word stored 
            # in temp_compound_word, that for skip the rest of lines. 
            if len(temp_compound_word) !=0:
                    break
        
        #check if the temp_compound_word not empty add full compound word in the 
        #filtering_result list , else the add the word filtering_result list. 
        #that for keeping the order of the text.  
        if len(temp_compound_word) > 1:
            
            # special case for "السلام عليكم ورحمة الله وبركاته"
            if " ".join(temp_compound_word) == "ورحمة الله وبركاته":
                # add index with index of "ورحمة" before the index "الله وبركاته"
                delete_index.insert(len(delete_index)-2, counter-2)
                temp_compound_word=[]
                continue
            else: 
                # add compound word to filtering result
                filtering_result.append((" ".join(temp_compound_word), 1))
                temp_compound_word=[]
                
        # special case if word matched with part of compound word
        elif len(temp_compound_word) == 1:
            filtering_result.append((tokenized_text[counter-1], 0))
            temp_compound_word=[]
        else: 
            # add non compound word to filtering result
            filtering_result.append((tokenized_text[counter], 0))
            counter+=1

#------------------------------------------------------------------------------------------------------
    
    # each iteration increase shift_index by one
    shift_index = 0
    for index in delete_index:
        del moropholgical_result[index - shift_index]
        shift_index += 1
        
    
    print(len(moropholgical_result))
    print(len(filtering_result))
    
    restructureText(filtering_result, moropholgical_result ,sock)
    
    
    
 
 
    
def restructureText(filtering_result, moropholgical_result ,sock):
        
    counter=0
    final_restructuring =[]
    
    # loop through all the words to produce final restructuring result
    for word in filtering_result: 
        
        # skip the compound word
        if word[1]==1:
            final_restructuring.append(word)
            counter+=1
            continue
        
        features= moropholgical_result[counter]
        # filter the lemam to delete extra character 
        lemma=  re.sub("[^أ-ي ٱآ]","",features['lex']) 
        
         
        # check if the POS equals noun or adj to add appropriate word depend on the features and cases  
        if  features['pos']== 'noun' or features['pos']== 'adj' or features['pos']== 'pron_dem':
            if features['form_num']== 's': # s= singler
                 if features['gen']== 'f' and lemma != word[0] and features['rat']=='r' or features['rat']=='y': # r = rational
                        final_restructuring.append((lemma,0))
                        final_restructuring.append(("أنثى",0))
                        
                 else: # else if gen = male
                      final_restructuring.append((lemma,0))

    
   # ********************************************************

            elif features['form_num']== 'd': # d= dual
                if features['gen']== 'f' and re.search( 'ة', lemma ) == None and features['rat']=='r' or features['rat']=='y': # r = rational 
                      
                      final_restructuring.append((lemma,0))
                      final_restructuring.append(("2",2))
                      final_restructuring.append(("أنثى",0))
                      
                else:  # else if gen = male
                    final_restructuring.append((lemma,0))
                    final_restructuring.append(("2",2))
            # ********************************************************

            elif features['form_num']== 'p': # p = plural
                if features['gen']== 'f' and re.search( 'ة', lemma ) == None and features['rat']=='r' or features['rat']=='y':  # r = rational
                  final_restructuring.append((lemma,0))
                  final_restructuring.append(("كثير",0))
                  final_restructuring.append(("أنثى",0))
                  
                else:  # else if gen = male
                    final_restructuring.append((lemma,0))
                    final_restructuring.append(("كثير",0))
       
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # check if the POS equals verb to add appropriate word depend on the features and cases 
        
        elif features['pos']== 'verb':
            if features['asp']== 'p': # p= perfect (which means past tense)
                final_restructuring.append((lemma,2))
                final_restructuring.append(("ٱنتهى",0))
                
            elif features['asp']== 'i': # i = imperfect (which means present or future tenses)
               if features['per']== '1' and features['form_num']== 'p': # per= person , 1 = first person (which means we or I) ,p = plural 
                   final_restructuring.append(("نحن",0)) 
                   
                #chexk if the verb start with 'سـ' letter to distinguish between the presen and future
               if features['prc1']!= 'sa_fut': #sa_fut = 'سـ' future letter
                   final_restructuring.append((lemma,2))
                   final_restructuring.append(("آن",0))
                   
               else: 
                   final_restructuring.append((lemma,2))
                   final_restructuring.append(("قريب",0))
                            
        #check for Interrogative names (أسماء الاستفهام)                
        elif features['pos']=='adv_rel' or features['pos']=='pron_rel' or features['pos']=='adv_interrog' or features['pos']=='pron_interrog' or features['pos']=='part_interrog' :
            final_restructuring.append(("استفهام",0))
            final_restructuring.append((lemma,0))
                
        elif features['pos']=='digit': 
            final_restructuring.append((re.sub("[^0-9]","",word[0]),3))            
            #check for the arabic letters
        elif features['pos']=='abbrev': 
            final_restructuring.append((lemma,4))
        elif features['pos']=='prep':
            final_restructuring.append((word[0],0))             
        else:
           final_restructuring.append((lemma,0))
        counter+=1
                
                           
                
  
    print(final_restructuring)
    
    textChecker(final_restructuring ,sock)

 



            
    
    
    
#filteringCopoundWord(['صفاء', 'السلام', 'عليكم','عشاء', 'ورحمة', 'الله', 'وبركاته', 'كيف حالك', 'نهنى', 'صباح', 'الخير', 'السلام', 'عليكم'])