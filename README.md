# oop-proj-5

## Description
This is a game with anime and items, up down left and left to control your position, and space to shut bullet.

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
