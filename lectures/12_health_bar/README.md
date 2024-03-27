<h2 align=center>Week 09: <em>Day 2</em></h2>

<h1 align=center>Video Game UI In Python</h1>

<p align=center><strong><em>Song of the day</strong>: <a href="https://youtu.be/t0NEfp9UysQ?si=4r4d4ypoumWKyprr"><strong><u>3aks el Seir</u></strong></a> by Charif Megarbane (2023)</em></p>

---

### Sections

1. [**Background**](#background)
2. [**Your Starter Code**](#part-1-your-starter-code)
3. [**Get The Health Bar Length**](#part-2-get-the-health-bar-length)
4. [**Getting Our Health Bar String**](#part-3-getting-our-health-bar-string)
5. [**Getting Our Colour-Coded String**](#part-4-getting-our-colour-coded-string)
6. [**Displaying Our Health UI**](#part-5-displaying-our-health-ui)

---

### _Background_

Health points (HP) are one of the most important and ubiquitous elements of tabletop and video games, representing the amount of damage a user or a player can take before they lose a life or lose consciousness. Being as important as it is displaying a user's health in a way that is simple and effective is an important part of a video game's UI.

A [**health bar**](https://en.wikipedia.org/wiki/Health_(game_terminology)#/media/File:Video_game_health_bar.svg) is one of the many ways to represent a player's health in video games. For example, we could "draw" a simple one in our shell / terminal by doing the following:

<a id="figure-1"></a>
```text
HP: 65 / 100
[=======   ]
```

<sub>**Figure 1**: A simple health bar, where the `'='` character represents one of the 10 "health bits" a player can have. Notice that each health bit here represents 10 HP.</sub>

This helps the player a ton with knowing how much health they have left, since just seeing the string `65 / 100` might lead the to believe that they have less (or more) health than they actually do; in general, visual representations are much more effective than numerical ones.

Another way of improving your UX experience is by adding colour to your UI. For example, if the user has a "high" amount of health, the health UI could be drawn in <span style="color:green; font-weight: bold">green</span>, whereas when the player has a critically low amount of health, it could be drawn in 
<span style="color:red; font-weight: bold">red</span>. We will be simulating this same effect in this problem.

<sub>**NOTE**: If you're using IDLE, the colour feature might unfortunately not work. I will show examples below of how colouring appears in IDLE so that you know if what you are coding up is correct. Running this on any kind of terminal, including Visual Studio's, should actually display colour.</sub>

<br>

### Part 1: _Your Starter Code_

To start, please copy-and-paste the following starter code into your file:

```python
from TextColour import TextColour, colour

GREEN  = TextColour.GREEN
YELLOW = TextColour.YELLOW
RED    = TextColour.RED
MIN_HEALTH = 0
MAX_HEALTH = 100
```

<sub>**Code Block 1**: Your starting code.</sub>

Click [**here**](https://drive.google.com/file/d/1wnyub_T1hhOCc9-82rlciTqpHMj4wfiO/view?usp=drive_link) to download the `TextColour` module. Make sure to place it in the same folder as the `py` file that you are working on. You do not need to worry about how this module works behind the hood. All you need to know is that:

- The **`colour()`** function accepts a `str` and a `TextColour` (i.e. `TextColour.GREEN`, `TextColour.YELLOW`, and `TextColour.RED`) as its two arguments, and returns the contents of that string in the colour that was passed.

```python
text = "Hello, world!"
print(colour(text, YELLOW))
```

Output:

> <span style="color:yellow; font-family:Courier">Hello, world!</span>

- `GREEN`, `YELLOW`, `RED` are `TextColour` objects that you can pass into the `colour()` function as arguments.
- `MIN_HEALTH` and `MAX_HEALTH` are, as their names imply, the minimum and maximum health our players will have.

Note, again, that you _must_ have the `TextColour.py` file in the same directory in order for this program to work.

Please don't hesitate to raise your hand if you have any questions about how these work!

<br>

### Part 2: _Get The Health Bar Length_

The same way we scaled `65 / 100` to seven health bits in **figure 1**, we will be using the health to scale our own health bar. The only difference here is that, instead of scaling by a factor of 10, we will be scaling by a _factor of 5_ (that is, our health bar will measure one fifth of the user's current health).

That is, you need to write code that converts the following health values:

```python
100
67
44
29
2
```

Into:

```python
20
14
9
6
1
```

Note that these values must be _rounded_ up, so that a player with `2` HP will still display one remaining health bit.

<br>

### Part 3: _Getting Our Health Bar String_

Create a string that contains a health bar similar to the one in [**figure 1**](#figure-1). You should use the `'['` and `']'` characters to represent the beginning and end of the bar, and the `'='` character to represent a health bit. The health bits should always be aligned to the left.

In other words, for the following health points:

```python
100
67
44
29
2
```

We should produce the following bars:

```text
[====================]
[==============      ]
[=========           ]
[======              ]
[=                   ]
```

<br>

#### Part 4: _Getting Our Colour-Coded String_

Our objective now is to turn our health bar into its colour-coded equivalent according to the player's current HP (all ranges are inclusive on both ends):

- **`0` - `33`**: <span style="color:red; font-weight:bold">red</span>
- **`34` - `66`**: <span style="color:yellow; font-weight:bold">yellow</span>
- **`67` - `100`**:  <span style="color:green; font-weight:bold">green</span>

For example, if our original string is `"Status"`, and the player's healths are:

```python
100
67
44
29
2
```

Their colour-coded equivalents would be:

> <span style="color:green; font-family:Courier">Status</span>

> <span style="color:green; font-family:Courier">Status</span>

> <span style="color:yellow; font-family:Courier">Status</span>

> <span style="color:red; font-family:Courier">Status</span>

> <span style="color:red; font-family:Courier">Status</span>

You will have to make use of the `colour()` function from the `TextColour` function included in your file here.

**NOTE**: If you're using IDLE or certain other IDEs, you might get the following output instead:

```text
[92mStatus[0m
[92mStatus[0m
[93mStatus[0m
[91mStatus[0m
[91mStatus[0m
```

This is an unfortunate limitation, but just know that if you see the strings `[92m` (for green), `[93m` (for yellow), and `[91m` (for red), and the string `[0m` at the end of your output lines, you're doing this correctly. It's just another instance of IDLE being a buzzkill.

<br>

### Part 5: _Displaying Our Health UI_

Finally, generate a random integer between the minimum possible health and the maximum possible health (inclusive) and, depending on what the number is print colour-coded UI that displays both its _numerical representation_ and its _health bar representation_. For example:


If the player's health is `92`:

> <span style="color:green; font-family:Courier">HP: 92 / 100</span>
> 
> <span style="color:green; font-family:Courier">[===================&nbsp;]</span>

If the player's health is `54`:

> <span style="color:yellow; font-family:Courier">HP: 54 / 100</span>
> 
> <span style="color:yellow; font-family:Courier">[===========&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]</span>

If the player's health is `6`:

> <span style="color:red; font-family:Courier">HP: 6 / 100</span>
> 
> <span style="color:red; font-family:Courier">[==&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]</span>

IDLE output:

```text
[92mHP: 92 / 100[0m
[92m[=================== ][0m
[93mHP: 54 / 100[0m
[93m[===========         ][0m
[91mHP: 6 / 100[0m
[91m[==                  ][0m
```
