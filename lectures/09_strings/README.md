<h2 align=center>Lecture 09</h2>

<h1 align=center>The <code>str</code> Object</h1>

<h3 align=center>16 Wyvern Moon, Imperial Year MMXXIII</h3>

<p align=center><strong><em>Song of the day</strong>: <a href="https://youtu.be/BI4zNteRP7E?si=PIHVKHxtjegdF9En"><strong><u>憐れみの讃歌 (Eulogy to Compassion)</u></strong></a> by Kyrie (Aina the End) (2023).</em></p>

### Sections

1. [**Strings As Sequences**](#part-1-strings-as-sequences)
2. [**String Comparison**](#part-2-string-comparison)
3. [**The `in` Operator**](#part-3-the-in-operator)
4. [**Special Characters And `print`'s `end` Parameter**](#part-4-special-characters-and-prints-end-parameter)

### Part 1: _Strings as Sequences_

Remember that a `for`-loop iterates through every member of a sequence?

```python
for number in range(0, 10):
    print("Sequence member '", number, "'", sep="")
```

Output:

```text
Sequence member '0'
Sequence member '1'
Sequence member '2'
Sequence member '3'
Sequence member '4'
Sequence member '5'
Sequence member '6'
Sequence member '7'
Sequence member '8'
Sequence member '9'
```

So, in this case, our sequence is every whole number between and including 0 and 9:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

It turns out that, in Python, sequences aren't limited to being numerical—they can also be alpha-numerical:

```python
alpha_seq = "Adachi and Shimamura"

for character in alpha_seq:
    print(character)
```

Output:

```text
A
d
a
c
h
i
 
a
n
d
 
S
h
i
m
a
m
u
r
a
```

So is a string a sequence? Technically. It can basically be used in sequence-like ways, which makes it very handy for 
programmers, since a good amount of user-input that we receive is in string form. The ability to be able to consider 
characters one-by-one is will prove to be indispensable.

---

What are other cool, sequence-like things we can do with strings?

Well, what if we wanted to access any individual letter in a string? Let's say we have the following activity log in a
chat-room:

```text
[A]: hey
[A]: whats up
[B]: Please leave me alone
```

In this case, it's pretty clear that the `"A"` and `"B"` characters represent two members of a chat-room. Moreover, we
know that both `"A"` and `"B"` are always the second character in the whole line. We can use this information to our 
advantage by using something called ***indexing***.

Let's say we wanted to find out whether user A or user B sent the message:

```python
ID_LOCATION = 1

message = "[B]: Please leave me alone"
user_id = message[ID_LOCATION]

print("User", user_id, "sent this message.")
```

Output:

```text
User B sent this message.
```

So, what did we do? The key line here is:

```python
user_id = message[ID_LOCATION]
```

Since `ID_LOCATION` is equal `1`, we could read this line as:

> Take the **first** character from the string variable `message` and store it inside a variable called `user_id`.

Why is it the first character if `A` and `B` always appear after the `[`? General speaking, all programming languages 
start counting from `0` instead of `1`. That's actually why the `range()` function's default starting value is `0`—it's
an inherent characteristic of most programming languages. So if you wanted to refer to the `[` in the strings above, 
you'd say:

> In the string `"[B]: Please leave me alone"`, the **0th** (zeroth) element is `[`.

So with this knowledge, we can now print each of the characters of a string in two ways:

```python
BOOK_TITLE = "In Search of Lost Time"
LENGTH = 22

# using sequences
for letter in BOOK_TITLE:
    print(letter)

# using indices
for index in range(LENGTH):
    letter = BOOK_TITLE[index]
    print(letter)
```

---

One quick other (***very***) important thing about strings is that they are ***immutable***. That is, once you define
the value of a string, you **cannot** change it. The only way to do something similar is to create a whole new string
using the value of the old string:

```python
first_name = "Élisabeth Louise"
last_name = "Vigée Le Brun"
full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Élisabeth Louise Vigée Le Brun
```

Here, it is very important to recognize that the string `full_name` is _not_ `first_name` with the strings `" "` and 
`last_name` appended to it. Instead, it is a **completely** different string, existing in a completely different place 
in memory. This new string will simply happen to have the contents of `first_name`, `" "`, and `last_name` put together
in that order—and only because we asked Python to create it in such a way.

Mutability / immutability is a huge topic in this class and computer science in general, so don't forget the words.
We'll see them again soon enough.

### Part 2: _String Comparison_

If we have a variable called `string`, and it has a value of `"abc"`. What does the following expression evaluate to?

```python
>>> string == "abc"
```

Well, let's check the output:

```python
>>> string == "abc"
True
```

Makes sense; the comparison operator `==` checks whether two Python objects are equal in value. Since the value of 
`string` is `"abc"`, it is indeed equal to the string `"abc"`.

So, if we can check for the equality of strings, can we check for inequality?

```python
>>> string != "not abc lol"
True
```

Makes sense; these strings are not at all the same in value. These are both pretty intuitive operations, but what about
comparing them using `>`, `<`, `>=`, and `<=`?

```python
>>> string >= "not abc lol"
False

>>> string < "bcd"
True
```

Clearly, these operations are not causing errors, so how do they work? When comparing string, Python uses their 
**lexicographical order** in order to determine whether one is larger than the other. Lexicographical order simply means
applying a value of, say, 1 to `"a"`, 2 to `"b"`, 3 to `"c"`, etc. (the numerical equivalent of `"a"` is actually `97`, 
but don't worry about that for now).

This means that:

```python
>>> "a" > "b"
False
>>> "a" < "b"
True
>>> "A" < "b"
True
```

Notice that these operations are not case-sensitive—a very rare exception in programming.

What about comparisons using strings of different lengths? Python basically goes in order:

```python
>>> "Paris" > "Parthenon"
False
```

1. Is the `"P"` from `"Paris"` equal to the "`P`" from `"Parthenon"`? Yes, so move on to the next character.
2. Is the `"a"` from `"Paris"` equal to the "`a`" from `"Parthenon"`? Yes, so move on to the next character.
3. Is the `"r"` from `"Paris"` equal to the "`r`" from `"Parthenon"`? Yes, so move on to the next character.
4. Is the `"i"` from `"Paris"` equal to the "`t`" from `"Parthenon"`? No, so apply the `>` operation.
5. Is `"i"` > `"t"`? `"i"` has a lower lexicoogical value than `"t"` (i.e. it appears earlier in the alphabet), so this
operation evaluates to `False`.
6. The whole operation evaluates to `False`

What about this?

```python
>>> "Car" >= "Cartagena"
False
```

1. Is the `"C"` from `"Car"` equal to the "`C`" from `"Cartagena"`? Yes, so move on to the next character.
2. Is the `"a"` from `"Car"` equal to the "`a`" from `"Cartagena"`? Yes, so move on to the next character.
3. Is the `"r"` from `"Car"` equal to the "`r`" from `"Cartagena"`? Yes, so move on to the next character.
4. Since `"Car"` has no more values to compare with `"Cartagena"`, `"Cartagena"` is by default of larger value.
5. The operation, thus, evaluates to `False`.

Here are more examples:

```python
>>> "Sonny Boy" < "SONNY BOY"
False

>>> "Nozomi" >= "Mizuho"
True

>>> "Napoleon I" > "Napoleon III"
False

>>> "!!!" <= "   "
False
```

That last one is a bit of a toughie if you don't know about ASCII values and how to find them, but don't worry—it's not
important for now. We'll get there eventually.

### Part 3: _The `in` Operator_

Yay, a new operator! `in` is actually kind of heaven-sent if you come from a Java/C++ background. `in` is what is called
a **membership** operator, and it evaluates to either `True` or `False`:

```python
>>> "Car" in "Cartagena"
True

>>> "PARIS" in "Parisian"
False
```

The above operations can be described in English as follows:

>> The string `Car` exists as a sub-string of the exact same value somewhere in the string `Cartagena`.
> 
>> The string `PARIS` does not exist as a sub-string of the exact same value somewhere in the string `Parisian`.

That's why it's called a membership operator: it checks for the membership of an object inside another object. You can 
also check for non-membership:

```python
>>> "Prague" not in "Czechia"
True

>>> "1" in "onetwothree"
False

>>> "net" not in "onetwothree"
False
```

---

### Part 4: _Special Characters and `print()`'s `end` Parameter._

There are a few "special characters" in programming that we should be aware of. The two that we'll need in this course
are `"\n"` and `"\t"`.

`\n` is the **newline operator**:

```python
information = "NAME: Alice Sara Ott\nOCCUPATION: Pianist\nBIRTHPLACE: München, West Germany"
print(information)
```

Output:

```text
NAME: Alice Sara Ott
OCCUPATION: Pianist
BIRTHPLACE: Munich, West Germany
```

And `\t` is the **tab, or indentation, operator**:

```python
first_half = "Jan\tFeb\tMar\tApr\tMay\tJun\t"
second_half = "Jul\tAug\tSep\tOct\tNov\tDec\t"

print(first_half)
print(second_half)
```

Output:

```text
Jan	Feb	Mar	Apr	May	Jun	
Jul	Aug	Sep	Oct	Nov	Dec	
```

---

To find out a character's ASCII equivalent, we use the `ord()`, or **ordinal**, function:

```python
>>> ord("a")
97

>>> ord("A")
65

>>> ord("ñ")
241

>>> ord("疲")
30130

>>> ord("δ")
948
```

And, conversely, to find the corresponding character to any given positive integer, we use `chr()`:

```python
>>> chr(123)
'{'

>>> chr(42)
'*'

>>> chr(512)
'Ȁ'
```

### Part 5: _String Traversal (Continued)_

Let's continue our conversation on strings with a quick program. Write a program that asks the user for two strings 
`first_string` and `second_string`. Then, your program will print all the characters from the first string that appear 
in the second string. Write three versions of this program:

1. Using `for`-loop string sequencing.
2. Using `for`-loop string indexing.
3. Using string indexing, but with a `while`-loop.

Here's a sample
output of how your program could behave:

```text
Enter a string: Rickenbacker 4000C Bass Guitar
Enter a second string: Rickenbacker 330 Electric Guitar
R
i
c
k
e
n
b
a
c
k
e
r
 
0
 
e
c
t
r
i
c
 
G
u
i
t
a
r
```

There are two ways we could approach this. The quickest and perhaps more intuitive one is use the second string as a
sequence, and then check for membership of each of its letters in the first string. We do this by using `in`, the 
membership operator:

```python
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

for letter in second_string:
    if letter in first_string:
        print(letter)
```

<sub>**Code Block 1**: Checking for membership by treating `second_string` as a sequence.</sub>

If we didn't want to use `second_sentence` as a sequence, and instead wanted to use indices, our `for`-loop would look 
something like this instead:

```python
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

second_string_length = len(second_string)

for index in range(second_string_length):
    letter = second_string[index]
    if letter in first_string:
        print(letter)
```

<sub>**Code Block 2**: Checking for membership by using indices. Note the use of `len()`.</sub>

Both ways work and are actually equally efficient. Which one to use depends largely on your use case. If you need to 
know, use, or keep track of the position of an element within a sequence (e.g. _"Find the x-th element of the string"_),
then using indices is the way to go.

Finally, the `while`-loop version will look as follows:

```python
first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

second_string_length = len(second_string)
index = 0

while index < second_string_length:
    letter = second_string[index]
    if letter in first_string:
        print(letter)

    index += 1
```

Check out the code here [**membership.py**](membership.py) with the configuration `Membership`.

### Part 6: _The `str` Object_

We've been spending a fair amount of time using strings now, so we should probably dive in a little deeper into their 
behavior.

Objects in general (not just `str` objects) have a set of values and operations associated to them. In technical jargon,
we would say that objects have **reference attributes bound to them**. The values associated with objects are called
**attributes** (similar to variables), and the operations associated with objects are called **methods** (similar to 
functions):

>> **Attribute**: A _variable_ associated to an object of a certain type/class.
> 
>> **Method**: A _function_ associated to an object of a certain type/class.

Both of these terms will make more sense when we get to object-oriented programming, but just learn to recognise this
behavior when I say things like "this is a _method_ of a `str` object", for example.

Let's take a look at some examples:

```python
>>> string = "the tale of the heike"
>>> string.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> string.__class__
<class 'str'>
```

In this case, `__doc__` is an **attribute** associated to the string object `string`, which prints out a bunch of 
technical information that you don't need to worry about. `__class__` is another such attribute, which tells us the name
of the class of the current object (in this case, it's a `str` object).

Let's take a look now at a couple of **methods**:

```python
>>> string = "the tale of the heike"
>>> string.capitalize()
'The tale of the heike'
>>> string.upper()
'THE TALE OF THE HEIKE'
```

In this case, `capitalize()` is ***returns*** a string with its first character capitalized (if the first character is
not a lower-case letter, it will simply return the same string). By the same token, `upper()` ***returns*** a string
with the original string's letters capitalized.

This is important. **Strings are immutable**; none of their methods that appear to be mutating them in any way, but 
rather creating an entirely new string object based on the contents of the original:

```python
>>> example = "Mineral water"
>>> example.upper()
'MINERAL WATER'
>>> example
'Mineral water'
>>> example_upper = example.upper()
>>> example_upper
'MINERAL WATER'
```

The value of example didn't change when its `upper()` method was invoked.

Here are some examples of methods from the `str` class that we'll be making heavy use of in this class:

| **Method**  | **Example**                                                                                                                | **Description**                                                                            |
|-------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `find()`    | `"abc".find("a")` returns `0` `"abc".find("z")` returns `-1`                                                               | Returns the index of **first** occurrence of the argument in a string object.              |
| `format()`  | `"Hi, my name is {}, and I love {}.".format("Sebastian", "Zelda")` returns `"Hi, my name is Sebastian, and I love Zelda."` | Formats string into nicer output.                                                          |
| `isalnum()` | `"1978".isalpha()`  returns  `False`  `"The1975".isalpha()`  returns  `True`                                               | Returns `True` if all the characters in a `str` object are alphanumeric.                   |
| `isalpha()` | `"1978".isalpha()` returns `False`  `"TheNineteenSeventyFive".isalpha()` returns `True`                                    | Returns `True` if all the characters in a `str` object are alphabetic.                     |
| `isdigit()` | `"1978".isdigit()`  returns  `False`  `"The1975".isalpha()`  returns  `False`                                              | Returns `True` if all the characters in a `str` object are numeric.                        |
| `islower()` | `"The The".islower()` returns `False`                                                                                      | Returns `True` if all the characters in a `str` object are lowercase.                      |
| `isupper()` | `"NYU".isupper()` returns `True`                                                                                           | Returns `True` if all the characters in a `str` object are uppercase.                      |
| `lower()`   | `"Liz and The Blue Bird.".lower()` returns `"liz and the blue bird."`                                                      | Returns a `str` object with all uppercase characters from the original string lower-cased. |
| `upper()`   | `"Liz and The Blue Bird.".upper()` returns `"LIZ AND THE BLUE BIRD."`                                                      | Returns a `str` object with all lowercase characters from the original string upper-cased. |

_**Figure 1**: Some useful `str` methods in this class 
([**Full list**](https://docs.python.org/2.5/lib/string-methods.html))._

There are obviously...a lot of them. But you don't have to memorize all of them. They're all pretty intuitive and self-
explanatory, so it's actually really easy to remember them.

**NOTE**: You may ***not*** yet use `split()` or any other method that returns a `str` object into a `list` object or
any other object that we haven't seen yet. This will be penalized in homework, so please always ask if you are unsure
whether you are allowed to use something or not.

### Part 7: _String Operations_

#### _Concatenation_

Okay, so if you can't modify strings, but your program requires you to put a bunch of strings together, what do we do?

Python makes this extremely easy for us, actually. We can quite literally add two strings together by using the `+` 
operator. This process is called **string concatenation**:

```python
first_name = "Camille"
last_name = "Pissarro"
full_name = first_name + " " + last_name

print(full_name)
```
Output:
```commandline
Camille Pissarro
```

Nothing we haven't seen before. We just have a name for it now. Again, remember neither `first_name` nor `last_name` are
being modified in any way here. All Python is doing here is extracting the contents of `first_name` and `last_name` and
creating a completely new string out of them, `full_name`.

What about this example?

```python
first_name = "Camille"
last_name = "Pissarro"
full_name = first_name + " " + last_name
age = 73
full_info = full_name + ", " + age

print(full_info)
```

Output:

```commandline
Traceback (most recent call last):
  File "<input>", line 5, in <module>
TypeError: can only concatenate str (not "int") to str
```

Ah-hah. We've seen this error before. You cannot concatenate a `str` and an `int`. So if you want to create a new string
from these components, you have to **explicitly convert all non-`str` components into `str` objects**:

```python
first_name = "Camille"
last_name = "Pissarro"
full_name = first_name + " " + last_name
age = 73
full_info = full_name + ", " + str(age)

print(full_info)
```

Output

```commandline
Camille Pissarro, 73
```

We didn't have to do this when we were composing `print()` statements because `print()` takes care fo the type 
conversions for us. But more often than not, we will not be able to rely on `print()` so it's important to know how to
do it yourself.

#### _Slicing_

The second important operation that we can do with strings is _slicing_ them—that is, extracting a specified subsection.

We, of course, already learned how to index a string, which is technically a form of slicing:

```python
>>> "Ahmad Jamal"[4]
'd'
```

But, just like with the `range()` function, we have the power to define our starting, ending, and stepping value using
the following syntax:

```python
>>> "Ahmad Jamal"[2:7]
'mad J'
```

```python
>>> jazz_musician = "Ahmad Jamal"
>>> jazz_musician[2:len(jazz_musician):2]
'mdJml'
```

---

<sub>**Previous: [Control-Flow Structures: The `for`-Loop](/lectures/08_for_loops)** || **[Next: Functions: _Parameters_](/lectures/10_functions_params/)**</sub>