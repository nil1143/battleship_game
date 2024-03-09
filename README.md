# Battleships Game

### [Game Live](https://battleships-6d00f58f1c3d.herokuapp.com/)
![Game](/docs/readme-images/readme0.jpg)
## Content


* [Description](#description)
* [Project goals and UX](#project-goals-and-ux)
    * [User Goals](#user-goals)
    * [Site owners Goals](#site-owners-goals)
    * [Target Audience](#target-audience)
    * [User Requirements](#user-requirements)
    * [User Stories](#user-stories)
* [Features](#features)
* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Tested features](#tested-features)
    * [Test Cases](#test-cases)
    * [User Stories](#user-stories)
* [Fixed Bugs](#fixed-bugs)
* [Deployment](#deployment)
    * [Cloning & Forking](#cloning--forking)
    * [Local Deployment](#local-deployment)
    * [Remote Deployment](#remote-deployment)
* [Credits](#credits)
 
# **Description**

### This is a Python implementation of the classic Battleship game. The game is played on a grid where players attempt to sink each other's ships by guessing their coordinates.
<br>

# **Project Goals and UX**

## User Goals

### The main goal of Battleships Gmae is to provide users with an enjoyable gaming experience including:
- Interesting gameplay that challenges the mind.
- Clear instructions and user interface.


## Site Owner Goals

### As an owner of the project my requirements are:
- Create a logical functional game.
- Provide a well user experience.

## Target Audience

### Battleships targets a diverse audience, including:
- Game enthusiasts at any age.
- Casual gamers looking for a fun pastime.
- Individuals looking a challenge.

## User Requirements

### The users of Battleships Game expect:
- Enjoyable gaming experience.
- Intuitive game controls.
- Responsive feedback during gameplay.

## User Stories
1. As a player, I want to understand the rules of the game.
2. As a player, I want the game to provide a funny experience.


# **Features**
### Welcome and Instruction Message

 Displays a welcome message to the user upon login. <br>

![Welcome Message](docs/readme-images/readme-1.jpg)

### Game Board

 Generated board to play the game.  <br>
![Game Board](docs/readme-images/readme-2.jpg)

### Game Inputs
Allows the user to put their guesses and provides feedback on the result. <br>
![Game Inputs](docs/readme-images/readme-3.jpg)

### Result 
Displaying a result after putting the guess. <br>
![Result](docs/readme-images/readme-5.jpg)

### Out of turns
This message will appear when you out of turns.<br>
![Out of turns](docs/readme-images/readme-6.jpg)

### Invalid input
This message will appear if input is incorrect.<br>
![Invalid input](docs/readme-images/readme-7.jpg)<br>
![Invalid input2](docs/readme-images/readme-8.jpg)

# **Testing**

## Validator Testing

For code testing I used CI Python Linter The results are below.<br>

![CI Python Linter](docs/readme-images/readme-linter.jpg)


## Tested features

- Game Board
- Valid input
- Invalid input

## Test Cases

### Game board
| Test Case | Description | Expected Result | Actual Result |
|-----------|-------------|-----------------|---------------|
| Game Board | Check game board layout | Game board matches expected layout | Passed |

### Input Handling
| Test Case | Description | Expected Result | Actual Result |
|-----------|-------------|-----------------|---------------|
| Valid Input | Enter valid coordinates | Coordinate is accepted and processed | Passed |
| Invalid Input | Enter invalid coordinates | Error message displayed | Passed |

## User Stories Testing


|Story No.|Result|Story|
| ------------- | ------------- | ------------- |
|1|As a player, <br> I want to understand the rules of the game. <br><br>I know I am done because instruction opens up above the game board. <br>|Test Pass|
|2|As a player, <br>  want the game to provide a funny experience. <br><br>I know I am done when code functionality works with no issues. <br>|Test Pass |


# **Fixed bugs**

During code testing I met unexpected bug/error with the inputs in **get_user_input(self)** function.<br> If I left input empty it caused error in the console like in the screenshoot below:<br>
![fixed-bug1](docs/readme-images/fixed-bug-1.jpg)

Before fixing the issue **get_user_input(self)** function was like this:<br>
![fixed-bug2](docs/readme-images/fixed-bug-2.jpg)

The solution to fix the issue was method to check if user input length is 0.<br> If so, trigger the error message.<br>
![fixed-bugs3](docs/readme-images/fixed-bug-3.jpg)