
from RestructureToArSL import filteringText
from camel_tools.disambig.mle import MLEDisambiguator
from camel_tools.tokenizers.word import simple_word_tokenize


def  tokenizeText(text ,sock):
    print(text)

    tokenized_text= simple_word_tokenize(text)
    extractMorphologicalFeatures(tokenized_text,sock )
    
    
def extractMorphologicalFeatures(tokenized_text,sock):
    # Load a pre-trained Maximum Likelihood Estimation model (MLE) disambiguator provided with CAMeL Tools.
    mle = MLEDisambiguator.pretrained()
    
    # diacritize all words of sentence.
    max_likelihood_solutions = mle.disambiguate(tokenized_text)
    #print(max_likelihood_solutions)
    
    # get morophlogical features of each word
    moropholgical_result = [features_of_word.analyses[0].analysis for features_of_word in max_likelihood_solutions]
    print('-----------------------------------------')
    filteringText(tokenized_text,moropholgical_result,sock)
    


