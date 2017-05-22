---
title: Sailor-Wheel
category: project
layout: page
---

[Sailor-Wheel](http://sizhky.github.io/Wheel-Puzzle) puzzle is a js based game that my friend and I have done in a week, as a way to build momentum in building more games together.  
The concept is pretty self explanatory - Spokes around a wheel need to be 'pulled' out by point and click. The catch being a network of internal connections that push and pull spokes when any single spoke's state is modified. The player needs to figure out these cause-effect rules and manage to pull out all the spokes.

<!--more-->
![][image1]
<div class = 'caption'>Home Page</div>

The rules are generated randomly at every level and keeps the game dynamic and repeater friendly. However the main bug is to be that the rules, being absolutely random, can generate impossible levels to solve and that pretty much ruins the streak.
That said I am figuring out the mathematics underneath the impossibility of a level and make sure the code only generates those that can be solved. You are free to download the source-code and play with it yourself - the entire game is a single .html file.

[image1]:{{site.baseurl}}/assets/project/sailor-wheel.png