#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i - 1; j++) {
			printf(" ");
		}
		for (int j = 1; j <= n - i + 1; j++) {
			printf("*");	
		}
		for (int k = 1; k <= n - i; k++) {
			printf("*");
		}
		printf("\n");
	}
}