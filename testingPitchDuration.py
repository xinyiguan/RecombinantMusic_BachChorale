import music21 as m21
import Modules as m
import itertools
import functools
import numpy as np

#___________________________________________________________
def _ChordsinScore(score):
    return score.chordify().flat.getElementsByClass('Chord')

def _ChordsAsPitchesInScore(score):
    return [x.pitches for x in _ChordsinScore(score)]

def ChordsAsPitchNamesAndDurationsInScore(score):
    pitchnames = [[x.nameWithOctave for x in c] for c in _ChordsAsPitchesInScore(score)]
    durations = [[x.duration.quarterLength] for x in _ChordsinScore(score)]
    return list(map(lambda pitchnames,durations:[pitchnames]+[durations], pitchnames, durations))

#___________________________________________________________

def Indices(searchspace, list_of_checkingelements):
    return [x for x in range(len(searchspace)) if searchspace[x:x+len(list_of_checkingelements)] == list_of_checkingelements]

#___________________________________________________________
def _CombineChordList2(list1,list2):
    return list(list1)+list([[]+[]])+list(list2)

def CombineChordLists(list_of_chordlist):
    return functools.reduce(_CombineChordList2,list_of_chordlist)

#___________________________________________________________
#testing field:
test_scores = list(m21.corpus.chorales.Iterator(1,100))


test_scores_transposed = [m.ScoreAbstraction.TransposeToCIndividual(x) for x in test_scores]


test_Chordlist = CombineChordLists([ChordsAsPitchNamesAndDurationsInScore(x) for x in test_scores_transposed])
len(test_Chordlist)
uniquechords = list(np.unique(test_Chordlist))
len(uniquechords)


# [x for x in uniquechords if test_Chordlist.count(x)>3]
# np.unique(test_Chordlist, return_inverse = True)[0].shape

markov_result = m.Markov_v2.Markov_model(test_Chordlist,36)



def GeneratedStream(markov_result):
    generated_stream = m21.stream.Stream()
    generated_stream.append([m21.chord.Chord(x[0],quarterLength=x[1][0]) for x in markov_result])
    return generated_stream

gen_seq = GeneratedStream(markov_result)

gen_seq.show()

mf = m21.midi.translate.streamToMidiFile(gen_seq)


mf.open('./byChordDSample4.mid', 'wb')
mf.write()
mf.close()


#check duration:
[x.duration for x in generated_stream]
