
from RestructureToArSL import restructureText
from camel_tools.disambig.mle import MLEDisambiguator
#from camel_tools.tokenizers.word import simple_word_tokenize


# function for tokenize text to word 
# parameter: text that received from speech 
#def  tokenizeText(text,text_with_marks ,sock):

#    tokenized_text= simple_word_tokenize(text)
    
#    extractMorphologicalFeatures(tokenized_text,sock )
    
# fuction for extract morphological features for each word
# parameter: tokenized_text 
def extractMorphFeatures(text,text_with_marks,sock):
    # Load a pre-trained Maximum Likelihood Estimation model (MLE) disambiguator provided with CAMeL Tools.
    
    mle = MLEDisambiguator.pretrained()
    
    # diacritize all words of sentence.
    max_likelihood_solutions = mle.disambiguate(text)


    # assign morophlogical features of each word in list 
    moropholgical_result = [features_of_word.analyses[0].analysis for features_of_word in max_likelihood_solutions]
    print(moropholgical_result)
    
    restructureText(text_with_marks,moropholgical_result,sock)
    


