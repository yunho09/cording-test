#include <stdio.h>
int main() {
	int n, m, i, j, k, arr[101] = { 0 };
	scanf("%d %d", &n, &m);
	for (int c = 1; c <= m; c++) {
		scanf("%d %d %d", &i, &j, &k);
		for (int d = i; d <= j; d++) {
			arr[d] = k;
		}
	}
	for (int i = 1; i <= n; i++) {
		printf("%d ", arr[i]);
	}
}