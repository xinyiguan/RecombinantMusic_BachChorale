# A Probabilistic Model for Recombinant Music

This project presents a simple implementation of David Cope’s *recombinancy* approach towards composition.

#### Project summary:

Markov model

Specific Style: Bach Chorales

Language used: Python

Libraries Dependency: (in Python) music21, numpy

### Data Processing: 

##### 1. Transposition 

Using music21’s most accessible built-in Bach chorale corpus and its various functionality, 
I transposed the chorales into either C Major or A minor according into their original keys. 

##### 2. Extracting the unit in music
 I have tried two different methods. One is the chord as the unit, looking at the chord progression in a local chord-to-chord level, 
 and the other is the beat as the unit at the beat-to-beat, as David Cope proposed in his book. 
 I have also preprocessed the scores using music21 “chordify” tool, which compresses every note in the four parts of a chorale into a single chord.

###### 2.1 The Chord as the Unit
###### 2.2 The Beat as the Unit

##### 3. Combining units
With the units prepared in the previous section, I now have to combine all units into one large list of data as an input for the Markov Chain.

### Markov Chain
The Markov model in this project is built from scratch using only the NumPy library in python. 
I have tried two approaches of constructing the transition matrix. For implementation details, see scripts ```Markov.py``` and ```Markov_v2.py```. 