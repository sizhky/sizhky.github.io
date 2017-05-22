---
layout: post
title:  "XOR using MultiLayered Perceptron"
date:   2016-10-28 13:48:42 +0530
categories: posts
---

Historically, almost every non-tree based ML algorithm created only linear separable spaces, and the XOR simply cannot be modeled with them. Enter [the multilayerd perceptron](https://www.coursera.org/learn/machine-learning/lecture/solUx/examples-and-intuitions-ii) (MLP) and everything changed. With an elegant chaining of linear combinations of inputs we can obtain almost any number of linear decision boundaries. So I thought I'd bulid a robust XOR gate using a simple MLP
<!--more-->

| x<sub>1</sub>|x<sub>2</sub> | y |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
|1  | 0 | 1 |
|  0| 1 | 1 |
| 1 | 1 | 0 |

<div class = 'caption'>Truth table of XOR </div>

The goal was to create a network which can learn these four points with as minimal setup as possible. And that would be one with one layer each for input, hidden and output nodes where the hidden layer has 2 neurons only. 

![](/assets/xor/nn architecture.jpg)
<div class = 'caption'>Simple MLP! </div>

To fit four points using a neural network is simple. Right? 

![](/assets/xor/zero loss on simple nn.bmp)
<div class = 'caption'>Loss on an XOR data. Done and dusted! </div>

It turns out, no. While it did classify correctly most of the times, there were instances when the network simply wouldn't converge. 

![](/assets/xor/loss on simple nn.bmp)
<div class = 'caption'>Why you no converge to zero? </div>

Why can't it fit four points? Is Andrew Ng wrong when he [claimed](https://www.coursera.org/learn/machine-learning/lecture/solUx/examples-and-intuitions-ii) that a simple MLP can predict XOR? The answer: It depends on the way the weights are initialized. This will dictate, at which local minimum is the network going to converge.

To dig deeper into this I created a 3D graph of y vs (x<sub>1</sub>,x<sub>2</sub>) where z-axis is y, the output of our simple MLP. And depending on the weights the MLP will have a different linear separators and heights for each plateau. 

![](/assets/xor/input output of a simple mlp.bmp)
<div class="caption">There are four plateaus for a simple MLP</div>

The interesting observation is that a pair of plateaus on the opposite corners necessarily have highest and lowest z value. And this actually means a simple MLP can **never** fit an XOR gate since the ideal gate should have the opposite quadrants on same heights. This got me confused. Where does Andrew Ng's claim fit into the picture? The answer is, the weights were built to fit the data. And this needn't happen with random initializations.

![](/assets/xor/special weights.gif)
<div class = "caption">Notice how (0,1) and (1,0) are in the valley while (0,0) and (1,1) are on the plateaus</div>

This made me rethink my model. XOR is not about fitting four points, but working with the entire cartesian plane. 

|       x<sub>1</sub>     |     x<sub>2</sub>       | y |
|:------------:|:------------:|:-:|
| negative     | negative     | 0 |
|positive      | negative     | 1 |
|  negative    | positive     | 1 |
| positive     | positive     | 0 |

<div class="caption">Modified XOR</div>

And this way, I generated thousands of pairs of real numbers (x<sub>1</sub>, x<sub>2</sub>) each between -10 and 10 and their corresponding y values. Almost every training instance gave only 85% accuracy.

![](/assets/xor/ideal vs computed.png)
<div class = "caption">Ideal XOR vs Computed. <br>The red circles on the right show the errors which a simple 2 node MLP cannot calculate.</div>

This once again shows that a simple MLP **cannot** fit XOR data. The workaround is to increase the number of nodes in the hidden layer, and this in turn creates multiple plateaus which will only fit the data and not generalize   

[//]: #P.S.  
[//]: #[They](https://www.tensorflow.org/versions/r0.11/tutorials/mnist/beginners/index.html) [say](https://deeplearning4j.org/mnist-for-beginners) [MNIST](lasagne.readthedocs.io/en/latest/user/tutorial.html) [is](https://db-blog.web.cern.ch/blog/luca-canali/2016-07-neural-network-scoring-engine-plsql-recognizing-handwritten-digits) the hello world of neural networks. MNIST is a collection of 28x28 pixel images of handwritten digits, which the neural network is supposed to classify.  
[//]: #IDK why it's the hello world when there is a much more simpler input to work with, the infamous XOR gate.  
[//]: #P.P.S  
[//]: #I had a break from work for a couple of days and planned on learning recurrent neural networks. It turns out that to understand them I needed to understand backpropagation, to understand which I needed to understand forward propagation, to understand which I need to make sense of the basic MLP. So I decided to create a simple working example of an XOR gate with two inputs (x<sub>1</sub> and x<sub>2</sub>) and one output (y). y is 1 when x<sub>1</sub> and x<sub>2</sub> have opposite signs and 0 otherwise.