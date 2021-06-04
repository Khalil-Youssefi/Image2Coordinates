# Image2Cordinates
## Requirements
This code uses the following Python libraries:

 - opencv-python (https://pypi.org/project/opencv-python/) 
 - OS Module
 - 
## Usage
Code inputs an Image-path and generates the corresponding coordinates map.

## Input Image File
In an input image:
  - There should be Black obstacles
  - and Red targets

Please note that the input files with no included Targets are allowed.

Please consider the provided examples.

## Output
An output coordinates map includes a list of x coordinates which are immediately followed by y coordinates for obstacles.

Example:

 x1
 
 y1
 
 x2
 
 y2 
 
 ....

After that, this file continues with the following line:

"---TARGETS---"

Hereafter, coordinates of the potential targets come into lines just like the ones of the obstacles.

Example:

 x1
 
 y1
 
 ....
 
 x99
 
 y99
 
 ---TARGETS---
 
 x100
 
 y100

Please note that there are coordinates for every pixel of the obstacles.

Also, please note that there is only ONE coordinate pair for each of the targets.
