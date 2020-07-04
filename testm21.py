import music21 as m21
import Modules as m
from Modules.helperfuncs import F
from Modules.helperfuncs import compose
import itertools
import functools
import numpy as np
import pandas as pd

#___________________________________________________________
def TransposeToCIndividual(score):
    key = score.analyze('key')
    if key.type == 'major':
        I = m21.interval.Interval(key.tonic, m21.pitch.Pitch('C'))
    elif key.type == 'minor':
        I = m21.interval.Interval(key.tonic, m21.pitch.Pitch('A'))
    return score.transpose(I)


#___________________________________________________________
# Retreive chords structure from scores
def _ChordsListinScore(score):
    transposed_score = TransposeToCIndividual(score)
    chordlist = transposed_score.chordify().flat.getElementsByClass('Chord')
    return list(chordlist)


def ChordListsFromScores(scores):
    chordlists = F(_ChordsListinScore, scores)
    flattened_chordlists = [y for x in chordlists for y in x]
    return flattened_chordlists

def MarkovReadyChordList(scores):
    return F(compose(tuple,lambda x:[x]),ChordListsFromScores(scores))

#___________________________________________________________
# Combine Chordlist to feed Markov
def _CombineChordList2(chordlist1,chordlist2):
    return list(chordlist1)+list(m21.chord.Chord([]))+list(chordlist2)

def CombineChordLists(list_of_chordlist):
    return functools.reduce(_CombineChordList2,list_of_chordlist)
#___________________________________________________________
#check location
def _Index(searchspace,x):
    index_number = []
    for i in range(len(searchspace)):
        if searchspace[i] == x:
            index_number.append(i)
    return index_number

def Indices(list, list_of_checkingelements):
    return [_Index(list,y) for y in list_of_checkingelements]



#___________________________________________________________
# testing area:

test_scores = list(m21.corpus.chorales.Iterator(1,100))

test_Chordlist=ChordListsFromScores(test_scores)

len(test_Chordlist)

uniquechords = list(np.unique(test_Chordlist))
len(uniquechords)


MarkovReadyChordListthing = MarkovReadyChordList(test_scores)

MarkovReadyChordListthing

m.Markov_v2.TransitionMatrix(testchordlists)

markov_result = m.Markov.Markov_model(testchordlists, 15)
markov_result



Indices(testchordlists, markov_result)
