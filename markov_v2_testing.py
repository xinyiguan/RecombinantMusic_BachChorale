import numpy as np


a = np.array([1,2,5,6,5,6,5,6,1,2,8,7,8,7,8,7,9])
b = np.array(['1','2','1','5','11'])


def _NextElements(sequence,x):
    cropped_sequence = sequence[0:-1]
    position_of_x_not_last = np.where(cropped_sequence == x)[0]
    next_elements = sequence[position_of_x_not_last + 1]
    return next_elements

def _TransitionMatrix_row(sequence,i):
    alphabet = np.unique(sequence)
    next_elements = _NextElements(sequence,alphabet[i])
    i_th_row_count = np.histogram(next_elements,np.concatenate((alphabet,np.array([alphabet[-1]+1]))))[0]
    if i_th_row_count.sum()!=0:
        i_th_row_normalized = i_th_row_count/i_th_row_count.sum()
    if i_th_row_count.sum()==0:
        i_th_row_normalized = i_th_row_count
    return i_th_row_normalized

def TransitionMatrix(sequence):
    alphabet,encoded_sequence = np.unique(np.array(sequence),return_inverse = True) #reconstruct the original sequence using indices
    transition_matrix = np.array([_TransitionMatrix_row(encoded_sequence,i) for i in range(len(alphabet))])
    return transition_matrix,alphabet





_NextElements(a,9)
alphabet = np.unique(a)
i_th_row_count = np.histogram(next_elements,np.concatenate((alphabet,np.array([alphabet[-1]+1]))))[0]
i_th_row_count
i_th_row_count.sum()
_TransitionMatrix_row(a,)

alphabet,encoded_sequence = np.unique(np.array(a),return_inverse = True)
alphabet
encoded_sequence

alphabet[encoded_sequence]
TransitionMatrix(a)

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
    transitionMatrix = TransitionMatrix(sequence)[0]
    letter = TransitionMatrix(sequence)[1]
    I = np.zeros(len(letter))

    if initialState == None:
        randomIndex = np.random.choice(range(len(letter)))
        I[randomIndex]=1
    else:
        I[initialState]=1

    generatedSequence = markov(transitionMatrix,I,generation,letter)

    return generatedSequence
















Markov_model([1,2,3],7)
