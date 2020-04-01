#include<stdio.h>
//parado - 1 ou 2
//pulo - >2
int main(){
    int n, i, j, dano;
    i = 0;
    scanf("%d", &n);

    while(i<n){
        int t;
        scanf("%d", &t);
        int seg[55], alt;
        char pulos[55], pulo;
        j = dano = 0;
        for(j=0; j<t; j++){
            scanf("%d", &seg[j]);
        }
        scanf("%s", &pulos);
        for(j=0; j<t; j++){
            pulo = pulos[j];
            alt = seg[j];
            if(pulo == 'J'){
                if(alt>2){
                    dano++;
                } 
            } else if(pulo == 'S'){
                if(alt<=2){
                    dano++;
                }
            }
        }
        printf("%d\n", dano);
        i++;
    }
    return 0;
}