#include <stdio.h>
int main() {
	int a[9][9], max1 = 0, max2 = 0;
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (a[max1][max2] <= a[i][j]) {
				max1 = i;
				max2 = j;
			}
		}
	}
	printf("%d\n%d %d", a[max1][max2], max1 + 1, max2 + 1);
}