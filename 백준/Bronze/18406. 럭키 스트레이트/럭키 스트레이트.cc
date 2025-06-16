#include <stdio.h>
#include <string.h>

int main() {
	char n[10];
	scanf("%s", &n);
	int a = 0, b = 0;
	int leng = strlen(n) / 2;
	for (int i = 0; i < leng; i++) {
		a += (n[i]-48);
	}
	for (int i = leng; i < leng*2; i++) {
		b += (n[i] - 48);
	}
	if (a == b) printf("LUCKY");
	else printf("READY");
}
