#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d\n%d\n%d", &a, &b, &c);
    if (a == 60 && b == 60 && c == 60) printf("Equilateral");
    else if (a + b + c == 180 && (a == b || b == c || c == a)) printf("Isosceles");
    else if (a + b + c == 180 && (a != b && b != c && c != a)) printf("Scalene");
    else printf("Error");
}