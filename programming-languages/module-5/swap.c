#include <stdio.h>

void swap(int *a, int *b);

int main() {
  int value = 2, list[5] = {1, 3, 5, 7, 9};
  /* swap(&value, &list[0]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[0]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[1]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[2]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[3]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[4]); */

  /* swap(&list[0], &list[1]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[0]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[1]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[2]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[3]); */
  /* printf("First call - Value: %d, List[0]: %d\n", value, list[4]); */
  swap(&value, &list[value]);
  printf("First call - Value: %d, List[0]: %d\n", value, list[0]);
  printf("First call - Value: %d, List[0]: %d\n", value, list[1]);
  printf("First call - Value: %d, List[0]: %d\n", value, list[2]);
  printf("First call - Value: %d, List[0]: %d\n", value, list[3]);
  printf("First call - Value: %d, List[0]: %d\n", value, list[4]);
  return 0;
}

void swap(int *a, int *b) {
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}

int test(int *l) {
  *l += 5;
  return 4;
}
