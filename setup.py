import cx_Freeze
import os  


audiofiles = ['src/audio/']
spritefiles = ['src/sprites/']
codefiles = ['src/game_modules']
'''
for dirname, dirnames, filenames in os.walk(''):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        audiofiles.append(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        audiofiles.append(os.path.join(dirname, filename))

'''

allfiles = audiofiles + spritefiles + codefiles

executables = [cx_Freeze.Executable("src/game.py")]

cx_Freeze.setup(name="Sword'N'Jump", options={"build_exe": {"packages":["pygame"],"include_files":allfiles}}, executables = executables)
