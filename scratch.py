import music21 as m21
import Modules as m
from Modules.helperfuncs import F
from Modules.helperfuncs import compose
import itertools
import functools
import numpy as np


def _Index(searchspace, x):
    index_number = []
    for i in range(len(searchspace)):
        if searchspace[i] == x:
            index_number.append(i)
    return index_number

def IndexOfEachElementInASequence(searchspace, list_of_elements):
    return [_Index(searchspace, x) for x in list_of_elements ]


a=np.array([1,3,6,0,0,3,6,6,7,0,0,1,3,7,0,2,3,1,1,6,6,7])
pattern=np.array([3,6])

s = m21.corpus.parse('bwv66.6')
s.show()
s.show('midi')
key = s.analyze('key')
key
key.tonalCertainty()
key.alternateInterpretations[0].correlationCoefficient
key.alternateInterpretations[0]
