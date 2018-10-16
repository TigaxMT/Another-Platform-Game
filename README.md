# Sword'N'Jump
A Platform Game written in Python with PyGame

# Demo Gif

* Sorry for the lag but my PC is very , very low. Probably in your's should run clear, if is not a 1.4GHz Dual core like mine :D

![Alt Text](https://github.com/TigaxMT/Another-Platform-Game/blob/master/APG.gif)

# Check List of things to do

- [x] Improve base_platform sprite movement;
- [x] Improve the platform collision;
- [x] Draw a better sprite player with a sword;
- [x] Draw the sprite player sword atack;
- [x] Add new sound effects for jump , walk , atack etc;
- [x] Add a new sound for the game menu;
- [ ] Improve the code for better performance;
- [ ] Improve the code for better programming patterns;
- [x] Add assets like trees , stones , bush etc to the environment;
- [x] Improve the credits screen;
- [ ] Add a animations to the credits and menu screen;


---

## Warning before compiling

For the game running well, you need to use python3.6 or higher

## Compiling

FIRST: Install cx_Freeze, if you already have pip3(because you need python3.6 or higher to run this game) installed,
run this: `pip3 install cx_Freeze --user`

To create an executable to double click and play instead of "Running in Python VM" always you want to play.

(In Linux): Now follow the next instructions

* (1) Open a terminal on the directory where you want to create game executable
* (2) Clone the repository: `git clone https://github.com/TigaxMT/Sword-N-Jump.git`
* (3) Now do a cd into the folder: `cd Sword-N-Jump/src/`
* (4) Run the following command: `python3 setup.py build`
* (5) cd into the build folder
* (6) cd into the only folder inside of the build folder
* (7) Now run this: `./game`
* (8) Enjoy!

You need to do this only 1 time , next time you only need to double click on the .exe or open a terminal inside the folder and run `./game`
 
## Running in Python VM

It is easy to run the game.

You need to have installed python3.6 or higher

Open a terminal and write the next commands:

* Ubuntu: ` sudo apt install python3 python3-pip`

* Fedora: ` sudo dnf install python3`

Verify if the version 3 is the 3.6 if not please download him of the official python website! 

After install python you need to install pygame with pip

If you use python3:
` pip3 install --user pygame`

Or if you compile python3.6:
` python3.6 -m pip install pygame --user`

(In Linux): Now follow the next instructions

* (1) Open a terminal on the directory where you want to run the game
* (2) Clone the repository: `git clone https://github.com/TigaxMT/Sword-N-Jump.git`
* (3) Now do a cd into the folder: `cd Sword-N-Jump/src/`
* (4) Write this command on terminal: ` python3 game.py` or ` python3.6 game.py`
* (5) Enjoy!  

## Controls

Jump = Up Arrow

Right = Right Arrow

Left = Left Arrow

Attack = SpaceBar

Pause = ESC

## Credits

* Programmers: Tiago Martins([Twitter](https://twitter.com/ttiago127)) & Kelvin Ferreira([Twitter](https://twitter.com/k30v1n))

* Sounds: Bruna Silva([SoundCloud](https://soundcloud.com/bruzzounds)|[YouTube](https://www.youtube.com/channel/UCrLNM0hqYuBzvpirB80SnRQ)|[Twitter](https://twitter.com/BruZZounds))

* Design: Zuhria Alfitra a.k.a pzUH([Website](https://www.gameart2d.com/))

# Donations

* If you liked the project and would like to contribute monetarily, you can make a donation of the amount you want through   Paypal. Thank you so much for everything.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RS4CKRLKDTKFJ)
