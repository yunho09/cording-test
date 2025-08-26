#include <stdio.h>

int main() {
    int a, b, arr[1001] = { 0 }, brr[1001] = { 0 };
    for (int i = 0; i < 3; i++) {
        scanf("%d %d", &a, &b);
        arr[a]++;
        brr[b]++;
    }
    for (int i = 0; i < 1001; i++) {
        if (arr[i] == 1) {
            a = i;
        }
        if (brr[i] == 1) {
            b = i;
        }
    }
    printf("%d %d", a, b);
}