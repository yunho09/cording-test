#include <stdio.h>

int main() {
	int a[9], M = 0;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &a[i]);
		if (a[M] <= a[i]) M = i;
	}
	printf("%d\n%d", a[M], M+1);
}