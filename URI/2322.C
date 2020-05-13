#include<stdio.h>

int main ( ){
    int n,i, num, soma;
    soma =0;
    int certo =0;
    scanf("%d", &n);
    for(i =1; i<n; i++){
        scanf("%d", &num);
        soma+=num;
    }
    for(i=1; i<=n; i++){
        certo+=i;
    }
    printf("%d\n", certo-soma);
    return 0;
}