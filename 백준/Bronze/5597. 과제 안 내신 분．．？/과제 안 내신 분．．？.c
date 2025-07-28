#include <stdio.h>

int main() {
	int num[28], a[2], b = 0, c;
	for (int i = 0; i < 28; i++) {
		scanf("%d", &num[i]);
	}
	for (int i = 1; i <= 30; i++) {
		c = 0;
		for (int j = 0; j < 28; j++) {
			if (i == num[j]) {
				c = 1;
				break;
			}
		}
		if (!c) {
			a[b++] = i;
		}
	}
	for (int i = 0; i < 2; i++) {
		printf("%d\n", a[i]);
	}
}