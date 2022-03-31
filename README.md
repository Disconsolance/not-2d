
# not 2d        

Pseudocomputer gibberish for gifs, inspired by 00s glitchcore


## Table of contents
- [Demo](#demo)
- [Installation](#installation)
- [Configuration](#config)
- [Usage](#usage)

## Demo

Input \
![input](https://github.com/PastelNightmare/not-2d/blob/master/demo/in.gif) 

Output \
![output](https://github.com/PastelNightmare/not-2d/blob/master/demo/out.gif)

## Installation

```bash
  git clone https://github.com/PastelNightmare/not-2d
  cd not-2d
  python -m pip install -r requirements.txt
```
    
## Config

|category| var | type | description |
|--------|-----|------|-------------|
| Input  | IMG | string | Image filename |
| Generation | GenPointer | bool | Use GenerateRandomPointer instead of GenerateRandomString |
| Generation | DrawShadow | bool | Whether or not to draw a shadow to text |
| Generation | LINES | int | How many lines to draw |
| Chars | STRINGCHARLIST | string | Characters used by GenerateRandomString |
| Chars | POINTERCHARLIST | string | Characters used by GenerateRandomPointer |
| Text | STRINGMIN | int | Min amount of chars |
| Text | STRINGMAX | int | Max amount of chars¹ |
| Font | FONTNAME | string | Font file name |
| Font | FONTSIZE | int | Font size |
| Placement | STEPRIGHT | int | Number of pixels to step from the left border |
| Placement | STEPDOWN | int | Number of pixels to step from the top border |
| Placement | LINESTEP | int | Number of pixels to step when making a new line² |
| Placement | OFFSET | int | Number of pixels to offset to make a shadow |
| Factor³ | FONTSIZEFACTOR | float | Calculate true character size in pixels |
| Factor³ | LINESTEPFACTOR | float | Calculate true new line step in pixels |

¹ - GenerateRandomPointer does not use STRINGMAX by default and sets 8 as max length. \
² - Equals to FONTSIZE by default \
³ - Optional variables, used for calculating total height of drawn text with newlines

## Usage

0. Put **.ttf** font into the root directory of this script
1. Move target **.gif** folder to `in` folder
2. Change config variables as required
3. Run script
4. Get result gif file from the `out` folder