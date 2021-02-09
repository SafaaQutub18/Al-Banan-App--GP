
import re

compound_word_file = open('compound word.txt', 'r', encoding="utf8",)

fullstring = "صفاء السلام عليكم ورحمة الله وبركاته نهنى صباح الخير السلام عليكم"

compound_word_indexes=[]

for line in compound_word_file :
    for m in re.finditer(line.strip() , fullstring):
        if line.strip()=='':
            break
        compound_word_indexes.append(m.span())
        
        
list_classified_text=[]
word_index=0
out=0 
x=(0,0)  
 
for word in fullstring.split():
    out=0
    word_index += len(word)
    print(word_index)
    if word_index in range(x[0],x[1]) :
        continue
    for tuble in compound_word_indexes:
        if word_index in range(tuble[0], tuble[1]):
            list_classified_text.append(fullstring[tuble[0]:tuble[1]])
            x = tuble
            out= 1 ; break
    if out == 1: 
        continue 
    else: 
        list_classified_text.append(word) 

        
    
print(list_classified_text)
    #list_classified_text.append(Words(word,0))  

#start_end

#start_index= re.findall(substring, fullstring)

    
#print(start_index)
