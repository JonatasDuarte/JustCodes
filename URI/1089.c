#include<stdio.h>

int main (){
    int n, i , j, prox, ante, pico, atual;
    while(n != 0){
        scanf("%d", &n);
        pico = ante = prox= 0;
        int loop[n];
        for(i=0; i<n; i++){
            scanf("%d", &loop[i]);
        }
        for(i=0; i<n; i++){
            ante = loop[i-1];
            prox = loop[i+1];
            atual = loop[i];
            if(i == 0){
                ante = loop[n-1];
                if((atual > ante && atual > prox) || (atual < ante && atual <prox)){
                    pico++;
                }
            }else if(i == n-1){
                prox = loop[0];
                if((atual > ante && atual > prox) || (atual < ante && atual <prox)){
                    pico++;
                }
            }else if((atual > ante && atual > prox) || (atual < ante && atual < prox)){
                pico++;
            }
        }
        if(n != 0){
            printf("%d\n", pico);
        }
    }
    return 0;
}