# oop-proj-5

## Description
This is a maze game with three modes : easy, normal and hard. You can choose to compete with the computer or not. Also you can choose single player mode or multiplayer mode.

<img src="./oop5.gif"/>

## Getting Started

### Ubuntu
git clone the game:
```
$ cd ~
$ git clone git@github.com:ARG-NCTU/oop-proj-5.git
```
Run docker
```
$ cd oop-proj-5
$ source docker_run.sh
```
Start the game
```
$ python3 main.py
```

### Windows
Install Anaconda from following site.
https://docs.anaconda.com/free/anaconda/install/windows/
#### Download oop-proj-5
Download oop-proj-5 as a zip, and unzip.
#### activate base env, and start the game
You can change "oop_env" to what ever the name you like.
```
$ conda create --name oop_env python=3.8.10
$ conda activate oop_env
$ pip3 install pygame
$ pip3 install numpy
```
cd to your oop-proj-proj-5 dir location, and run the game.
```
$ cd oop-proj-proj-5
$ python main.py
```
## Executing Program
<br />Just run the code you have just downloaded.</br >
<br />After running the code you would see the main menu. Just press start to start the game.</br >
<br />After that you would be able to choose the game mode : easy, normal and hard. Just choose a mode you like.</br >
<br />Press the up, down , left, right key to move and to get out of the maze. If you have trouble getting out of the maze, you can press the solution button to see the solution. The game is preseted to compete with the computer, the computer will start to solve the maze after the game have started 30 seconds. If you don't want to have a competetion with the computer, go to the main menu and press the setting button to go to the setting menu to turn the setting off. You may notice that there is a thing called seed in the setting menu and also shown on the main game screen,  the seed code is for genearting the same maze. The maze is preseted to be randomly genearted, but if you want to generate the maze that had been genearted just go to the setting menu to enter the seed code. You may notice there is another thing at the setting page, which is multiplayer mode. You can choose to play the game by yourself, or play along with your friends. The game is preseted to be single player mode. If you want to play with your friends, just turn on the multiplayer mode. You can create a room or join a room. As long as everyone have join the room, the game will start and you can have a competition with your friends.</br >
<br />As long as you exit the maze, the score screen will be shown. You can see the time you spend to break through the maze. If you spend less time than computer, you will see " You win!" on the score screen. Otherwise, you will see " You lose!" on the score screen and also the time the computer have spend to solve the maze. </br >
<br />Last but not least, if you go to the main menu and then press score to see all of the game results. </br >

## Authors
- [veldahung](https://github.com/veldahung)
- [Cyw-twntpc](https://github.com/Cyw-twntpc)
