#include <string.h>
#include <stdio.h>

int main() {
	int c = 0;
	char a[101], b[101];
	scanf("%s", &a);
	for (int i = strlen(a) - 1; i >= 0 ; i--) {
		b[c] = a[i];
		c++;
	}
	b[c] = '\0';
	if (!strcmp(a,b)) printf("1");
	else printf("0");
}