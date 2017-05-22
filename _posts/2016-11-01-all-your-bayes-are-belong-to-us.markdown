---
layout: post
title:  "A to Z Bayes - Part 1: The Basics"
date:   2017-04-21 19:45:49 +0530
categories: posts
---
<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
Back in the days when neither of us were born, science was a pioneering concept destined to take humanity from the shore of darkness to light. The selling point was repeatability of experiments. Careful reproduction of experiments ensured that a lot of falsifiable theories stayed false. But, the method falls flat when there is an unfalsifiable hypothesis in picture. Science can never prove a hypothesis right, it can only prove it wrong. The ignorant - armed with this fact - use science to say:

> "Evolution is just a theory. It could be God as well and you can't prove me wrong!".  

If everything is 'just a theory' then which one is the right theory?
<img src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Bayes_sig.svg/800px-Bayes_sig.svg.png' width="300px" style="margin-top: 10px">
<div class = 'caption'>Take a dose of Bayes before sleep for sanity.</div>

<!--more-->

Using the scientific method meant only one thing. The wrong will be disproved. And the hope is that if a right theory springs up it will explain nature until there comes an observation which cannot be explained (consider, Newton's laws for example - While it lasted for centuries, unchallenged, it could never explain what theory of relativity could predict). And in science that means we discard the wrong and embrace the new/temporary right theory. Evidendtly, there is a big  issue that cannot be dealt with using the scientific method - multiple hypotheses which fit the data. In other words, smart-asses who come up with all sorts of theories which can't be proved wrong.

## Let's Experiment
Let us work with a thought experiment and I'll try to explain the bayes way of thinking as we go along. I have a dice whose number of faces is a question for you to figure out. What I will tell you is this - when I rolled the dice 9 times the following numbers showed up -  

>  3, 4, 2, 5, 4, 6, 4, 7, 4 

Alluding to the above quote referring to evolution, I can argue that I used a *373-faced dice* and there's no way to prove me wrong. *But it just. doesn't. feel. right.* that I would have used that particular dice. How *do* you prove me wrong then? What is the number of faces of the dice that I have used? Can we make a reasonable guess atleast?
Take your time to solve the problem.

<p class="side-note">On a side note, isn't this how the world works? All we have at hand is the data and not the process which got us the data. It's upto us to find out which process was likely responsible.</p>

'Common sense' dictates that the dice must have at least 7 faces or else we would never have seen a seven in our data. Techincally speaking we've done a bayesian update on our hypotheses space. But we are jumping to incomplete conclusions. Let's take a step back and solve the problem the right way, the bayesian way.  

### Step 1: Figuring out the hypothesis space
Before we've even seen the data all we could've told is that the dice can have the number of faces as any integer between 2 and infinity. And each such possibile reality is called as a **hypothesis** (plural - hypotheses). The set of all hypotheses is called as the **hypothesis space** and we need to figure out which one is the most probable hypothesis among them.  


<img src = '/assets/bayes/priors.png' width="2000px" style="margin-top: 10px">
<div class = 'caption'>Hypothesis Space and Prior Probabilities of each hypothesis.<br/>For example the prior probability for the hypothesis '10 sided dice' is approx 0.04.<br/>Note that all the heights must sum to 1.</div>
<br/>Since we couldn't have all the infinite integers we chose the last hypothesis as *'any dice with greater than 28 sides'*  

### Step 2: Figuring out the probabilities of hypotheses **(Priors)**
The wisdom in thinking like a bayesian lies in setting the probabilities to this hypothesis space. Firstly the sum of all the probabilities of these hypotheses sum upto one. Generally speaking, we set larger probability to events that have happened more in the past.  

To give an idea of what I'm talking about - 'experience' tells us that the probability that I own a 373 faced dice is really small. The number of times one has seen such a dice is non-existent (what about a 10 Million faced dice?) but it's not impossible. So we set a probability of seeing that hypothesis as almost zero. What we do often see are dice with a fewer faces and the probabilities better reflect that. (Strictly speaking, the [priors don't matter]({% post_url 2017-04-23-priors-do-not-matter %}) when we have enough evidence)

### Step 3: Figuring out the probability of seeing the data under each hypothesis. **(Likelihood)**
Once the hypotheses are set, we compute the probability of seeing our data in each of the hypothesis. This is a realitively easy and straight forward step. In the case of an *n sided fair dice* the probability of seeing a number *k* show up is 1/n irrespective of k as long as k <= n and 0 if k > n. 

<center>
\[
P(k|N-sidedDice) = 
\begin{cases}
  \ \frac{1}{n} & \text{if}\ k \leq n \\
  \ 0 & \text{if}\ k > n
\end{cases}
\]</center>
Hence the probability of a dice showing the above 9 data points is $$\frac{1}{n}$$ for all $$n \geq 7$$. This renders 2, 3, 4, 5 and 6 faced dices to have zero likelihood since probabilty of a 7 occuring in these cases is zero. Thus we have a likelihood for each hypothesis.
<img src = '/assets/bayes/likelihoods.png' width="2000px" style="margin-top: 10px">
<div class = 'caption'>Likelihoods of my hypotheses<br/>Probabilities of 2-6 are zero.</div>

### Step 4: Multiply Priors and Likelihoods **(Posterior)**
This should be the easiest of all. Simply multiply the prior probabilities of each hypothesis with their own likelihoods. That's it! We have the relative probabilities for each hypothesis that reflect the seen data. A small issue here is that the sum of these don't add up to one so we normalize to get them as actual probabilities.

### Step 5: Profit $$
Firstly, the probability of me choosing fewer faced dice is an absolute 0, which aligns with our intuition like we have shown above and the scientific method.  
We still can't deny the fact that I have used a *373-faced dice* since the posterior probability is non-zero. Using the bayesian approach we presupposed that such a dice, firstly, is a rare occurance and secondly, has lower likelihood compared to a fewer faced dice. However, we calculated that the posterior probability of a *373-faced dice* is miniscule compared to other hypotheses. This asserts that such a dice usage is far rare if not impossible. Bottom line is that we can idiot proof our arguments by not getting confused between a probable hypothesis with an extremely uncommon hypothesis.  
<p class="side-note">Now can you see why evolution deniers are wrong?</p>
