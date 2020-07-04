import music21 as m21




def TransposeToCIndividual(score):
    key = score.analyze('key')
    if key.type == 'major':
        I = m21.interval.Interval(key.tonic, m21.pitch.Pitch('C'))
    elif key.type == 'minor':
        I = m21.interval.Interval(key.tonic, m21.pitch.Pitch('A'))
    return score.transpose(I)
