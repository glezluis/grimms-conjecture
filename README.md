# grimms-conjecture
Grimm's conjecture states that for a set of consecutive composite numbers you can assign a unique prime to each element in that set. It still has yet to be proven mathematically but the algorithm in this python script will help analyze it numerically. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
The program runs on python3 so you will need pip3 to install sympy. 
To install sympy:
```
pip3 install sympy
```

### Usage

To install: 
```
git clone https://github.com/glezluis/grimms-conjecture.git
cd grimms-conjecture
python3 main.py
```

you will then be prompted by the menu:

```
Grimm's conjecture! what do you want to?
(f)ind consectuive composite sets
(p)rint sets
(q)uit
enter a choice:
```
```(f)``` will find all the set of consecutive composites for a given range. 
```
enter a choice: f
Enter a range [a,b]
a = 46
b = 68
3 consecutive composite sets found between [46, 68]
```
```(p)``` will print the sets. The first number is the composite and the second number the unique prime divisor. 
```
enter a choice: p
1 .  {48: 3, 49: 7, 50: 5, 51: 17, 52: 13}

2 .  {54: 3, 55: 11, 56: 7, 57: 19, 58: 29}

3 .  {62: 31, 63: 7, 64: 2, 65: 13, 66: 11}
```
