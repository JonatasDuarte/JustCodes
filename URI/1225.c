#include<stdio.h>

int main (){
    int n, i, media, soma, cont, ult;
    while(scanf("%d",  &n) != EOF){
        int notas[n];
        media = soma=cont= 0;
        for(i=0; i<n; i++){
            scanf("%d", &notas[i]);
            soma += notas[i];
        }
        media = soma/n;
        if(soma%n == 0){
            for(i=0;i<n;i++){
                if(notas[i]>media){
                    cont += notas[i] - media;
                }
                
            }
            printf("%d\n",cont+1);
        } else{
            printf("-1\n");
        }
    }
    return 0;
}