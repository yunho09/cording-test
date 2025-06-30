#include <stdio.h>

int main() {
	int n[101];
	int a, b, count = 0;
	scanf("%d", &a);
	for (int i = 0; i < a; i++) {
		scanf("%d", &n[i]);
	}
	scanf("%d", &b);
	for (int i = 0; i < a; i++) {
		if (n[i] == b) count++;
	}
	printf("%d", count);
}