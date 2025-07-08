#include <string.h>
#include <stdio.h>

char input[1000001];

int main() {
	int a[26], b[26], count[26];
	for (int i = 0; i < 26; i++) {
		a[i] = 'A' + i;
		b[i] = 'a' + i;
		count[i] = 0;
	}
	scanf("%s", input);
	for (int i = 0; i < strlen(input); i++) {
		for (int j = 0; j < 26; j++) {
			if (a[j] == input[i] || b[j] == input[i]) {
				count[j] += 1;
				goto next;
			}
		}
		next: ;
	}
	int max = 0;
	for (int i = 0; i < 26; i++) {
		if (count[i] >= count[max]) {
			max = i;
		}
	}
	int p = 0;
	for (int i = 0; i < 26; i++) {
		if (count[max] == count[i]) {
			p++;
		}
	}
	if (p >= 2) printf("?");
	else printf("%c", a[max]);
}