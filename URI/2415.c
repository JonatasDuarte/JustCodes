#include<stdio.h>

int main(){
    int n, atual;
    scanf("%d", &n);
    int antes;
    int i = 0;
    int maxseq = 0;
    int seq = 0;
    int valores[n];
    while(i<n){
        scanf("%d", &atual);
        valores[i] = atual;
        if(i == 0 || (atual != antes)){
            seq = 1;
        } else{
            seq++;
        }
        if(seq > maxseq){
            maxseq = seq;
        }
        antes = atual;
        i++;
    }
    printf("%d\n", maxseq);
    return 0;
}