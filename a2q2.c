/*
-------------------------------------
File:    a2q2.c
Project: a2q2
file description
-------------------------------------
Author:  Fangjian Lei
ID:      163165490
Email:   leix5490@mylaurier.ca
Version  2018-01-17
-------------------------------------
 */


#include<stdio.h>
#include<stdlib.h>
int horner(int, int, int[]);

int main(int argc, char* args[]) {
	if (argc <= 3) {
		printf("need more than two integer arguments: 2 1 2 3 4");
		return 0;
	}

	int i, x = atoi(args[1]), n = argc - 2;
	int* a;
	a = (int*)malloc(n * sizeof(int));
	for (i = 0; i < n; i++) {
		a[i] = atoi(args[i + 2]);
	}
	for (int u = 0; u < n; u++) {
		if (u == n - 1) {
			printf("%d*%d^%d = ", a[u], x, n - u - 1);
		}

		else {
			printf("%d*%d^%d + ", a[u], x, n - u - 1);

		}
	}
	printf("%d", horner(x, n, a));
	
	/*infinite loop testing*/
	while(1==1){
	}
	
	return 0;
	
}

int horner(int x, int n, int a[]) {
	int p = 0, i;
	for (i = 0; i < n; i++) {
		p = p * x + a[i];
	}
	return p;
}



