---
layout: post
title:  "Tokenizers in Telugu Text"
date:   2018-08-02 02:00:00 +0530
categories: posts
---

సహస్రనామావళి (range of 1000 names) are commonly associated with Hindu Gods/Goddesses where a Deity's  characterestics are propounded with as many names. I've gotten interested in [Garikapaati Narasimha Rao](https://www.youtube.com/watch?v=Sq1PlEo-sWY)'s talks and specifically one called శ్రీ లలితా సహస్రనామావళి (Lalitha sahasranamam). At a junction he explains about the counts of her names grouped by the first character and how a few groups have a lot more names compared to others. I took it as a small task to work with telugu NLP and count these groups

<!--more-->

The text was downloaded from [here](https://stotras.krishnasrikanth.in/sri-lalitha-sahasranama-stotram/) and later cleaned

```python
with open('lalitha-sahasranaamam.txt', 'r') as f:
    txt = f.read()

print(txt[:1500], '...')

'''
ధ్యానమ్ 
సిందూరారుణవిగ్రహాం త్రినయనాం మాణిక్యమౌళిస్ఫురత్
తారానాయకశేఖరాం స్మితముఖీమాపీన వక్షోరుహామ్ 
పాణిభ్యామలిపూర్ణరత్నచషకం రక్తోత్పలం బిభ్రతీం
సౌమ్యాం రత్నఘటస్థరక్తచరణాం ధ్యాయేత్పరామంబికామ్

అరుణాం కరుణాతరంగితాక్షీం ధృతపాశాంకుశపుష్పబాణచాపామ్ 
అణిమాదిభిరావృతాం మయూఖైరహమిత్యేవ విభావయే భవానీమ్

ధ్యాయేత్పద్మాసనస్థాం వికసితవదనాం పద్మపత్రాయతాక్షీం
హేమాభాం పీతవస్త్రాం కరకలితలసద్ధేమపద్మాం వరాంగీమ్ 
సర్వాలంకారయుక్తాం సతతమభయదాం భక్తనమ్రాం భవానీం
శ్రీవిద్యాం శాంతమూర్తిం సకలసురనుతాం సర్వసంపత్ప్రదాత్రీమ్

సకుంకుమవిలేపనామళికచుంబికస్తూరికాం
సమందహసితేక్షణాం సశరచాపపాశాంకుశామ్ 
అశేషజనమోహినీం అరుణమాల్యభూషాంబరాం
జపాకుసుమభాసురాం జపవిధౌ స్మరేదంబికామ్

లమిత్యాది పంచపూజాం కుర్యాత్ 
లం – పృథ్వీతత్త్వాత్మికాయై శ్రీలలితాదేవ్యై గంధం పరికల్పయామి 
హం – ఆకాశతత్త్వాత్మికాయై శ్రీలలితాదేవ్యై పుష్పం పరికల్పయామి 
యం – వాయుతత్త్వాత్మికాయై శ్రీ లలితాదేవ్యై ధూపం పరికల్పయామి 
రం – వహ్నితత్త్వాత్మికాయై శ్రీ లలితాదేవ్యై దీపం పరికల్పయామి 
వం – అమృతతత్త్వాత్మికాయై శ్రీ లలితాదేవ్యై అమృతనైవేద్యం పరికల్పయామి

స్తోత్రమ్

ఓం శ్రీమాతా శ్రీమహారాజ్ఞీ శ్రీమత్సింహాసనేశ్వరీ 
చిదగ్నికుండసంభూతా దేవకార్యసముద్యతా

ఉద్యద్భానుసహస్రాభా చతుర్బాహుసమన్వితా 
రాగస్వరూపపాశాఢ్యా క్రోధాకారాంకుశోజ్జ్వలా

మనోరూపేక్షుకోదండా పంచతన్మాత్రసాయకా 
నిజారుణప్రభాపూరమజ్జద్బ్రహ్మాండమండలా

చంపకాశోకపున్నాగసౌగంధికలసత్కచా 
కురువిందమణిశ్రేణీకనత్కోటీరమండితా

అష్టమీచంద్రవిభ్రాజదళికస్థలశోభితా 
ముఖచంద్రకళంకాభమృగనాభివిశేషకా

వదనస్మరమాంగళ్యగృహతోరణచిల్లికా 
వక్త్రలక్ష్మీపరీవాహచలన్మీనాభలోచనా

నవచంపకపుష్పాభనాసాదండవిరాజితా 
తారాకాంతితిరస్కారినాసాభరణభాసురా

కదంబమంజరీక్లప్త ...

'''
```

A few lines in the beginning and end were invocations and expositions. So I discarded them. Apart from the obvious `\n` and `space` I also noticed `ఽ` was separating valid names in the text. So I wrote a custom function that can take any number of candidiate splitters and return tokens

```python
def split_on(string, splits):
    string = [string]
    for s in splits:
        string = [part for subpart in string for part in subpart.split(s)]
        
    string = [s for s in string if s!='']
    return string

tokens = [' ', '-', 'ఽ']
```

I went ahead and tokenized the text as follows
```python
N = '\n'.join(txt.split('\n')[28:-4]) # first 28 were invocations and last 4 were blank, the way I preprocessed
n = N.split()
_n = []
for idx, n_ in enumerate(n):
    _n.extend(split_on(n_, tokens))
n = _n
print(f'Number of names found: {len(n)}')

'''
Number of names found: 998
'''
```
The names have not been perfectly extracted. On the whole it seems like 2 names are missing, but there will be more due to the nature of combinations of words (as the language calls it సంధులు). 

```python
enum = lambda x: list(enumerate(['']+x))
enum(n[1:20])

'''
[(0, ''),
 (1, 'శ్రీమాతా'),
 (2, 'శ్రీమహారాజ్ఞీ'),
 (3, 'శ్రీమత్సింహాసనేశ్వరీ'),
 (4, 'చిదగ్నికుండసంభూతా'),
 (5, 'దేవకార్యసముద్యతా'),
 (6, 'ఉద్యద్భానుసహస్రాభా'),
 (7, 'చతుర్బాహుసమన్వితా'),
 (8, 'రాగస్వరూపపాశాఢ్యా'),
 (9, 'క్రోధాకారాంకుశోజ్జ్వలా'),
 (10, 'మనోరూపేక్షుకోదండా'),
 (11, 'పంచతన్మాత్రసాయకా'),
 (12, 'నిజారుణప్రభాపూరమజ్జద్బ్రహ్మాండమండలా'),
 (13, 'చంపకాశోకపున్నాగసౌగంధికలసత్కచా'),
 (14, 'కురువిందమణిశ్రేణీకనత్కోటీరమండితా'),
 (15, 'అష్టమీచంద్రవిభ్రాజదళికస్థలశోభితా'),
 (16, 'ముఖచంద్రకళంకాభమృగనాభివిశేషకా'),
 (17, 'వదనస్మరమాంగళ్యగృహతోరణచిల్లికా'),
 (18, 'వక్త్రలక్ష్మీపరీవాహచలన్మీనాభలోచనా'),
 (19, 'నవచంపకపుష్పాభనాసాదండవిరాజితా')]
'''
```
It looks fine for a first try. When I inspected, there were quite a lot of mistakes.  
E.g. the line 
>స్వాహా స్వధాఽమతి-ర్మేధా శ్రుతిః స్మృతి-రనుత్తమా 

is divided into

`స్వాహా`, `స్వధా`, `మతి`, `ర్మేధా`, `శ్రుతిః`, `స్మృతి`, `రనుత్తమా`

where it is supposed to be 

`స్వాహా`, `స్వధా`, `అమతి`, `మేధా`, `శ్రుతిః`, `స్మృతి`, `అనుత్తమా`

In telugu (and a few Indian languages I know of) when you combine words, sometimes news sounds between the words are generated, and sometimes removed based on the context. This is the reason for the wrong names while splitting.

However, it is noteworthy that even though many of the tokens are (partially) wrong, the _number_ of tokens is preserved due to poems following the metre.

Despite these mistakes (which I invite the reader to think about and propose possible solutions) I went ahead with my counting of names, grouping by starting character.

```python
from collections import Counter

counter = Counter()
for n_ in n:
    counter[n_[0]] += 1

print(counter.most_common(6))

'''
[('స', 124), ('మ', 105), ('క', 92), ('ప', 83), ('వ', 82), ('న', 77)]
'''
```

There are a significant number of them starting with 'స' and 'మ'. Incidentally, the speaker at in the video below tells how it is not a fluke that those two happen to be the characters with most names because the characters combined `సమ` means equanimity, gaining which, is reaching Devi. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/6IFss8UBllI?t=31m20s&start=1880" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

