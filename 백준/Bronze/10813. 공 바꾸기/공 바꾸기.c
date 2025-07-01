#include <stdio.h>
int main() {
	int n, m, i, j, arr[101], tmp;
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++) {
		arr[i] = i;
	}
	for (int c = 1; c <= m; c++) {
		scanf("%d %d", &i, &j);
			tmp = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp;
	}
	for (int i = 1; i <= n; i++) {
		printf("%d ", arr[i]);
	}
}