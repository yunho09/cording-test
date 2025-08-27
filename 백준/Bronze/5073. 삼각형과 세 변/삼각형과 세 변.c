#include <stdio.h>

int main() {
    int a = 1, b = 1, c = 1, M, all;
    while (1) {
        scanf("%d %d %d", &a, &b, &c);
        all = a + b + c;
        M = a;
        if (M <= b) M = b;
        if (M <= c) M = c;
        if (a == 0 && b == 0 && c == 0) return 0;
        else if (M >= (all - M)) printf("Invalid\n");
        else if (a == b && b == c && a == c) printf("Equilateral\n"); 
        else if (a != b && b != c && a != c) printf("Scalene\n");
        else printf("Isosceles\n");                
    }
}