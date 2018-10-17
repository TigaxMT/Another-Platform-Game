import cx_Freeze

audiofiles = ['src/audio/']
spritefiles = ['src/sprites/']
codefiles = ['src/game_modules']

allfiles = audiofiles + spritefiles + codefiles

executables = [cx_Freeze.Executable("src/game.py")]

cx_Freeze.setup(name="Sword'N'Jump", options={"build_exe": {"packages":["pygame"],"include_files":allfiles}}, executables = executables)
