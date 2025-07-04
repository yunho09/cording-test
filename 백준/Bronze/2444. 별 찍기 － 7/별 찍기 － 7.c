#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int k = 0; k < n-i-1; k++) {
			printf(" ");
		}
		for (int j = 0; j < (i)*2+1; j++) {
			printf("*");
		}
		printf("\n");
	}
	for (int i = 1; i <= n; i++) {
		for (int k = 0; k < i; k++) {
			printf(" ");
		}
		for (int j = 0; j < n - i; j++) {
			printf("*");
		}
		for (int j = 0; j < n - i - 1; j++) {
			printf("*");
		}
		printf("\n");
	}
}