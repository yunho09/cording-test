#include <stdlib.h>
#include <stdio.h>

void Switch (char* a) {
	int temp;
	temp = *a;
	*a = a[2];
	a[2] = temp;
}

int main() {
	char a[4], b[4];
	scanf("%s %s", a, b);
	Switch (a);
	Switch (b);
	if (atoi(a) >= atoi(b)) printf("%d", atoi(a));
	else printf("%d", atoi(b));
}