#midi note definition
#alligned so that c[0] will return the MIDI note number for C[0]
#C[-1] will pull the last item in the list, matching standard MIDI
#terminology
C  = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 0]
Db = [13, 25, 37, 49, 61, 73, 85, 97, 109, 121, 1]
D  = [14, 26, 38, 50, 62, 74, 86, 98, 110, 122, 2]
Eb = [15, 27, 39, 51, 63, 75, 87, 99, 111, 123, 3]
E  = [16, 28, 40, 52, 64, 76, 88, 100, 112, 124, 4]
F  = [17, 29, 41, 53, 65, 77, 89, 101, 113, 125, 5]
Gb = [18, 30, 42, 54, 66, 78, 90, 102, 114, 126, 6]
G  = [19, 31, 43, 55, 67, 79, 91, 103, 115, 127, 7]
Ab = [20, 32, 44, 56, 68, 80, 92, 104, 116, 128, 8]
A  = [21, 33, 45, 57, 69, 81, 93, 105, 117, 129, 9]
Bb = [22, 34, 46, 58, 70, 82, 94, 106, 118, 130, 10]
B  = [23, 35, 47, 59, 71, 83, 95, 107, 119, 131, 11]

#Other variable definitions

Mtrk=1297379947 #int representation of tag that indicates a new track


#Midi Message Generators

def NoteOn(note, channel=0, velocity=96):
    #velocity of 96 is a standard in at least one DAW I looked up
    status="1000"+GetBin(channel,4)
    D1="0"+GetBin(note,7)
    D2="0"+GetBin(velocity,7)
    return status+D1+D2

def NoteOff(note, channel=0, velocity=96):
    #Similar to NoteOn
    status="1001"+GetBin(channel,4)
    D1="0"+GetBin(note,7)
    D2="0"+GetBin(velocity,7)
    return status+D1+D2

def AfterTouch(note, channel=0, pressure=0):
    #key pressure/aftertouch, for a single note
    status="1010"+GetBin(channel,4)
    D1="0"+GetBin(note,7)
    D2="0"+GetBin(pressure,7)
    return status+D1+D2

def PitchBend(LSB, MSB, channel=0):
    #Pitchbend affects all currently active notes on a channel (I think)
    #LSB and MSB are both 8 bit numbers, with one bit on each used for flags
    #ie its a 14bit number. 
    status="1010"+GetBin(channel,4)
    D1="0"+GetBin(LSB,7)
    D2="0"+GetBin(MSB,7)
    return status+D1+D2

    
def MIDIHeadder(MIDIformat=1, NumberOfTracks=1):
    #Generates the headder of the midi file
    #format can be 0, 1 or 2
    #0 is a single track
    #1 is multiple tracks
    #2 is multiple tracks, but not necissarily played simultaneously
    #NumberOfTracks must be at least one, but can be much larger
    MThd="4D546864" #similar to Mtrk above
    HeadderLength="00000006"
    MFormat = str(MIDIformat).zfill(4) #this creates a hex value
    tracks = str(hex(NumberOfTracks)).zfill(4)



#Utility Commands

def GetBin(Interger, Length=8):
    #takes an ingerger, converts it to binary (type)
    #then converts that to a string, strips off the leading
    #0b and pads out the result with zeros so it is of length Length.
    return str(bin(Interger))[2:].zfill(Length)

def GetHex(String, Base=2):
    #Converts a string that represents a binary number (ie the output of GetBin)
    #to an actual hex output
    return hex(int(String, base=Base))
