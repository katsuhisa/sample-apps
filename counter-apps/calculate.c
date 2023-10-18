#include <stdio.h>
#include <stdlib.h>

int add(int a, int b) {
    return a + b;
}

int main(int argc, char *argv[]) {
    if(argc < 3) {
        printf("Usage: calculate <num1> <num2>\n");
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    printf("Result: %d\n", add(a, b));
    return 0;
}