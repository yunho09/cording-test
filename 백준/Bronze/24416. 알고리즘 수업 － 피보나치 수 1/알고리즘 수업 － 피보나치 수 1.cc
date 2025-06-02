#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int count1, count2;
int fib(int n) {
	if (n == 1 || n == 2) {
		count1++;
		return 1;
	}
	count1++;
	return (fib(n - 1) + fib(n - 2));
}
int fibonacci(int n) {
	if (n <= 2) {
		count2++;
		return 1;
	}

	int f[41];
	f[1] = f[2] = 1;

	for (int i = 3; i <= n; i++) {
		f[i] = f[i - 1] + f[i - 2];
		count2++;
	}

	return f[n];
}
int main() {
	int n;
	scanf("%d", &n);
	fibonacci(n);
	printf("%d %d", fib(n), count2);
}