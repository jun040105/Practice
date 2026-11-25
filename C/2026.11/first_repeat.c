#include <stdio.h>

int first_repeat(int n, int list[]) {

    for (int i = 1; i < n; i++){ 

        for (int j = 0; j < i; j++) {
            if (list[j] == list[i]) {

                return i;
            }
        }
    }   

    return -1;
}

int main(){

    int n; 
    int list[100];

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &list[i]);
    }

    if (first_repeat(n, list) == -1) {
        printf("NONE");
    }
    else {
        printf("%d", list[first_repeat(n, list)]);
    }

    return -1;
}