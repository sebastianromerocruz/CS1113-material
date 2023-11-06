<h2 align=center>Lecture 12</h2>

<h1 align=center>Python Lists</h1>

<h3 align=center>6 Red Wolf Moon, Imperial Year MMXXIII</h3>

<p align=center><strong><em>Song of the day</strong>: <a href="https://youtu.be/y3nwDlcYaUg?si=4nMK-QQeOvH8fOxC"><strong><u>DONT YOU THINK IT'D BE NICE?</u></strong></a> by PAPOOZ (2023).</em></p>

### Sections

1. [**Parameters and `return` Review**](#part-1-parameters-and-return-review)
    1. [**Background**](#background)
    2. [**Your Starting Code**](#your-starting-code)
    3. [**The `get_health_bar_length()` Function**](#the-get_health_bar_length-function)
    4. [**The `get_health_bar()` Function**](#the-get_health_bar-function)
    5. [**The `diplay_health()` Function**](#the-display_health-function)
2. [**An Introduction To Python Lists**](#part-2-an-introduction-to-python-lists)
3. [**Lists As Sequences**](#part-3-lists-as-sequences)

### Part 1: _Parameters and `return` review_

#### _Background_

Health points (HP) are one of the most important and ubiquitous elements of tabletop and video games, representing the
amount of damage a user or a player can take before they lose a life or lose consciousness. Being as important as it is
displaying a user's health in a way that is simple and effective is an important part of a video game's UI.

A [**health bar**](https://en.wikipedia.org/wiki/Health_(game_terminology)#/media/File:Video_game_health_bar.svg) is one
of the many ways to represent a player's health in video games. For example, we could "draw" a simple one in our shell
/ terminal by doing the following:

```text
HP: 65 / 100
[=======   ]
```

<sub>**Figure 1**: A simple health bar, where the `'='` character represents one of the 10 "health bits" a player can 
have. Notice that each health bit here represents 10 HP.</sub>

This helps the player a ton with knowing how much health they have left, since just seeing the string `65 / 100` might
lead the to believe that they have less (or more) health than they actually do; in general, visual representations are
much more effective than numerical ones.

#### _Your starting code_

Here, I have included the following lines of code to get you started:

```python
from random import randrange


MIN_HEALTH = 0
MAX_HEALTH = 100

"""
WRITE YOUR FUNCTIONS BELOW
"""



"""
WRITE YOUR FUNCTIONS ABOVE
"""

def main():
    curr_health = randrange(MIN_HEALTH, MAX_HEALTH)
    # display_health(curr_health)  # uncomment to test


main()
```

<sub>**Code Block 1**: Your starting code. Since the `display_health()` function has yet to be defined, I have commented
its invocation out inside the `main()` function. Feel free to uncomment it when you are ready to test it.</sub>

---

#### _The `get_health_bar_length()` function_

Write a function `get_health_bar_length()` that accepts a single parameter: `health`, an integer that represents the 
user's current health. The same way we scaled `65 / 100` to seven health bits in **figure 1**, we will be scaling our 
own health bar. The only difference here is that, instead of scaling by a factor of 10, we will be scaling by a factor
of 5 (that is, our health bar will measure one fifth of the user's current health).

Sample executions (feel free to pose these examples in your `main()` to test):

```python
print(get_health_bar_length(100))
print(get_health_bar_length(67))
print(get_health_bar_length(44))
print(get_health_bar_length(29))
print(get_health_bar_length(2))
```

Output:

```text
20
14
9
6
1
```

Note that the amount of health bits are being **rounded** up, so that a player with `2` HP will still display one 
remaining health bit.

---

#### _The `get_health_bar()` function_

Your next function will accept one parameter: `health`, also an integer that represents the user's current health. This
function will return a string that contains a health bar similar to the one in **figure 1**. You must, of course, use 
`get_health_bar_length()` inside of it in order to determine how many health bits it will contain. You should use the
`'['` and `']'` characters to represent the beginning and end of the bar, and the `'='` character to represent a health
bit.

Sample executions:

```python
print(get_health_bar(100))
print(get_health_bar(67))
print(get_health_bar(44))
print(get_health_bar(29))
print(get_health_bar(2))
```

Output:

```text
[====================]
[==============      ]
[=========           ]
[======              ]
[=                   ]
```

Notice that the second "section" of the health bar is shown as being "depleted" by using a space character `' '` instead
of a `'='`; every health bar returned by `get_health_bar()` must be the same length.

#### _The `display_health()` function_

Finally, the `display_health()`, which will accept the `health` integer parameter as its only parameter, will use our
other functions to print both a numerical and a visual health UI.

Sample executions:


```python
display_health(92)
print()

display_health(54)
print()

display_health(6)
```

Terminal output:

```
HP: 92 / 100
[=================== ]

HP: 54 / 100
[===========         ]

HP: 6 / 100
[==                  ]
```

### Part 2: _An Introduction to Python Lists_

So, we've seen sequences of numbers, and we've seen sequences of characters. There's not really anything else in the
world of computing that gets more atomic than that—ones and zeroes are numbers, after all.

So instead of looking to smaller things, let's think the exact opposite way: numbers, characters, and really everything
in Python are objects. So can we store a sequence of objects? SURE CAN.

```python
CURRENT_YEAR = 2021

name = "Léa Seydoux"
age = 37
hometown = "Paris"
occupation = "Actress"
years_active = range(2005, CURRENT_YEAR + 1)

information = [name, age, hometown, occupation, years_active]
print(information)
```

Output:

```text
['Léa Seydoux', 36, 'Paris', 'Actress', range(2005, 2022)]
```

Say hello to the Python list. In technical terms:

> **List**: A data type representing a sequence of objects. These objects (the elements of a list) can be of different 
> types.

Here's another example of a list:

```python
character = ["Link", 10, True, ["Kokiri Sword", "Razor Sword", "Gilded Sword"]]
```

<sub>**Code Block 2**: Even lists can be elements of a list.</sub>

### Part 3: _Lists as Sequences_

It also turns out that **indexing** works with the exact same syntax that we use for strings:

```python
CURRENT_YEAR = 2021

name = "Léa Seydoux"
age = 36
hometown = "Paris"
occupation = "Actress"
years_active = range(2005, CURRENT_YEAR + 1)

information = [name, age, hometown, occupation, years_active]

print("{}, a(n) {} from {}".format(information[0], information[3].lower(), information[2]))
```

Output:

```text
Léa Seydoux, a(n) actress from Paris
```

By way of a more useful example say that we have a list populated by integers and floats. How would we find the average of
these numbers?

```python
sample_list = [10, 50.6, -44, -0.0001, 56.00043, 45]

average = get_list_average(sample_list)

print(average)
```

Well, let's write the function stub first, before anything else:

```python
def get_list_average(list):
    pass
```

As we learned last week, a list is a **sequence of elements**, the same way that a string is a sequence of characters
and a range is a sequence of numbers. Therefore, we can iterate through it using a `for`-loop. How does this help us?
Well, in order to calculate the average of any set of numbers, we need both the sum of those numbers, and the amount
of numbers in that set. We can get both of these things via a `for`-loop:

```python
def get_list_average(list):
    total_sum = 0
    length = 0

    for number in list:
        total_sum += number
        length += 1

    average = total_sum / length
    return average
```

There's one thing we should be careful here, though. If the list that the user passes in as an argument turns out to be 
empty, our `average` calculation will yield a divide-by-zero error, so we should add a failsafe mechanism for that. 
Turns out that, just like with strings, we can use the `len()` function to get the length of a list. Let's use that to
our advantage:

```python
def get_list_average(list):
    length = len(list)
    
    if length == 0:
        print("WARNING: List is empty. Returning 0.0")
        return 0.0
    
    total_sum = 0

    for number in list:
        total_sum += number

    average = total_sum / length
    return average
```

<sub>**Code Block 3**: In this whole function, we never see list-specific behavior. We're just treating it like a sequence 
of numbers.</sub>

What does that mean for lists? If we can treat lists like sequences and, as we have seen, we can index them to
get individual values, we can iterate through lists using indexing! Let's say we wanted to write a function that returns
the **index of the largest number in a list of positive numbers**. By definition, we need to use indexing, so let's set
up our function to do that:

```python
def get_index_of_largest(list):
    length = len(list)

    for index in range(length):
        current_element = list[index]
        
        # Our algorithm
```

To find the largest number, we need to keep track of the current largest number, and if we encounter a number that is 
larger than the current largest number, we make the new number the current largest number. Since we made the assumption
that the list will contain positive numbers only, our starting value can simply be `-1` or any other negative number,
since we can safely assume that no positive number will be lower than it:

```python
def get_index_of_largest(list):
    length = len(list)
    largest_number = -1
    largest_index = -1

    for index in range(length):
        current_element = list[index]
        if current_element > largest_number:
            largest_number = current_element
            largest_index = index

    return largest_index


def main():
    sample_list = [20, 45, 34.56432, 1, 2.3, 1.00002, 45.0000002, 5]
    largest_index = get_index_of_largest(sample_list)
    print("The index of the largest number in the list {} is {}.".format(sample_list, largest_index))


main()
```

Output:

```text
The index of the largest number in the list [20, 45, 34.56432, 1, 2.3, 1.00002, 45.0000002, 5] is 6.
```

On the topic of indexing, it's also worth remembering that you can also index them the same way you would a string:

```python
list = [1, 2, 3, 4, 5]

for index in range(len(list)):
    slice = list[:index + 1]
    print("Current slice: {}".format(slice))
```

Output:

```text
Current slice: [1]
Current slice: [1, 2]
Current slice: [1, 2, 3]
Current slice: [1, 2, 3, 4]
Current slice: [1, 2, 3, 4, 5]
```

So, we can iterate and index through a list. In a similar fashion to `range()` and strings, we can also check for 
membership of elements using the `in` operator:

```python
french_revolution_years = [1789, 1830, 1848]
year = 1967

print(year in french_revolution_years)
```

Output:

```text
False
```

In other words, the value of `"1967"`, stored in the variable `year`, does _not_ exist in the sequence (i.e. list)
stored in the variable `french_revolution_years`.

Here's couple more examples:

```python
>>> print(5 in [3, 6, [5, 7]])
False

>>> print(7 not in [1, 2, 3, 4])
True
```

<sub>**Previous: [Functions: _`return`_](/lectures/11_functions_return/)**</sub>