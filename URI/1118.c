#include<stdio.h>

int main (){
    int dois, cont, true;
    dois = 1;
    double nota, media;
    while(dois!=2){
        true = media = cont= 0;
        while(cont!=2 && dois==1){
            true = 1;
            scanf("%lf", &nota);
            if((nota>=0)&&(nota<=10)){
                media += nota;
                cont++;
            } else{
                printf("nota invalida\n");
            }
        } 
        if(true ==1) {
            printf("media = %.2lf\n", media/2);
        }
        printf("novo calculo (1-sim 2-nao)\n");
        scanf("%d", &dois);
        if(dois == 2){
            break;
        }
    }
    return 0;
}