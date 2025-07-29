#include <stdio.h>

int main() {
	char a[100], n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        if (scanf("%s", a) == 1) {
            printf("%sDORO ", a);
        }
    }
}