---
layout: post
title:  "The Kernel Trick in Neural Networks"
date:   2017-11-09 07:39:38 +0530
categories: posts
---

Data-science is the science of finding patterns in data. Given lots and lots of points on a 2D plane, they could all be lying on a line, or on an organized pattern (maybe they all form a circle), or there could be clumps of data here and there, or a combination of both (maybe they are all on *two* circles). 

All the machine learning algorithms are specialized to do one or more of these tasks, i.e., finding the line(s) of best fit [such as Linear Regression] or finding the line(s) of best separation [such as Decision trees, Logistic regression], or both [such as SVMs and Neural Networks]

Even more basically, data-science is about finding lines. And linear regression is the easiest to explain. Find the coefficients of that line which has maximum overlap with the points, in case of regression and that line which divides the points most. But there is an obvious assumption in the method. That data is linearly separable. This is not true. Never true, in fact. There will always be that curve which can separate the clouds more evenly. And hence the need for non-linear models. 

The kernel trick is one of the coolest things I've learned in ML. We have bulit methods that are fundamentally based on drawing lines (Linear Regression, SVM or NN can ultimately only draw lines). However the genius of kernel trick is to *transform* the data such that the clouds simply go apart and a line can then be drawn.

<p class="side-note">Think of it like this. There is a river separating the land into two. We can think of lands separated by a crooked line, or if the land itself were to be stretched like a blanket, with the right kind and amount of stretching the river <b>looks</b> straight and the two lands on both sides warped. </p>

That's the simple trick. SVM and (for this particular topic) Neural Networks are basically about that. While SVM has an explicit bais about the type of kernel that must be used, Neural Networks take it a step further and finds its own kernel.

<!--more-->
<br/>
## Experiment

*Let's start with a simple cloud of data where the blue points are in a circular disc and the orange points are surrounding the disk*
<img src="/assets/kerneltrick/0.png" style="margin-top: 10px"/>
<div class="caption">There is no way a single line could ever separate this data</div> 

As you can see in the above network, the inputs fed are `(x, y)` of the point. Then each point is transformed into a 3 dimnesional hidden space of `(h1, h2, h3)` axis data (and hence the `three neurons`, which is then brought back into the 2 dimensional `(orange, blue)` axis space. The transformation from inputs to hidden dimensions is caused by a weight matrix whose dimensions would be `(2, 3)` (2 dimensional data being transformed into 3 dimensional data). 
<p class="side-note">This transformation is the root of all matrix algebra and vector algebra</p>
<p class="side-note">Also, the process of finding the right weight matrices, a.k.a., back-propagation is another genius trick that we could talk some other time</p> 


<img src="/assets/kerneltrick/1.png" style="margin-top: 10px"/>
<p class="caption">Initially for the machine all the data is simply there on the ground. Just lying. No redness or blueness attached. It knows nothing, like John Snow.</p>
But fter the first transformation the points are shot into 3d space.
<img src="/assets/kerneltrick/2.png" style="margin-top: 10px"/>
<img src="/assets/kerneltrick/2.1.png"/>

You can already see how the two circles are two *triangles* in 3D. From the second perspective it is clear that one could cut a slice of the cube with a slant plane and have the two triangles on two sides of it. Techincally we have made the data *linearly separable*.

The second transformation is again bringing the data back into 2 dimensions. However the projection is from a different vantaget point such that the two clusters remain separate.
<img src="/assets/kerneltrick/3.png" style="margin-top: 10px"/>
<img src="/assets/kerneltrick/3.1.png"/>

The softmax layer is a special transform which simply returns a 'yes'/'no' kind of output for every class. The last transformation looks like this
<img src="/assets/kerneltrick/4.png" style="margin-top: 10px"/>

This process is exactly what we meant by the kernel trick. By saying neural networks can find their own kernels, we mean -
1. it can take data into any higher/lower/same dimensions we specify.
2. it can do that as many times as there are hidden layers.
3. if it finds a right combination of these transforms *(this is automaticallly done by back-propagation which is a topic for another day)* the data becomes linearly separable.