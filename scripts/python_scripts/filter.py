import re


text= "الخير السلام عليكم ورحمة الله وبركاته وردة ذهبت الى ورحمة الله الخير صباح السلام عليكم ورحمة"
moro = [1, 2, 3, 4, 5 , 6, 7 ,8 ,9 ,10 ,11 , 12, 13,14 ,15, 16]
#def filteringText(text,tokenized_text,moropholgical_result,sock):
def filteringText(text,moropholgical_result):
    
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
        
    #--------------------------------------------------------------------------------------------------------------------    
        
    deleted_index_num = 0 
    counter = 0
    while counter < len(filtering_result):
        
        word = filtering_result[counter]
        
        if word[1] == 0:
            
            if word[0] in asma_mosola or word[0] in punctuation_marks or moropholgical_result[counter]['pos'] =='prep':
                del moropholgical_result[counter]
                del filtering_result[counter]
            
            #******************************************
                
            for num in numbers:
                 if word[0] == num[0]:
                        moropholgical_result[counter]['lex'] = str(num[1])
                        moropholgical_result[counter]['pos'] = 'digit'
                        word[0] = str(num[1])
                        break
            counter+=1
            continue
        else:
            deleted_index_num = len(word[0].split())-1
            print(deleted_index_num)
            shift_index = 0
            for index in range(counter ,counter+deleted_index_num):
                del moropholgical_result[index - shift_index]
                shift_index += 1
            counter +=1
        
        
        
       
        
    print(moropholgical_result) 
    print(filtering_result)    
        
        
        
filteringText(text, moro)