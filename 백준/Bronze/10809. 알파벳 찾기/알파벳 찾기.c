#include <stdio.h>
#include <string.h>

int main() {
	char arr[27], brr[101], crr[27], j = 0;
	for (int i = 0; i < 26; i++) {
		arr[i] = 'a' + i;
		crr[i] = -1;
	}
	arr[26] = '\0';

	scanf("%s", &brr);

	for (int i = 0; i < strlen(brr); i++) {
		while (arr[j] != '\0') {
			if (arr[j] == brr[i]) {
				if(crr[j] == -1) crr[j] = i;
				break;
			}
			j++;
		}
		j = 0;
	}	
	for (int i = 0; i < 26; i++) {
		printf("%d ", crr[i]);
	}
}