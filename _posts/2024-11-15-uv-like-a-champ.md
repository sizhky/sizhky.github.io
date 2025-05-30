---
layout: post
title:  "Become a UV ninja with these simple commands"
date:   2024-11-15 14:48:38 +0530
categories: workflows
---

Conda is the Undisputed King of Python Environments. Or Is It?

<!--more-->
**Scroll down to Summary for a quick TLDR**

Conda is synonymous with Python environment management. Whenever you think of managing Python environments, there's a good chance you think Conda. However, Conda has its issues—a lot of issues, actually:

1. **Slow**: Conda can be incredibly sluggish, especially when managing dependencies.
2. **Dependency Hell**: When Conda gets stuck in resolving environments, you can kiss your time goodbye.
3. **Bulky**: It's a heavy system, taking up a lot of space.
4. **License Concerns**: For companies, you might face copyright claims at any time.



## Enter UV: The New Way to Maintain Python Environments

UV is the new kid on the block, aiming to simplify and speed up environment management. Built in Rust, it guarantees performance and eliminates the pain of sluggish environments.
![](https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310)
Here's a breakdown of using UV with a few handy aliases to make your workflow efficient.

## Installing UV
Just head to [uv install page](https://docs.astral.sh/uv/getting-started/installation/) and follow the instructions for your operating system.

## Creating Environments

```bash
# Instead of Conda:
conda create --name myenv python=3.9

# Use UV:
cd ~
uv venv --python 3.12
```

Instead of installing in a central directory like Conda, UV installs the environment in the `.venv` of the current folder.


## Listing Environments

```bash
# Conda:
conda env list
```

There is no equivalent command in UV. Since environments are installed locally in each project, managing them is as simple as navigating to your project's `.venv` folder.


Deactivating Environments

```
# conda deactivate
deactivate
```

Deactivating an environment is quite similar to other virtual environment packages like venv


## Activating Environments

```bash
# Conda:
conda activate myenv

# UV:
cd /path/to/project
source .venv/bin/activate
```

Typing `.venv/bin/activate` every time can be tedious, and sometimes you want a default environment no matter where you are. Introducing the `uva` alias:

```bash
. "$HOME/.cargo/env"
alias uva='f() {
    if [ -n "$1" ] && [ -f "$1/.venv/bin/activate" ]; then
        source "$1/.venv/bin/activate";
    elif [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate;
    else
        source "/home/yeshwanth/.venv/bin/activate";
    fi
}; uva'
```

In the above alias `source "/home/yeshwanth/.venv/bin/activate";` is sourcing my home environment which acts as a global python. Please change the path to your home directory.

With this alias, you can now activate environments effortlessly:

```bash
# Activate from current folder
uva

# Activate a specific environment directly
uva /path/to/project
```

If there's no `.venv` in the current directory, `uva` will activate the default environment located at `/home/yeshwanth/`.



## Installing Packages

To install packages with UV, you need an extra step:

```bash
# After activating the environment:
uv pip install numpy
```

However, this can be simplified with a Bash alias:

```bash
alias pip="uv pip"
```

With this in your `.bashrc`, you can continue using `pip install` as usual without the extra hassle.



## Summary: Supercharge Your Python Workflow with UV

To get started with UV, add these aliases to your `.bashrc`:

```bash
# UV Aliases
alias uva='f() {
    if [ -n "$1" ] && [ -f "$1/.venv/bin/activate" ]; then
        source "$1/.venv/bin/activate";
    elif [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate;
    else
        source "/home/yeshwanth/.venv/bin/activate";
    fi
}; uva'

alias pip="uv pip"
alias uvd="deactivate"
```

Start using `uva` like there's no tomorrow, and let UV bring speed and simplicity to your Python projects.

