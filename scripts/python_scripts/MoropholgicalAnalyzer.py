
from RestructureToArSL import restructureText
from camel_tools.disambig.mle import MLEDisambiguator


# fuction for extract morphological features for each word
# parameter: text, text_with_marks
def extractMorphFeatures(text,text_with_marks,sock):

    # Load a pre-trained Maximum Likelihood Estimation model (MLE) disambiguator provided with CAMeL Tools.
    mle = MLEDisambiguator.pretrained()
    
    # diacritize all words of sentence.
    max_likelihood_solutions = mle.disambiguate(text)


    # assign morophlogical features of each word in list 
    moropholgical_result = [features_of_word.analyses[0].analysis for features_of_word in max_likelihood_solutions]
   
    print(moropholgical_result)
    restructureText(text_with_marks,moropholgical_result,sock)
    
    
    


