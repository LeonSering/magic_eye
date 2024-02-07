# 

This is a small python3 script to create a [autostereogram](https://en.wikipedia.org/wiki/Autostereogram). 

As a child I was fascinated from the [Magic Eye Book](https://en.wikipedia.org/wiki/Magic_Eye) and much later I was eager to figure out how this depth perception actually works. The result was this small script which I used to "impress" my co-workers and my girlfriend in a nerdy way. ;-)

# Requirements

python3 with pip

# Installation

1) Set up an python virtual environment
   
   ```bash
     python3 -m venv env
   ```

2) Start the virtual environment
   
   ```bash
   source env/bin/activate
   ```

3) Install the python dependencies
   
   ```bash
   pip install -r requirements.txt
   ```

(To terminate the virtual environment afterwards use the command: ```deactivate```)

# Usage

1. Create a small 80x80 image that is used a repeated tile and store it as tile.png in the main directory. For a good effect the tile should be contrast rich.

2. Create holo.png for the 3D effect. It must be in grey-scales and of dimension 1120 × 800.
   
   - black -> background
   
   - grey -> in the middle
   
   - white -> foreground

3. Run python main.py to create the "magic_eye.png".

# Obtain Depth Perception

To obtain the depth perception you have to squint your eyes in the "wall-eyed"-way (meaning that you have to focus behind the screen). 
The easiest way to achieve this is to make the magic_eye picture about 30 - 40 cm wide on the screen and then put your face close to 
the to it (a distance of 40 cm should work). Try to focus behind the screen to see the effect. If it does not work, get closer to the screen.
As soon as you have the depth perception you can slowly move back to a comfortable position.
With a bit of training it is easy to achieve from all distances.
