from RestructureToArSL import filteringCopoundWord
from camel_tools.disambig.mle import MLEDisambiguator
from camel_tools.tokenizers.word import simple_word_tokenize
from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer



sentence= ['ألف', 'الحنون']

  
    # Load a pre-trained Maximum Likelihood Estimation model (MLE) disambiguator provided with CAMeL Tools.
mle = MLEDisambiguator.pretrained()
    
 # diacritize all words of sentence.
 
disambig = mle.disambiguate(sentence)
diacritized = [d.analyses[0].analysis['diac'] for d in disambig]


    
morophological_result = []

db = MorphologyDB.builtin_db()


# Create analyzer with no backoff

analyzer = Analyzer(db)


 

index_of_word = 0

# To analyze a word, we can use the analyze() method

for word in sentence:

    list_of_solutions = analyzer.analyze(word)

    for dictionary_of_solution in list_of_solutions:
    
        if dictionary_of_solution['diac'] == diacritized[index_of_word]:
        
            index_of_word = index_of_word + 1
            
            morophological_result.append(dictionary_of_solution)
            
            break

 

 

print( morophological_result)