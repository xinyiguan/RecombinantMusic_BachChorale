import music21 as m21
import Modules as m
import itertools
import functools
import numpy as np


#___________________________________________________________
def _CombineChordList2(list1,list2):
    return list(list1)+list([ ])+list(list2)

def CombineChordLists(list_of_chordlist):
    return functools.reduce(_CombineChordList2,list_of_chordlist)


#___________________________________________________________
def FermataSegments(score):

    return fermata_seg

def GroupChordByBeatInMeasure(measure):
    measure = measure.getElementsByClass('Chord')
    total_beat = int(max(map(lambda chord: chord.beat,measure),default=0))
    pitchnames = [[x.nameWithOctave for x in c] for c in [x.pitches for x in measure]]
    durations = [[x.duration.quarterLength] for x in measure]
    measure_by_beat = list(map(lambda pitchnames,durations:[pitchnames]+[durations], pitchnames, durations))
    chord_by_beat = [[] for x in range(total_beat)]
    for i in range(len(measure)):
        chord_by_beat[int(measure[i].beat)-1].append(measure_by_beat[i])

    return list(chord_by_beat)

def GroupChordByBeatInScore(score):
    measures = score.chordify().getElementsByClass('Measure')
    measurelist = m.helperfuncs.F(GroupChordByBeatInMeasure,measures)
    flattened_measures = [y for x in measurelist for y in x]
    return flattened_measures


#___________________________________________________________
#testing field:

test_scores = m21.corpus.chorales.Iterator(1,10)
test_scores[6].show()

test_scores_transposed = [m.ScoreAbstraction.TransposeToCIndividual(x) for x in test_scores]

test_scores_transposed[1].show()
GroupChordByBeatInScore(test_scores_transposed[1])

test_Chordlist = CombineChordLists([GroupChordByBeatInScore(x) for x in test_scores_transposed])

markov_result = m.Markov_v2.Markov_model(test_Chordlist,100)
markov_result




def GeneratedStream(markov_result):
    generated_stream = m21.stream.Stream()
    for i in range(len(markov_result)):
        if len(markov_result[i])!=0:
            generated_stream.append([m21.chord.Chord(x[0],quarterLength=x[1][0]) for x in markov_result[i]])
        if len(markov_result[i])==0:
            generated_stream.append([m21.note.Rest(quarterLength=1.0)])
    return generated_stream

GeneratedStream(markov_result).show()







#check duration:
[x.duration for x in generated_stream]
