# Image2Cordinates
## Requirements
This code uses the following Python libraries:

 - opencv-python (https://pypi.org/project/opencv-python/) 
 - OS Module
 - 
## Usage
Code inputs an Image-path and generates the corresponding coordinates map.

You can run it as a normal Python3 program.

## Input Image File
In an input image:
  - There should be Black obstacles
  - and Red targets

Please note that the input files with no included Targets are allowed.

Please consider the provided examples.

## Output
An output coordinates map includes a list of x coordinates which are immediately followed by y coordinates for obstacles.

Example:

```
 x1
 y1
 x2
 y2 
 ....
```

After that, this file continues with the following line:

```
"---TARGETS---"
```

Hereafter, coordinates of the potential targets come into lines just like the ones of the obstacles.

Example:
```
 x1
 y1
 ....
 x99
 y99
 "---TARGETS---"
 x100
 y100
```
Please note that there are coordinates for every pixel of the obstacles.

Also, please note that there is only ONE coordinate pair for each of the targets.

### Using Output file in NetLogo
You can use the following code to load the file in a NetLogo Programm:

```NetLogo
breed [Targets Target]
to Load-Map
  ask patches [set pcolor white]
  file-open "Example_map_2.cxy"
  let y/2 max-pycor / 2
  let end_of_obstacles? false
  while [not end_of_obstacles?]
  [
    let line file-read
    ifelse line = "---TARGETS---" [
      set end_of_obstacles? true]
    [
      let y 0 - line + max-pycor
      let x file-read - max-pxcor
      ask patches with [pxcor = x and pycor = y]
      [
        set pcolor black
      ]
    ]
  ]
  while [not file-at-end?]
  [
    let y 0 - file-read + max-pycor
    let x file-read - max-pxcor
    create-Targets 1
    [
      setxy x y
      set shape "X"
      set size 2
      set color red
    ]
  ]
  file-close
end
```
