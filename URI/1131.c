#include<stdio.h>

int main(){
    int inter, gremio, wini, wing, emp, dois, grenos;
    grenos = wini = wing = emp = 0;;

    while(1){
        scanf("%d %d", &inter, &gremio);
        grenos++;
        if(inter > gremio){
            wini++;
        } else if(gremio > inter){
            wing++;
        } else{
            emp++;
        }
        printf("Novo grenal (1-sim 2-nao)\n");
        scanf("%d", &dois);
        if(dois == 2){
            break;
        }
    }
    printf("%d grenais\n", grenos);
    printf("Inter:%d\n", wini);
    printf("Gremio:%d\n", wing);
    printf("Empates:%d\n", emp);
    if (wini>wing){
        printf("Inter venceu mais\n");
    } else if(wing>wini){
        printf("Gremio venceu mais\n");
    } else{
        printf("Nao houve vencedor\n");
    }
    return 0;
}