#include<stdio.h>

int main(){
    int n, i, j, ind, dias;
    dias=0;
    int tam, ponto;
    scanf("%d %d", &tam, &ponto);
    int parada = tam;
    int fita[tam];
    for(i=0;i<tam;i++){
        fita[i] = 1;
    }
    for(i=0; i<ponto; i++){
        scanf("%d", &ind);
        fita[ind-1] = 0;
    }

    for(j=0;j<tam;j++){
        if(parada == 0){
            break;
        }
        for(i=0;i<tam; i++){
            if(fita[i] == 0 && parada != 0){
                if(i==0){
                    fita[j] = 0;
                    fita[j+1] = 0;
                    parada -+ 2;
                } else if(i = tam-1){
                    fita[j] = 0;
                    fita[j-1] = 0;
                } else{
                    fita[j] = 0;
                    fita[j-1] = 0;
                    fita[j+1] = 0;
                }
                
            }      
        }dias++;
        
    }
    printf("%d\n", dias);

    return 0;
}