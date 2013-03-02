#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

#define DATA_SIZE 1000000

int *quicksort(int *A, int size) {
  if (size <= 1) {
    return A;
  }
  int pivotIndex = rand() % size;
  int pivot = A[pivotIndex];
}

int main( int argc, char **argv ) {
  if (argc != 2) {
    printf("Not enough arguments\n");
    return 1;
  }
  FILE *file = fopen(argv[1], "r");
  if (file == NULL) {
    perror("Failed to open file");
    printf("errno = %d.\n", errno);
    return 2;
  }
  int data[DATA_SIZE];  // TODO: dynamic data size
  int i = 0;
  while (fscanf(file, "%d", data + i++) == 1) {
  }
  // TODO: add error checking
  quicksort(data, DATA_SIZE);

  fclose(file);
}
