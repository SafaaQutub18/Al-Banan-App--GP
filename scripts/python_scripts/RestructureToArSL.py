
import re
# filtering the compound word and word in text. 
# parameter: the tokenized_text: which contains the list of word.
#            the morphological_result: which contains the analyzed feature that extracted from the words.

def filteringCopoundWord(tokenized_text,moropholgical_result):
    # read the compound word file 
    compound_word_file = open('compound word.txt', 'r', encoding="utf8",) 
    
    jarr_letters = ["من", "عن", "على",  "حتي", "حتى", "في","الي" , "الى", "إلي", "إلى"] 
    asma_mosola = ["الذي" , "التي" , "اللذان" , "اللتان" , "الذين" , "اللتان" ,  "اللاتي" ,  "اللواتي" ,  "اللائي"]
    filtering_result = [] 
    counter = 0
    temp_compound_word=[]
    delete_index = []
    
    # loop through the text word by word
    while counter < len(tokenized_text):
 
        if tokenized_text[counter] in asma_mosola or tokenized_text[counter] in jarr_letters:
            delete_index.append(counter)
            counter+=1
            continue
        
        # start from the beginning of file
        compound_word_file.seek(0)  
        
        # loop through the lines of file 
        for line in compound_word_file:
            
            # loop through the words of lines
            for word_in_line in line.split():
                
                # check if the word in file match with the word in "tokenized_text" list
                if word_in_line==tokenized_text[counter]:
                    #collect each word of the compound_word.
                    temp_compound_word.append(word_in_line) 
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
        if len(temp_compound_word) !=0:
            
            # special case for "السلام عليكم ورحمة الله وبركاته"
            if " ".join(temp_compound_word) == "ورحمة الله وبركاته":
                # add index with index of "ورحمة" before the index "الله وبركاته"
                delete_index.insert(len(delete_index)-2, counter-2)
                temp_compound_word=[]
                continue
            else: 
                filtering_result.append((" ".join(temp_compound_word), 1))
                temp_compound_word=[]
        else: 
            filtering_result.append((tokenized_text[counter], 0))
            counter+=1

    
    # each iteration increase shift_index by one
    shift_index = 0
    for index in delete_index:
        del moropholgical_result[index - shift_index]
        shift_index += 1
        
    
    print(moropholgical_result)
    restructureText(filtering_result,moropholgical_result)
        
    
    
    
 
 
    
def restructureText(filtering_result, moropholgical_result):
    
    # 
    counter=0
    while counter < len(filtering_result): 
        if moropholgical_result[counter]['pos']== 'verb':
            
            if moropholgical_result[counter+1]['pos']== 'noun' or moropholgical_result[counter+1]['pos']== 'noun_prop' :
                temp_moropholgical_result= moropholgical_result[counter]
                temp_filtering_result= filtering_result[counter]
                print(temp_filtering_result)
                
                moropholgical_result[counter]= moropholgical_result[counter+1]
                filtering_result[counter] = filtering_result[counter+1]
                
                
                moropholgical_result[counter+1]= temp_moropholgical_result
                filtering_result[counter+1] = temp_filtering_result
                
                counter+=2
                continue
            
        
        counter+=1
        continue
    
    
    # -------------------------------------------------------------------------------------
    
    counter=0
    final_restructuring =[]
    
    for word in filtering_result: 
        if word[1]==1:
            final_restructuring.append(word)
            counter+=1
            continue
        
        lemma= lex_filter(moropholgical_result[counter]['lex'])
        print(lemma)
        
        if  moropholgical_result[counter]['pos']== 'noun' or moropholgical_result[counter]['pos']== 'adj':
            if moropholgical_result[counter]['num']== 's':
                 if moropholgical_result[counter]['gen']== 'f' and lemma != word[0] and moropholgical_result[counter]['rat']=='r':
                        final_restructuring.append(word)
                        final_restructuring.append(("أنثى",0))
                        counter+=1
                 else: 
                      final_restructuring.append(word)
                      counter+=1
                      
            # ********************************************************
            else:
                if moropholgical_result[counter]['num']== 'd':
                      if moropholgical_result[counter]['gen']== 'f' and re.search( 'ة', lemma ) == None and moropholgical_result[counter]['rat']=='r':
                            
                            final_restructuring.append(word)
                            final_restructuring.append(("اثنان",0))
                            final_restructuring.append(("أنثى",0))
                            counter+=1
                      else: 
                          final_restructuring.append(word)
                          final_restructuring.append(("اثنان",0))
                          counter+=1
                # ********************************************************
                else:
                    if moropholgical_result[counter]['num']== 'p':
                          if moropholgical_result[counter]['gen']== 'f' and re.search( 'ة', lemma ) == None and moropholgical_result[counter]['rat']=='r':
                                
                                final_restructuring.append(word)
                                final_restructuring.append(("كثير",0))
                                final_restructuring.append(("أنثى",0))
                                counter+=1
                          else: 
                              final_restructuring.append(word)
                              final_restructuring.append(("كثير",0))
                              counter+=1
        
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    else: 
         if moropholgical_result[counter]['pos']== 'verb':
             
                 
        
                        
                     
                
    
    print(final_restructuring)
    
    

def lex_filter(lemma):
    return re.sub("[^أ-ي]","",lemma)
    

            
    
    
    
#filteringCopoundWord(['صفاء', 'السلام', 'عليكم','عشاء', 'ورحمة', 'الله', 'وبركاته', 'كيف حالك', 'نهنى', 'صباح', 'الخير', 'السلام', 'عليكم'])