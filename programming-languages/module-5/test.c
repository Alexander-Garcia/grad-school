#include <stdio.h>

void blah(int *a, int *b);

int main() {
  int list[2] = {1, 3};
  blah(&list[0], &list[1]);
  printf("List[0]: %d\n", list[0]);
  printf("List[1]: %d\n", list[1]);
  return 0;
}

void blah(int *a, int *b) {
  *a += *a;
  *b += *b;
}

int test(int *l) {
  *l += 5;
  return 4;
}
