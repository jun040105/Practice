#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int n;
    scanf("%d", &n);
    
    int* arr = malloc(n * sizeof(int));
    
    int x = 0;
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        x += arr[i];
    }
    
    printf("%d", x);
    return 0;
}