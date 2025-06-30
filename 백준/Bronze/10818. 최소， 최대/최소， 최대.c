#include <stdio.h>

int main() {
	int n, a[1000001], m = 0, M = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
		if (a[m] >= a[i]) m = i;
		if (a[M] <= a[i]) M = i;
	}
	printf("%d %d", a[m], a[M]);
}