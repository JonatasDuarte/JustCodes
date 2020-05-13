#include<stdio.h>
#include <stdlib.h>

int main(){
    int n, pm, i, j, dif, cont;
    cont =0;
    scanf("%d %d", &n, &pm);
    int num[n];
    for(i=0;i<n;i++){
        scanf("%d", &num[i]);
    }
    for(i=0;i<n-1;i++){
        dif = pm - num[i];
        cont += abs(dif);
        num[i] += dif;
        num[i+1] += dif;
    }
    printf("%d\n", cont );

    return 0;
}