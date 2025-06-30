#include <stdio.h>

int main() {
	int n, a[10001], x;
	scanf("%d %d", &n, &x);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
		if (a[i] < x) printf("%d ", a[i]);
	}
}