# MIDI
An Experiment in MIDI and procedural generation (maybe)

The main goal is to be able to take a well structured text file containing chord symbols (ie/ Cmaj) and convert them to a properly formatted MIDI file that can be played in any General MIDI compatable synthasizer.

This serves a secondary, more challanging goal, of a program that can take a chord file input and produce a musically meaningful output. 

Bits and pieces of these goals have been completed already by others. Tying these together, and filling in the missing pieces, is the goal of this project. 

Presently, I'm thinking of using something like a prime number encoding of MIDI notes to represent music. I do not quite know what purpose this will serve, or what use it will have, but it seems like fun to me.

##Goals
There exist tools to move between MIDI and MusicXML and other, related, ways of representing musical information on a computer. These are useful since software exists that can play the music and generate more traditional visual representations. The primary goal should therefore be to be able to convert from a string of intergers representing notes and chords and transform it into a more portable form (ie any format that can be converted freely between other music formats).

The other, more interesting, goal is to make tools to analyze and generate the strings of encoded intergers which can be translated into a playable format (goal 1).

##Prime Number Encoding
The prime encoding for the octave starting from Middle C is:

Letter Note | MIDI Number | Prime Encoding
------------ | ------------ | -------------
C	| 60	| 283
Db	| 61	| 293
D	| 62	| 307
Eb	| 63	| 311
F	| 64	| 313
Gb	| 65	| 317
G	| 66	| 331
Ab	| 67	| 337
A	| 68	| 347
Bb	| 69	| 349
Bb	| 70	| 353
B	| 71	| 359

This means that any particular collection of notes sounded at a single time has a unique representation, ie a C Major is C-F-Ab and is represented as the product of prime numbers 283, 313 and 337, the composite number 29851123.

Written in Python 3.7.9