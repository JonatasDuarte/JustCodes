#include<stdio.h>

int main () {
    int i, j, temp;
    int altura, kmada, furos, ant;
    int  dif;
    while(1){
        scanf("%d %d", &altura, &kmada);
        if(altura == 0 && kmada == 0){
            break;
        }
        furos = ant = temp = 0;

        for(i=0; i<kmada; i++){
            scanf("%d",&temp);
            dif = altura-temp;
            if(dif >ant){
                furos += dif-ant;
            }
            ant = dif;
        }
        printf("%d\n", furos);
    }
    return 0;
}