from corpustools.corpus import io
from corpustools.symbolsim import phono_edit_distance
import numpy
import itertools

#---------------------------------------------------------------------//
#                                                                     //
# calculates the phonological edit distance of all words within a set //
#                                                                     //
#---------------------------------------------------------------------//


phonoSimList = []


#Load a corpus. replace 'myCorpus.csv' with the corpus of your choice.
#Ensure that the first 3 columns are headed by 'spelling','transcription', and 'frequency'.

myCorpus = io.csv.load_corpus_csv(
	"myCorpus", 
	"myCorpus.csv",
	",", 
	".", 
	annotation_types=None, 
	feature_system_path=None, 
	stop_check=None, 
	call_back=None)


print ("Loaded: ",myCorpus)

#downloads a Hayes feature matrix
io.binary.download_binary("ipa2hayes", "/matrix", call_back=None)

ipa2hayes = io.binary.load_binary("/matrix")
io.binary.save_binary(ipa2hayes, "/matrix")

print("Features: ",ipa2hayes.features)

#generate all unique combinations of 2 from the corpus
wordCombinations = itertools.combinations(myCorpus.wordlist,2)

#iterates through word combinations and calcuates the edit distance
for wordCombo in wordCombinations:
	print(wordCombo)
	phonoEditDistance = phono_edit_distance.phono_edit_distance(
				myCorpus.wordlist.get(wordCombo[0]),
				myCorpus.wordlist.get(wordCombo[1]),
				"transcription",
				io.binary.load_binary("/matrix")
				)
	print("comparing: ",
			myCorpus.wordlist.get(wordCombo[0]).transcription,
			" to: ",
			myCorpus.wordlist.get(wordCombo[1]).transcription, 
			": ", 
			phonoEditDistance
			)
	phonoSimList.append(phonoEditDistance)

#the mean result of all edit distances from the corpus
print("mean result: ", numpy.mean(phonoSimList))

