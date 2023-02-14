#include <stdio.h>
#include <stdlib.h>


// Returns -1 on failure to find square root
// Otherwise returns square root
int mysqrt(int target, int guess) {
  // If guess * guess if bigger than target any increase will be too
  // Prevents endless loops
  return guess * guess > target ? -1: guess * guess == target ? guess: mysqrt(target, guess+1);
}

void usage() {
  printf("Find square root via recursion\n");
  printf("Usage: sqrt number\n");
  printf("Example: sqrt 42\n");
}

int main(int argc, char **argv) {
  if (argc <2) 
    usage();

  printf("Searching for square root of %d\n", atoi(argv[1]));
  int res = mysqrt(atoi(argv[1]), 1);
  
  if (res == -1) { 
    printf("Could not find square root, sorry :(\n");
  } else { 
    printf("Found square root: %d\n", res);
  }
  return 0;
}
