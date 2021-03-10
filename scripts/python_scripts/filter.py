import re


text= "الخير السلام عليكم ورحمة الله وبركاته السلام عليكم كيف الحال كيف حالك روعة صباح الخير مندي الخير مساء"

#def filteringText(text,tokenized_text,moropholgical_result,sock):
def filteringText(text):
    
      # read the compound word file 
    compound_words_file = open('compound word.txt', 'r', encoding="utf8",) 
    
    # declare the  prepositions, relative pronouns, punctuation marks, numbers
   
    asma_mosola = ["الذي" , "التي" , "اللذان" , "اللتان" , "الذين" , "اللتان" ,  "اللاتي" ,  "اللواتي" ,  "اللائي"]
    punctuation_marks = ["." , ":" ,  "،", "؟"]
    numbers = [('واحد',1), ('اثنين',2),('ثلاثة',3),('اربعة', 4),('خمسة', 5),('ستة', 6),('سبعة',7),('ثمانية', 8),('تسعة',9),('عشرة',10)
,('صفر',0), ('اثنان',2),('ثلاث',3),('اربع', 4),('خمس', 5),('ست', 6),('سبع',7),('ثمان', 8),('تسع',9),('عشر',10)]
    
    # list for the indexes of compword
    compWord_indexes=[]
    
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
                 print(text[counter])
                 temp_words+=(text[counter]) #collect the character of evry word
                 
         else:
             filtering_result.append((temp_words, 0))  
             temp_words=""
         counter+=1
             
             
    if temp_words!="":
        filtering_result.append((temp_words, 0)) 
        
        
       
        
        
        
       
        
      
    print(filtering_result)    
        
        
        
filteringText(text)