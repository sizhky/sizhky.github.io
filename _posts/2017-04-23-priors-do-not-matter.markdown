---
layout: post
title:  "Priorities Don't Matter"
date:   2017-04-23 22:21:04 +0530
categories: posts
hidden: true
---
<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
This is a follow up post to my [previous blog post]({% post_url 2016-11-01-all-your-bayes-are-belong-to-us %}) explaining the A-Z of bayes. 

The argument that someone is using a 373-faced dice to produce the following 

> 3, 4, 2, 5, 4, 6, 4, 7, 4   

dice rolls is discussed in it. 

The post could be summarized into the following steps

1. Set the hypothesis space - $$H_i$$
2. Set the prior probability of each hypothesis - $$P(H_i)$$
2. Calculate the likelihoods of each hypothesis for the seen data - $$L(H_i)$$
3. Report the posterior probabilities of each hypothesis - $$P(H_i)*L(H_i)$$

The prior probabilites show half the impact in reporting the posterior. That means, if someone *does* set a high prior probability for that hypothesis then it looks like the posterior probability will be high. Let's see how the results work themselves out when we set the last hypothesis' probability to 99.5%, leaving the other 0.5% shared by the other 29 hypotheses.

<img src = '/assets/bayes/extreme priors.bmp' width="2000px" style="margin-top: 10px">
<div class = 'caption'>Stubborn priors result in...</div>
<img src = '/assets/bayes/same posteriors.bmp' width="2000px" style="margin-top: 10px">
<div class = 'caption'>The same posteriors</div>
It's almost funny how there's still a 1.3% chance that it is a 29+ faced dice. But the drop from 99.5% after just 9 data points is a statement that with more data points the probability will go even low.<br/> The bottom line is, priorities don't matter if there's enough evidence