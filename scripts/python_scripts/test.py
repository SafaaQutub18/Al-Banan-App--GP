import re


tokenized_text= ['مساء','الله','الخير','السلام','عليكم']
compound_word_file = open('compound word.txt', 'r', encoding="utf8",) 
    
jarr_letters = ["من", "عن", "على",  "حتي", "حتى", "في","الي" , "الى", "إلي", "إلى"] 
asma_mosola = ["الذي" , "التي" , "اللذان" , "اللتان" , "الذين" , "اللتان" ,  "اللاتي" ,  "اللواتي" ,  "اللائي"]

filtering_result = [] 
counter = 0
counter2=0
temp_compound_word=[]
# delete_index = []

while counter < len(tokenized_text):
    
    # start from the beginning of file
        compound_word_file.seek(0) 
        
        for line in compound_word_file: 
            for word_in_line in line:
                if word_in_line == tokenized_text[counter]:
                    temp_compound_word=tokenized_text[counter]
                    counter+=1
                else: break
            
            
            
                
            
            