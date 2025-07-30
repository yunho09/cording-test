#include <string.h>
#include <stdio.h>

int main() {
	char a[21];
	int b, n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %s", &b, &a);
		for (int j = 0; j < strlen(a); j++) {
			for (int p = 0; p < b; p++) {
				printf("%c", a[j]);
			}
		}
		printf("\n");
	}
}