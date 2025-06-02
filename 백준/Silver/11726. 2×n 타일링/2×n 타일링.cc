#include <stdio.h>
int main() {
	int n[1000];
	n[1] = 1;
	n[2] = 2;
	int a;
	scanf("%d", &a);
	for (int i = 3; i <= a; i++) {
		n[i] = (n[i - 1] + n[i - 2]) % 10007;
	}
	printf("%d", n[a]);
}