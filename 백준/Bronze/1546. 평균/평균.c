#include <stdio.h>

int main() {
	int n, max = 0;
	float c = 0, a[1000];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%f", &a[i]);
	}
	for (int i = 0; i < n; i++) {
		if (a[max] <= a[i]) {
			max = i;
		}
	}
	for (int i = 0; i < n; i++) {
		c += a[i] / a[max] * 100;
	}
	printf("%f", c / n);
}