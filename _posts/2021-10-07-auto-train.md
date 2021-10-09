---
layout: post
title:  "AutoTrain - Part 0"
date:   2021-10-07 16:45:00 +0530
categories: posts
---

What if there is a framework that uses SOTA techniques to train Deep Learning models that needs (almost) no coding?

<!--more-->

## Deep Learning can be overwhelming

The barrier to data science is usually high. One has to learn a lot of concepts both theoritical and practical before building anything meaningful. This barrier has been brought down to a large extent by excellent libraries such as *keras, pytorch-lightning, spacy and fastai* which tend to abstract away a lot of complexities and expose state of the art practices into one line functions. Data scientists still have to write significant code to preprocess, postprocess their datasets as well as any custom functions such as augmentations - not to mention the repetitive code of connecting the individual pieces as well as boilerplate code. 

From countless experiments we have understood that there are some moving parts in an ML pipeline and the rest are fixed. We treat the moving parts as **ingredients** and the fixed parts as **recipe**

Stuff specific to data, model and training will change with every experiment as shown below
<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FjtyPVcszoV6yvfbfGapRNT%2Fautotrain-moving-parts%3Fnode-id%3D0%253A1" allowfullscreen></iframe>
<div class='caption'>Ingredients</div>

Whereas the overall pipeline largely remains the same.
<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FIfYiHaXDI9jyeGfRrpvYDH%2Fautotrain%3Fnode-id%3D0%253A1" allowfullscreen></iframe>
<div class='caption'>Recipe</div>

It is meaningful to abstract away the fixed parts into static files and keep the moving parts as accessible as possible. Libraries like mmdetection and spacy-projects rely heavily on configuration files to achieve this. Usually these are coded to be domain specific and cannot be extend to personal tasks. One more downside to such config based libraries is that the fixed components have multiple layers of inheritences making the library somewhat cryptic for a beginner to understand - ending up having a hard time debugging if something goes wrong.

Our library - [AutoTrain](https://github.com/sizhky/AutoTrain) - tries to bring in the best practices from all such libraries to help you build a platform from scratch that will achieve the following  
* you are in complete control of the code base  
* project structure along with configuration makes the whole pipeline efficient  
* all the moving parts, and only the moving parts of an experiment are exposed in a config file (and one more python file for custom functions) 
* rest of the parts are static but debuggable  

The outcome is an easy maintain code with few files to worry about. This let's you run experiments where the outcome is dictated only by the configuration file. 

It is better to break AutoTrain into the following blogs for a clean understanding of all components  
* [Part 1: Config First Approach a.k.a., Ingredients]({% post_url 2021-10-07-auto-train-config %})  
* [Part 2: Standardizing SOTA]({% post_url 2021-10-09-auto-train-boiler-plate %})  
* [Part 3: Use Cases]({% post_url 2021-10-09-auto-train-use-cases %})  
