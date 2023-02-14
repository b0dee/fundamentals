#!/bin/python3
import sys

def mysqrt(target:int, guess:int):
  if (guess * guess > target):
    return -1 # any guess higher wont be finding it 
  if (guess * guess == target):
    return guess
  return mysqrt(target, guess + 1) 

if (len(sys.argv) < 2):
  print("sqrt number\nExample: sqrt 36\nFinds square root of square numbers - won't work for non-square numbers\n")
  exit(-1)
print(f"Looking for square root of {sys.argv[1]}")
res = mysqrt(int(sys.argv[1]), 1)
if (res != -1):
  print(f"Found square root: {res}")
else:
  print("Unable to find square root, sorry...\n")


