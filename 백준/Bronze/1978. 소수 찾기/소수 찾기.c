#include <stdio.h>

int main() {
    int n, a, count = 0, ncount = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a);
        for (int j = 1; j <= a; j++) {
            if (a != 1 && a % j == 0) count++;
        }
        if (count == 2) ncount++;
        count = 0;
    }
    printf("%d", ncount);
}