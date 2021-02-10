

# filtering the compound word and word in text. 
# parameter: the tokenized_text: which contains the list of word.
#            the morphological_result: which contains the analyzed feature that extracted from the words.

def filteringCopoundWord(tokenized_text,moropholgical_result):
    # read the compound word file 
    compound_word_file = open('compound word.txt', 'r', encoding="utf8",) 
    
    filtering_result = [] 
    counter = 0
    temp_compound_word=[]
    
    # loop through the text word by word
    while counter < len(tokenized_text):
        
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
                temp_compound_word=[]
                continue
            else: 
                filtering_result.append(" ".join(temp_compound_word))
                temp_compound_word=[]
        else: 
            filtering_result.append(tokenized_text[counter])
            counter+=1
            
    print(filtering_result)        
        
            
    
    
#filteringCopoundWord(['صفاء', 'السلام', 'عليكم','عشاء', 'ورحمة', 'الله', 'وبركاته', 'كيف حالك', 'نهنى', 'صباح', 'الخير', 'السلام', 'عليكم'])