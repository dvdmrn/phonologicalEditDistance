# Phonological Edit Distance
This uses the mighty power of [Phonological Corpus Tools](http://phonologicalcorpustools.github.io/CorpusTools/) to calculate the average phonological edit distance of all items in a set. This can be used as a proxy measure of phonological dissimilarity.

### Dependencies:
To run this you must have:  
* [Python 3](https://www.python.org/download/releases/3.0/)  
* [Phonological Corpus Tools](http://phonologicalcorpustools.github.io/CorpusTools/)  
* [numpy](http://www.numpy.org/)  
    
------------------------------------------------------------

### About:  
The (Levenshtein) edit distance is the number of operations (i.e. add, delete, replace) needed to change one string to another. For example 'bat'->'pat' has an edit distance of 1. But some changes may more phonologically different than others. For example, 'bat'->'rat' differs in more phonological features than 'bat'->'pat'. The phonological edit distance takes the levenshtein edit distance and weights it based off the difference in phonological features. More info can be found [here](http://corpustools.readthedocs.io/en/latest/string_similarity.html#phonological-edit-distance)

### How to use:  

Right now there's no pretty input or output methods because I'm lazy, but if you feel like adding them in let me know. With that out of the way...  
`phonoEditDistanceWITHINsubjects.py` compares a set of words to itself, and `phonoEditDistanceBETWEENsubjects.py` compares a set of words to another set of words.

Using `phonoEditDistanceWITHINsubjects.py`:  
* Replace "myCorpus.csv" with the corpus of your choice. (Note: make sure it's [formatted properly](http://corpustools.readthedocs.io/en/latest/loading_corpora.html))  
* Open a terminal window and type `sudo python3 phonoEditDistanceWITHINsubjects.py`. (Note: may not need sudo, or to specify python3 if it's the only version you have installed).  

Using `phonoEditDistanceWITHINsubjects.py`:  
* Replace "corpusA.csv" and "corpusB.csv" with the corpora you wish to compare.
* Open a terminal window and type `sudo python3 phonoEditDistanceBETWEENsubjects.py`. (Note: may not need sudo, or to specify python3 if it's the only version you have installed).
