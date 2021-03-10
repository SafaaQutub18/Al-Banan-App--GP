import re


text= (['صباح','صفاء', 'السلام', 'عليكم', 'ورحمة', 'الله', 'صلى','وسلم', 'كيف', 'السلام', 'عليكم',''])

def filteringText(text,tokenized_text,moropholgical_result,sock):
    
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
    
    # counter of while loop 
    counter = 0


    
   
    # loop through the lines of file   
    for line in compound_words_file :
        for m in re.finditer(line.strip() , text):
            if line.strip()=='':
                break
            compWord_indexes.append(m.span())
    
   
    temp=""
    while counter < len(text):          
        if(text[counter] != " ") :
            temp+=(text[counter])
        else:
            if(temp!=""):
                filtering_result.append((temp, 0))  
                temp=""
        counter+=1
        
        for index in compWord_indexes:
            print(index[0])
            if index[0]== counter:
                filtering_result.append((text[index[0]:index[1]], 1))
                counter+= len(text[index[0]:index[1]])
                break
            
        if counter >= len(text): break
        
       
        
      
    print(filtering_result)    
        
        
        
