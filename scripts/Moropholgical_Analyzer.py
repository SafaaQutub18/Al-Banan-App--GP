from camel_tools.disambig.mle import MLEDisambiguator

# Load a pre-trained Maximum Likelihood Estimation model (MLE) disambiguator provided with CAMeL Tools.
mle = MLEDisambiguator.pretrained()

sentence = ['سوف', 'نقرأ', 'الكتب']

# diacritize all words of sentence.
max_likelihood_solutions = mle.disambiguate(sentence)

# get morophlogical features of each word
moropholgical_result = [features_of_word.analyses[0].analysis for features_of_word in max_likelihood_solutions]
