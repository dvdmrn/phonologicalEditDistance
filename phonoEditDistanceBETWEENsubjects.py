from corpustools.corpus import io
from corpustools.symbolsim import phono_edit_distance
import numpy
import itertools


#compares the phonological similarity of two corpuses

#replace 'corpusA.csv' and 'corpusB.csv' with the corpuses (corpora?) you wish to compare.

myCorpus = io.csv.load_corpus_csv(
	"corpusA", 
	"corpusA.csv", 
	",", 
	".", 
	annotation_types=None, 
	feature_system_path=None, 
	stop_check=None, 
	call_back=None)

everythingElse = io.csv.load_corpus_csv(
	"corpusB", 
	"corpusB.csv", 
	",", 
	".", 
	annotation_types=None, 
	feature_system_path=None, 
	stop_check=None, 
	call_back=None)



print ("loaded? Loaded.",myCorpus)
io.binary.download_binary("ipa2hayes", "/matrix", call_back=None)

ipa2hayes = io.binary.load_binary("/matrix")
io.binary.save_binary(ipa2hayes, "/matrix")
print("did it load?",ipa2hayes.features)

giantPhonoSimList = []

for word in myCorpus.wordlist:
	for compareWord in everythingElse.wordlist:

		phonoEditDistance = phono_edit_distance.phono_edit_distance(
				myCorpus.wordlist.get(word),
				everythingElse.wordlist.get(compareWord),
				"transcription",
				io.binary.load_binary("/matrix")
				)
		print("comparing giant phono sim list!!: ",
				myCorpus.wordlist.get(word).transcription,
				" to: ",
				everythingElse.wordlist.get(compareWord).transcription, 
				": ", 
				phonoEditDistance
				)
		giantPhonoSimList.append(phonoEditDistance)

print("giant phonoSimList: ",giantPhonoSimList)

print("mean result: ", numpy.mean(giantPhonoSimList))

