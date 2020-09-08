#attempt at algorithmically generating music


#midi note definition
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


#Midi Message Generators

def NoteOn(note, channel=0, velocity=96):
    status="1000"+GetBin(channel,4)
    D1="0"+GetBin(note,7)
    D2="0"+GetBin(velocity,7)
    return status+D1+D2

def NoteOff(note, channel=0, velocity=96):
    status="1001"+GetBin(channel,4)
    D1="0"+GetBin(note,7)
    D2="0"+GetBin(velocity,7)
    return status+D1+D2




#Utility Commands

def GetBin(Interger, Length=8):
    return str(bin(Interger))[2:].zfill(Length)

def GetHex(String, Base=2):
    return hex(int(String, base=Base))
