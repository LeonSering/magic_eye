# 

This is a small python3 script to create a [autostereogram]([Autostereogram - Wikipedia](https://en.wikipedia.org/wiki/Autostereogram)). 

As a child I was fascinated from the [Magic Eye Book]([Magic Eye - Wikipedia](https://en.wikipedia.org/wiki/Magic_Eye)) and much later I was eager to figure out how this depth perception actually works. The result was this small script which I used to "impress" my co-workers and my girlfriend in a nerdy way. ;-)

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

To obtain the depth perception you have squint wall-eyed (meaning you have to focus behind the screen). The easiest way to achieve make the magic_eye picture about 30 - 40 cm wide and put your face close to the screen (about 40 cm). Try to focus behind the screen to see the effect. Then you can slowly move back to a comfortable position. 
