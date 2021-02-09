import nltk

from WordsClass import Words


def wordTokenize(text):
        word_list = nltk.word_tokenize(text)
        
        classifyText(word_list)
        
        
        
def classifyText(word_list):
  
    classified_word_list=[]
    compound_word_file = open('compound word.txt', 'r', encoding="utf8",)
    
        for line in compound_word_file :
            if line.strip() in word_list: 
                classified_word_list.append(Words(word,1))
                break
        classified_word_list.append(Words(word,0))
    print(classified_word_list[0].word_type)      

classifyText("السلام عليكم سوف نقرأ الكتب كيف حالك")   
   
   

        
        