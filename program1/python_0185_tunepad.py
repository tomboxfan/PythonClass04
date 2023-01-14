'''

step 1) Open https://tunepad.com

step 2) Register and Login (on the right top corner)

step 3) Create a new project

step 4) add cell(on the right side) -> keyboard


===================================================
keyboard
===================================================


------------------------------
Version 1
------------------------------

playNote(55, beats = 0.50)
playNote(52, beats = 0.50)
playNote(52, beats = 0.50)

playNote(53, beats = 0.50)
playNote(50, beats = 0.50)
playNote(50, beats = 0.50)

playNote(48, beats = 0.50)
playNote(50, beats = 0.50)
playNote(52, beats = 0.50)
playNote(53, beats = 0.50)
playNote(55, beats = 0.50)
playNote(55, beats = 0.50)
playNote(55, beats = 0.50)

rest(1)



------------------------------
Version 2 - I use while to let it play 3 times
------------------------------

i = 1

while i <= 3:

    playNote(55 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(52 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(52 + i * 2, beats = 0.50 + 0.25 * i)

    playNote(53 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(50 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(50 + i * 2, beats = 0.50 + 0.25 * i)

    playNote(48 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(50 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(52 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(53 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(55 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(55 + i * 2, beats = 0.50 + 0.25 * i)
    playNote(55 + i * 2, beats = 0.50 + 0.25 * i)

    rest(1)

    i += 1




===================================================
drum
===================================================


------------------------------
Version 1 - base version
------------------------------

playNote(2, beats = 0.25)
playNote(10, beats = 0.25)
playNote(3, beats = 0.25)
playNote(10, beats = 0.25)



------------------------------
Version 2 - I use while to let it play 3 times
------------------------------


i = 1

while i <= 3:

    playNote(2,  beats = 0.50 + 0.25 * i)
    playNote(10, beats = 0.50 + 0.25 * i)
    playNote(3,  beats = 0.50 + 0.25 * i)
    playNote(10, beats = 0.50 + 0.25 * i)

    playNote(2,  beats = 0.50 + 0.25 * i)
    playNote(10, beats = 0.50 + 0.25 * i)
    playNote(3,  beats = 0.50 + 0.25 * i)
    playNote(10, beats = 0.50 + 0.25 * i)

    playNote(2,  beats = 0.50 + 0.25 * i)
    playNote(10, beats = 0.50 + 0.25 * i)
    playNote(3,  beats = 0.50 + 0.25 * i)
    playNote(10, beats = 0.50 + 0.25 * i)

    playNote(5,  beats = 0.50 + 0.25 * i)

    rest(1)

    i += 1









Ctrl + F -> Find
Ctrl + R -> Find and Replace 

'''