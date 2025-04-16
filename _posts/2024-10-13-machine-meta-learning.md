---
layout: post
title: "Machine Meta Learning"
date: 2024-10-05 14:35 +0530
categories: posts
---

  
Large Language Models (LLMs) are primarily rote learners. They can answer straightforward calculations like \(1 + 1 = 2\) because they have seen enough examples in their training data to predict the token `2` when given the sequence of tokens `1`, `+`, `1`. However, this approach breaks down when faced with more complex problems, such as:

<!--more-->
  
```python
>>> 1231212 + 12311131
Let me calculate the result for you:
  
1231212 + 12311131 =
  
First, I'll add the two numbers together:
  
1231212
+ 12311131
--------
24623243
```

but the actual answer is: 13542343

LLMs lack true reasoning capabilities. They might answer questions like Zeno’s Paradox or solve the Wolf, Goat, and Cabbage Problem because there are numerous examples online. But when presented with a twist, they often falter:
  
Example:
_Which is heavier? A pound of cotton wetted by the rain or a pound of tungsten pellets?_

An LLM might respond that both weigh the same because they are specified as a pound. However, this answer can be ambiguous without clarification on whether a one pound cotton was wetted (making it heavier) or if the wet cotton weighs one pound.

Consider a scenario 

```
you observe the following growth of lotuses in a pond:

• On January 1st: 1 lotus.  
• January 2nd: 2 lotuses.  
• January 3rd: 4 lotuses.  
• January 4th: 16 lotuses.  
  
When you return on January 30th and see the pond half full, you might ask: _How many more days until the pond is completely filled?_

```

An LLM can fail in any number of ways as there are a few moving components. Here's what llama3 gave -

```
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

In fact, a recent study from Apple demonstrated that all state-of-the-art LLMs exhibit significant performance variations, indicating fragility in their reasoning abilities. 

Questions from the GSM8K dataset were templatized to generate new variations, like so,

<img src='https://i.imgur.com/TeBhAUD.png' alt='image' style='max-height: 600px; width=auto;'>


and the resulting accuracy distributions suggested that LLMs often guess answers based on token prediction rather than true comprehension.

<img src='https://i.imgur.com/ksZruxa.png' alt='image' style='max-height: 600px; width=auto;'>

  
Machines Should Learn How to Learn
  
Consider the following datasets for teaching machines to translate numbers into words:
  
Dataset 1:
```
117502964426 -> one hundred and seventeen billion five hundred and two million nine hundred and sixty-four thousand four hundred and twenty-six
455237208077 -> four hundred and fifty-five billion two hundred and thirty-seven million two hundred and eight thousand seventy-seven
698096686169 -> six hundred and ninety-eight billion ninety-six million six hundred and eighty-six thousand one hundred and sixty-nine
928537308484 -> nine hundred and twenty-eight billion five hundred and thirty-seven million three hundred and eight thousand four hundred and eighty-four
70833109621 -> seventy billion eight hundred and thirty-three million one hundred and nine thousand six hundred and twenty-one

... and a billion more examples ...
```
  
Dataset 2:

```
1. Understand Place Values: Teach the different place values (units, tens, hundreds, thousands, millions, billions, etc.).
2. Break Down the Number: Explain that large numbers can be segmented into groups of three digits.
3. Learn Basic Number Words: Ensure the machine knows the words for numbers 1 to 20 and larger multiples.
4. Combine Place Value and Number Words: Show how to combine number words with their corresponding place values.
```

The first method uses hyper-specialized examples, resulting in a system adept at its specific task but incapable beyond it. This mirrors current LLMs - highly proficient at predicting the next word, creating an illusion of reasoning, yet fundamentally limited.

The second approach requires a foundational understanding of English grammar before tackling the conversion task. This method builds on existing knowledge, enabling the system to expand its capabilities incrementally. 

While LLMs might handle this via one-shot learning and chain of thought, some problems demand ground-up reasoning rather than token prediction. 

In essence, LLMs are sophisticated next-token predictors. To advance AI, we need training schemes incorporating diverse loss functions, fostering fundamental reasoning skills rather than mere pattern matching.