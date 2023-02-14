from setuptools import setup
#from ez_setup import use_setuptools

#use_setuptools()

APP=['catanDiceRoller.py']
DATA_FILES = ['catanlogo.jpg',
              'diceroll1.mp3',
              'diceroll2.mp3',
              'diceroll3.mp3',
              'diceroll4.mp3',
              'dicerollerbg960.png',
              'eventBARBSHIP2d.png',
              'eventBLUE2d.png',
              'eventGREEN2d.png',
              'eventYELLOW2d.png',
              'red1.png',
              'red2.png',
              'red3.png',
              'red4.png',
              'red5.png',
              'red6.png',
              'rollbutton.png',
              'rollbuttonHOVER.png',
              'yellow1.png',
              'yellow2.png',
              'yellow3.png',
              'yellow4.png',
              'yellow5.png',
              'yellow6.png',]
OPTIONS={
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
