#include <stdio.h>

int main() {
	int n, count = 0;
	scanf("%d", &n);
	if (n == 1 || n == 3) {
		printf("-1");
		return 0;
	}
	while (1) {
		if (10 <= n || n >= 5 && (n % 5) % 2 == 0) {
			n -= 5;
			count++;
		}
		else
			break;
	}
	while (n > 0) {
		n -= 2;
		count++;
	}
	printf("%d", count);
}