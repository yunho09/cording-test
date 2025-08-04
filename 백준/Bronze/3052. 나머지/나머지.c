#include <stdio.h>

int main() {
	int n[10], a[42], num = 0;
	for (int i = 0; i < 42; i++) {
		a[i] = 0;
	}
	for (int i = 0; i < 10; i++) {
		scanf("%d", &n[i]);
	}
	for (int i = 0; i < 10; i++) {
		a[n[i] % 42]++;
	}
	for (int i = 0; i < 42; i++) {
		if (a[i] != 0) {
			num++;
		}
	}
	printf("%d", num);
}