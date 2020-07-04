import music21
import numpy
def F(f,X):

    return [f(x)for x in X]

# retrieve by chords
def ChordsinScore(score):
    return score.chordify().flat.getElementsByClass('Chord')

def ChordsinScores(scores):
    return F(ChordsinScore, scores)

# retrieve by beat:

def GroupChordByBeatInMeasure(measure):
    measure = measure.getElementsByClass('Chord')
    total_beat = int(max(map(lambda chord: chord.beat,measure)))
    chord_by_beat = [[] for x in range(total_beat)]
    for i in range(len(measure)):
        chord_by_beat[int(measure[i].beat)-1].append(measure[i])
    return list(map(tuple,chord_by_beat))

def GroupChordByBeatInScore(score):
    measures = score.chordify().getElementsByClass('Measure')
    measurelist = F(GroupChordByBeatInMeasure,measures)
    flattened_measures = [y for x in measurelist for y in x]
    return flattened_measures

def GroupChordByBeatFromScores(scores):
    scorelist = F(GroupChordByBeatInScore, scores)
    flattened_scorelist = [y for x in scorelist for y in x] #tuplize each chord to feed in mk chain
    return flattened_scorelist
