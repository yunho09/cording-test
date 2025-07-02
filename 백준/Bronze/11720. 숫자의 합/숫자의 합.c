#include <stdio.h>

int main() {
	int n, a[101], sum = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%1d", &a[i]);
		sum += a[i];
	}
	printf("%d", sum);
}