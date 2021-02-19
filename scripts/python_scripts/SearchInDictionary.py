
import csv
import pandas as pd

compoundWord_file = pd.read_csv('compoundWords_Dictionary.csv',delimiter='\t', )
letters_file = pd.read_csv('letters_Dictionary.csv',delimiter='\t' )
#digit_file = pd.read_csv('digit_Dictionary.csv', delimiter='\t' )
#words_file = pd.read_csv('words_Dictionary.csv',delimiter='\t' )

cw = pd.DataFrame(compoundWord_file)

#def textChecker(restructured_text):
    
    
    #for word in restructured_text:
    #    
    

for data in cw.items():
	print(data[])


