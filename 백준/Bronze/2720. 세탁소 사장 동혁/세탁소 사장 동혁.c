#include <stdio.h>

int main() {
    int n, c, arr[4] = { 0 };
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &c);
        while (c != 0) {
            if (c >= 25) {
                c -= 25;
                arr[0] += 1;
            }
            else if (c >= 10) {
                c -= 10;
                arr[1] += 1;
            }
            else if (c >= 5) {
                c -= 5;
                arr[2] += 1;
            }
            else {
                c -= 1;
                arr[3] += 1;
            }
        }
        for (int j = 0; j < 4; j++) printf("%d ", arr[j]);
        for (int j = 0; j < 4; j++) arr[j] = 0;
    }
}