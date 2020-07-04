import numpy as np


def count_sub_list(subsequence,sequence):
    matches = []
    for i in range(len(sequence)):
        if sequence[i] == subsequence[0] and sequence[i:i+len(subsequence)] == subsequence:
            matches.append(subsequence)
    return len(matches)


def removeDuplicates(sequence):
    seen = set()
    seen_add = seen.add
    return [x for x in sequence if not (x in seen or seen_add(x))]


# main function
def getTransitionMatrix(sequence):
    S = np.array(sequence)
    letter = removeDuplicates(sequence)
    countMatrix = np.zeros((len(letter),len(letter)))
    transitionMatrix = np.zeros((len(letter),len(letter)))
    for i in range (len(letter)):
        for j in range (len(letter)):
            countMatrix[i][j] = count_sub_list([letter[i],letter[j]],sequence)

    for i in range (len(letter)):
        for j in range (len(letter)):
            if countMatrix.sum(axis=1)[i] != 0:
                transitionMatrix[i][j]=countMatrix[i][j]/countMatrix.sum(axis=1)[i];
            else :
                transitionMatrix[i][j]=0

    return transitionMatrix,letter,countMatrix

def getTransitionMatrixOnly(sequence):
    S = np.array(sequence)
    letter = removeDuplicates(sequence)
    countMatrix = np.zeros((len(letter),len(letter)))
    transitionMatrix = np.zeros((len(letter),len(letter)))
    for i in range (len(letter)):
        for j in range (len(letter)):
            countMatrix[i][j] = count_sub_list([letter[i],letter[j]],sequence)

    for i in range (len(letter)):
        for j in range (len(letter)):
            if countMatrix.sum(axis=1)[i] != 0:
                transitionMatrix[i][j]=countMatrix[i][j]/countMatrix.sum(axis=1)[i];
            else :
                transitionMatrix[i][j]=0
    mat = np.matrix(transitionMatrix)
    return mat

def markov(transitionMatrix, initialState, generation, letter):
    P = transitionMatrix
    x = initialState
    n = generation
    recordState = [0]*n
    for i in range(n):
        if np.sum(x) != 0:
            recordedindex=(np.random.choice(range(len(letter)),1,p=x)[0])
            recordState[i]=letter[recordedindex]
            x = np.matmul(x,P)
        else:
            recordState[i]="stopped"
            x = np.matmul(x,P)
    return recordState


def Markov_model(sequence,generation,initialState=None):
    transitionMatrix = getTransitionMatrix(sequence)[0]
    letter = getTransitionMatrix(sequence)[1]
    I = np.zeros(len(letter))

    if initialState == None:
        randomIndex = np.random.choice(range(len(letter)))
        I[randomIndex]=1
    else:
        I[initialState]=1

    generatedSequence = markov(transitionMatrix,I,generation,letter)

    return generatedSequence
