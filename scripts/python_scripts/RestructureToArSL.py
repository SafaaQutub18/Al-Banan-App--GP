from SearchInDictionary import checkText
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
    numbers = [('واحد',1), ('اثنين',2),('ثلاثة',3),('اربعة', 4),('خمسة', 5),('ستة', 6),('سبعة',7),('ثمانية', 8),('تسعة',9),('عشرة',10)
,('صفر',0), ('اثنان',2),('ثلاث',3),('اربع', 4),('خمس', 5),('ست', 6),('سبع',7),('ثمان', 8),('تسع',9),('عشر',10)]
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
        
        for num in numbers:
            if tokenized_text[counter] == num[0]:
               moropholgical_result[counter]['lex'] = str(num[1])
               moropholgical_result[counter]['pos'] = 'digit'
               tokenized_text[counter] = str(num[1])
               break
        
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
                    continue
        
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
    restructured_text =[]
    
    # loop through all the words to produce final restructuring result
    for word in filtering_result: 
        
        # skip the compound word
        if word[1]==1:
            restructured_text.append(word)
            counter+=1
            continue
        
        features= moropholgical_result[counter]
        # filter the lemam to delete extra character 
        lemma=  re.sub("[^أ-ي ٱآ]","",features['lex']) 
        if (re.sub("[^ك+_]","",features['atbtok'])) == 'ك+_' :
            restructured_text.append(("مثل",0))
         
        # check if the POS equals noun or adj to add appropriate word depend on the features and cases  
        if  features['pos']== 'noun' or features['pos']== 'adj' or features['pos']== 'pron_dem':
            if features['num']== 's': # s= singler
                 if features['gen']== 'f' and lemma != word[0] and features['rat']=='r' or features['rat']=='y': # r = rational
                        restructured_text.append((lemma,0))
                        restructured_text.append(("أنثى",0))
                        
                 else: # else if gen = male
                      restructured_text.append((lemma,0))

    
   # ********************************************************

            elif features['num']== 'd': # d= dual
                if features['gen']== 'f' and re.search( 'ة', lemma ) == None and features['rat']=='r' or features['rat']=='y': # r = rational 
                      
                      restructured_text.append((lemma,0))
                      restructured_text.append(("2",2))
                      restructured_text.append(("أنثى",0))
                      
                else:  # else if gen = male
                    restructured_text.append((lemma,0))
                    restructured_text.append(("2",2))
            # ********************************************************

            elif features['num']== 'p': # p = plural
                if features['gen']== 'f' and re.search( 'ة', lemma ) == None and features['rat']=='r' or features['rat']=='y':  # r = rational
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
            #chexk if the verb start with 'سـ' letter to distinguish between the presen and future
               if features['prc1']!= 'sa_fut': #sa_fut = 'سـ' future letter
                  restructured_text.append((lemma,2))
               else:
                  restructured_text.append((lemma,2))
                  restructured_text.append(("قريب",0))
            else:
                  restructured_text.append((lemma,2))
                            
        #check for Interrogative names (أسماء الاستفهام)                
        elif features['pos']=='adv_rel' or features['pos']=='pron_rel' or features['pos']=='adv_interrog' or features['pos']=='pron_interrog' or features['pos']=='part_interrog' :
            restructured_text.append(("استفهام",0))
            restructured_text.append((lemma,0))
                
        elif features['pos']=='digit': 
            restructured_text.append((re.sub("[^0-9]","",word[0]),3))            
            #check for the arabic letters
        elif features['pos']=='abbrev': 
            restructured_text.append((lemma,4))
        elif features['pos']=='prep':
            restructured_text.append((word[0],0))             
        else:
           restructured_text.append((lemma,0))
        counter+=1
                
                           
                
  
    print(restructured_text)
    
    checkText(restructured_text ,sock)

 



            
    
    
    
#filteringCopoundWord(['صفاء', 'السلام', 'عليكم','عشاء', 'ورحمة', 'الله', 'وبركاته', 'كيف حالك', 'نهنى', 'صباح', 'الخير', 'السلام', 'عليكم'])