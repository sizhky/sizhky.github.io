---
layout: post
title:  "Barebones Git"
date:   2016-07-11 18:43:38 +0530
categories: posts
---

Many people I know confuse Git with Github, and probably don't have a good idea of how powerful version control is. I guess, half the trouble with it is the steepness of the learning curve, not to mention how wonky even the concept of version control is. I've had my own million doubts in using Git and never knew where to start. Even if I did start, I'd have given up on the second day not understanding why certain thing is the way it is.

This post is just for that, to de-mistify what a good tool Git is and how easy it is to integrate into the workflow and, really, master version control with only a handful of commands. I hope the days of copy-pasting a file in the name of 'backup' are a days of the past.

## Firstly...
Git is a version control software, created by [Linus Torvalds](https://www.linux.com/blog/10-years-git-interview-git-creator-linus-torvalds), the founder of Linux. [Github](github.com), on the other hand is a neat platform to share and store code along with all the goodness of git. Github, is by default, a free platform at the cost of hosting the contents visible to the public. There's a subscription service to have propitiatory projects stored online in all secrecy. Even though Git can seamlessly integrate with Github, it is however, also compatible with other code sharing platforms or just any location for that matter (ftps and shared networks, included)

## Secondly...
It's all about practice. Let's dedicate this section to setting a something to restore backups without copy-pasting a single file.

### Let's start setting up in an empty folder (I'll name it gittut)

The magic starts with initializing a Git repository

```
C:\...\>mkdir gittut

C:\...\>cd gittut

C:\...\gittut>git init
```

It means that the folder is ready for some version control action! The only visible difference would be that there is be .git folder created in the directory which is hidden by default. The takeaway point is that any location containing a .git folder means one or more (generally all) files have versions which Git is handling. Let's create a text file named 'my.txt'.

```
C:\...\gittut>more my.txt
First line, nothing more!!

```

![on my waaaay!](/assets/gittut/initialized_folder.jpg)
*the current folder would look like this*

Git still wouldn't know that something new has been added. Technically, it hasn't started *tracking* any files. 

```
C:\...\gittut>git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        my.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Git status gives, well, the current status of the folder. 

### The way to start tracking a file is

```
C:\...\gittut>git add my.txt

C:\...\gittut>git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   my.txt
```

To add all the files in a folder, one would ```git add -A```

### Let's see what happens after editing the text file...

```
C:\...\gittut>more my.txt
First line, nothing more!! :3

Second line... ADDED!

```
There was a modification in the first line ':3' and a second line was added.

```
C:\...\gittut>git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   my.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   my.txt
```

Git notifies the modification that happend with respect to the state when a file was added. This is because, the moment we ```add``` a file (to what is called as a stage), it freezes the state of the file for a possible commit. And any modifications after ```add``` -ing a file will not be committed in the future. ```add``` functions as a soft commit where if a code goes awry after modification, one could always go back to the state when it was ```add``` -ed. ```git checkout my.txt``` would essentially revert back the text file to the state when it was added for staging. 

```
C:\...\gittut>git checkout my.txt

C:\...\gittut>more my.txt
First line, nothing more!!

```

And this way, it is always possible to revert a dysfunctional code back to a working state (given you ```add``` the file to stage everytime a code works just fine). There's your backup isn't it!?

---

Of course! We've just scratched the surface of the shell. We barely tickled the tentacles and hardly glanced at the ginormous gizmo, which is Git. There's more to git than simple ```add``` command.