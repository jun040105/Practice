#include <stdio.h>

#define MAX_SIZE 5

int shortest_path(int maze[MAX_SIZE][MAX_SIZE], int rows, int cols) {
    // TODO

    return -2;
}

int main(void) {
    int maze1[MAX_SIZE][MAX_SIZE] = {
        {0, 1, 0, 0, 0},
        {0, 1, 0, 1, 0},
        {0, 1, 0, 1, 0},
        {0, 0, 0, 1, 0}
    };

    int maze2[MAX_SIZE][MAX_SIZE] = {
        {0, 1, 1},
        {1, 1, 1},
        {1, 1, 0}
    };

    int maze3[MAX_SIZE][MAX_SIZE] = {
        {0}
    };

    printf("%d\n", shortest_path(maze1, 4, 5));
    printf("%d\n", shortest_path(maze2, 3, 3));
    printf("%d\n", shortest_path(maze3, 1, 1));

    return 0;
}