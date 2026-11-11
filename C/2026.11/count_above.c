#include <stdio.h>

int count_above(const int* arr, int length, int threshold) {

    int sum = 0;

    for (int i=0; i < length; i++) {
        if(arr[i] > threshold) {

            sum++;
        }
    }

    return sum;
}

int main(void) {

    int numbers[] = {4, 7, 2, 9, 7, 3};
    printf("%d\n", count_above(numbers, 6, 5));

    return 0;
}