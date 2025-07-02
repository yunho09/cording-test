#include <stdio.h>

int main() {
	char a[101];
	int i = 0, n;
	scanf("%d", &n);
	for (int b = 0; b < n; b++) {
		scanf("%s", &a);
		while (a[i] != '\0') {
			i++;
		}
		printf("%c%c\n", a[0], a[i -1]);
		i = 0;
	}
}