---
layout: post
title:  "Learn Python in One Hour (?)"
date:   2024-07-08 20:35:38 +0530
categories: posts
---

I took it as a challenge to teach someone who has no idea of python to get started in 1 hour

<!--more-->

Go to [colab.research.google.com](https://colab.research.google.com) and open a new notebook. You're ready to execute python!

```python
x = 1
y = 2
```
Just like algebra!  
x and y are a variables and they can be changed anytime

Now you can - 
```python
print(x+y)
print(x-y)
print(x*y)
print(x/y)
```
Just like math! `+`, `-`, `*` and `/` are what you think they are, addition, subtraction, multiplication and division

Let's learning about printing

- You want to print multiple things? Separate them with a comma

```python
print(x, y)
# this should print a `1 2` in the output
```
> What is the `#` doing in my code?
>> All lines that start with a `#` are called comments 
>> and are used for communicating stuff to the reader

- You want to separate x and y with something other than a space? Use

```python
print(x, y, sep=';')
# this should print a `1;2` in the output
```
> What just happened?
>> - Well, print is a function. 
>> - All functions take two kinds of inputs: arguments and keyword-arguments
>>   - arguments → Those that are directly fed to the function. Order usually matters
>>     E.g., `func(y,x,z,a,b,c)`
>>     `x`, `y`, `z`, `a`, `b` and `c` are called arguments to the function
>>   - keyword arguments → Those that are of the form 
>>     `func(..., key1=value1, key2=value2, ...)`
>>   - all arguments and keyword arguments are separated by a comma in python

- You want to print "x=1 and y=2"? Just wrap your variables with the text you want.

```python
print(f'{x=} and {y=}')
# should print `x=1 and y=2`
```
- You don't want to print `x=` and `y=` and need more control? Just remove the equal to symbol

```python
print(f'ex is equal to {x} and why = {y}')
# ex is equal to 1 and why = 2
```

<details> <summary> What is going on? What is `f'` and what are `{}` brackets doing in my code?️️️ </summary> In Python, f'...' denotes an **f-string**, which is a way to format output by mixing text and variables. The {} brackets within an f-string are used to include variables inside the string, allowing you to create dynamic outputs. 
</details>

