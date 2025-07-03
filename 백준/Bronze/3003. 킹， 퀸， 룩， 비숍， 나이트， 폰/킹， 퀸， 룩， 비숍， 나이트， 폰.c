#include <stdio.h>

int main() {
	int plus = 0, minus = 0;
	int arr[6] = { 1, 1, 2, 2, 2, 8 };
	int brr[6];
	int crr[6];
	for (int i = 0; i < 6; i++) {
		scanf("%d", &brr[i]);
	}
	for (int i = 0; i < 6; i++) {
		if (brr[i] > arr[i]) {
			while (brr[i] != arr[i]) {
				brr[i] -= 1;
				minus--;
			}
			crr[i] = minus;
			minus = 0;
		}
		else if (brr[i] < arr[i]) {
			while (brr[i] != arr[i]) {
				brr[i] += 1;
				plus++;
			}
			crr[i] = plus;
			plus = 0;
		}
		else {
			crr[i] = 0;
		}
	}
	for (int i = 0; i < 6; i++) {
		printf("%d ", crr[i]);
	}
}