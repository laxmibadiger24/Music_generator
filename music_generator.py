from music21 import stream, note
import random

music = stream.Stream()

notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

for i in range(20):
    n = random.choice(notes)
    music.append(note.Note(n))

music.write('midi', fp='generated_music.mid')

print("Music generated successfully!")