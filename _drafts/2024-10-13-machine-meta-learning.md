---
layout: post
title:  "Machine Meta Learning"
date:   2024-10-05 14:35 +0530
categories: posts
---

We know what is an LLM. Now it's time to know about MML.

<!--more-->

heading: LLMs are rote learners. 

It knows 1+1=2 because there are sufficient examples in the training data and it was trained to predict the token `2` when the input tokens were `1`, `+`, `1` in that sequence.
that is why llms fail when you give something complex like 1231212 + 12311131

```llama3
>>> 1231212 + 12311131
Let me calculate the result for you:

1231212 + 12311131 =

First, I'll add the two numbers together:

1231212
+ 12311131
--------
24623243

So the result is: 24623243
```

llms cannot reason. 
it can answer the `Zeno's paradox` 
it can solve `The Wolf, Goat, and Cabbage Problem` 
because there are so many examples over the internet. 

Give it something with a twist and it will fall apart
```
which is heavier? A pound of cotton wetted by the rain or a pound of tungsten pellets that are somewhat small?
```

it will tell you that a pound of tungsten and a pound of cotton weigh the same. because there are so many examples over the internet.

```gpt4-o
Both the wet cotton and the tungsten pellets weigh the same: **one pound**, since the question specifies they each weigh a pound. The materials may differ in density, but the weight is defined as equal in this case. However, the wet cotton would feel bulkier and larger in volume, while the tungsten pellets would be denser and more compact.
```

But this is ambiguous and you need to confirm if a pound of cotton is wetted or if the wetted cotton weighs a pound.

Give it something that is not well available on the internet - 

in a pond on Jan 1st i saw 1 lotus. on second jan i saw 2 lotuses. on 3rd i saw 4 and 16 on 4th jan. i went for a business trip and came back on 30th jan to see half the pond full. how many more days is it going to take to see the pond filled with lotuses

```llama3
>>> in a pond on Jan 1st i saw 1 lotus. on second jan i saw 2 lotuses. on 3rd i saw 4 and 16 on 4th jan. i went for a business trip and came back on 30th jan to see half the pond full. how many more days is it going to take to see the pond filled with lotuses
What an intriguing problem!

Let's analyze the situation:

* On January 1st, you saw 1 lotus.
* On January 2nd, you saw 2 lotuses, which means the number of lotuses doubled (1 → 2).
* On January 3rd, you saw 4 and 16 lotuses, which is a consistent pattern of doubling. So, we can infer that the number of lotuses also doubled on this day.
* On January 4th, you didn't see an exact power-of-2 increase (e.g., 8 or 32), but since it's likely that the growth rate remained consistent, let's assume the pattern continued.

Now, let's find the number of days until the pond is filled with lotuses:

* Day 1: 1 lotus
* Day 2: 2 lotuses
* Day 3: 4 lotuses (doubled from 2)
* Day 4: 16 lotuses (doubled from 4)

Notice a pattern? Each day, the number of lotuses doubles. This means that on January 30th, when you returned and saw half the pond filled, there were likely:

* ...16 × 2 = 32 lotuses
* ...32 × 2 = 64 lotuses (on the next day)
* ...64 × 2 = 128 lotuses

And so on.

To calculate how many more days it will take to fill the pond, let's find when the number of lotuses exceeds the capacity of the pond. Since you saw half the pond filled, assume the total capacity is roughly double that: around 32-64 lotuses (a rough estimate).

From our calculations:

* Day 5: 128 lotuses
* Day 6: 256 lotuses
* Day 7: 512 lotuses

On day 7, you would likely see more than half the pond filled. However, to be precise, let's find the first day when the number of lotuses exceeds the estimated capacity (32-64):

* Day 8: 1024 lotuses (which is already above the estimated capacity)

So, it will take approximately 8 days for the pond to be filled with lotuses.

```

and it will fail

In fact a [study from apple](https://arxiv.org/pdf/2410.05229) tested and found that all state-ofthe-art LLMs exhibit significant performance variations, suggesting the fragility or lack of reasoning.

Questions from GSM8K dataset were templatized like so - 


![[Pasted image 20241013130207.png]]

to create a new dataset where one can generate a new copy of the entire dataset with different values for the variables. For copy of the dataset the llms were asked the questions in the datset and evaluated. below you can see how llms give a distribution of evaluation-accuracies for each copy suggesting that llms are guessing the answers purely based on trying to predict the next token, in other words fragile.

<img src='https://i.imgur.com/ksZruxa.png' alt='image' style='max-height: 600px; width=auto;'>

heading: machines should learn how to learn

consider the two datasets
```
117502964426 -> one hundred and seventeen billion five hundred and two million nine hundred and sixty four thousand four hundred and twenty six
455237208077 -> four hundred and fifty five billion two hundred and thirty seven million two hundred and eight thousand seventy seven
698096686169 -> six hundred and ninety eight billion ninety six million six hundred and eighty six thousand one hundred and sixty nine
928537308484 -> nine hundred and twenty eight billion five hundred and thirty seven million three hundred and eight thousand four hundred and eighty four
70833109621 -> seventy billion eight hundred and thirty three million one hundred and nine thousand six hundred and twenty one

... and a billion more examples

```

and this dataset
```
1. **Understand Place Values**:
• Teach the about the different place values (units, tens, hundreds, thousands, millions, billions, etc.).

2. **Break Down the Number**:
• Explain that large numbers can be broken down into groups of three digits, starting from the right. For example, the number 117,502,964,426 can be segmented into:
• 117 (billion)
• 502 (million)
• 964 (thousand)
• 426 (units)

3. **Learn Basic Number Words**:
• Ensure the machine knows the words for numbers 1 to 20, as well as the tens (30, 40, 50, etc.) and larger multiples (hundred, thousand, million, billion).

4. **Combine Place Value and Number Words**:
• Show how to combine the number words with their corresponding place values. For instance:
• 117 becomes “one hundred and seventeen”
• 502 becomes “five hundred and two”
• 964 becomes “nine hundred and sixty-four”
• 426 becomes “four hundred and twenty-six”
```
Both are fundamentally trying to teach how to translate a number to corresponding words. 

The first one is easy to train because the examples are hyper-specialized to the task. End of the day the program is intelligent because it's able to tell any number in its constituent words. End of the day the program is dumb because it cannot do anything else. This is what current LLMs are as of today. They have been hyper specialized to predict the next word, giving the illusion that they can reason

Second dataset is more nuanced and the neural network needs to have a basic understanding of english grammar itself before tackling the problem. In this method neural network is building on top of what it already knows. now it can do one more additional thing. granted you can say this can be treated as a oneshot example and llms are capable of doing this. my point is there are problems which need ground up thinking rather than predicting the next token. 

to summarize, llms are hyperspecialized next token predictors and we need training schemes that have more varieties of losses to learn about fundamental reasoning.