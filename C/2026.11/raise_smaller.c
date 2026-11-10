#include <stdio.h>

void raise_smaller(int* a, int* b, int step)
{
    if (*a > *b) {
        if (*a - *b < step) {
            *b = *a; 
        }
        else {
            *b += step;
        }
    }

    if (*b > *a) {
        if (*b - *a < step) {
            *a = *b; 
        }
        else {
            *a += step;
        }
    }
}

int main(void)
{
    int x = 9;
    int y = 2;

    raise_smaller(&x, &y, 3);
    printf("%d %d\n", x, y);

    x = 4;
    y = 6;
    raise_smaller(&x, &y, 10);
    printf("%d %d\n", x, y);

    raise_smaller(&x, &y, 5);
    printf("%d %d\n", x, y);

    return 0;
}