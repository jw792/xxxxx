# kg_jw792_2020

## Summary

This repository contains a simple program main.py that determines whether a one-to-one character mapping exists from one string, s1, to another string, s2.

For example, given s1 = abc and s2 = bcd, print "true" into stdout since we can map each
character in "abc" to a character in "bcd".

Given s1 = foo and s2 = bar, print "false" since the character ‘o’ cannot map to two characters.

But given s1 = bar and s2 = foo, print "true" since each character in "bar" can be mapped to a
character in "foo".

## Prerequisites

Python 3 should be installed on your testing environment.

## How to run

You should run the code in the following manner: 
```
python3 main.py abc bcd
```
You should provide two strings as input. If fewer or more than two strings are provided, the program outputs a warning. Ortherwise, it prints a true or false value indicating if a mapping exists between two strings.