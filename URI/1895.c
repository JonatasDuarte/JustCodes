#include<stdio.h>

int main (){
    int cartas, inicial, limite, carpilha, i, pontob, pontoa;
    pontob = pontoa = 0;
    scanf("%d %d %d", &cartas, &inicial, &limite);

    for(i = 0; i<cartas-1; i++){
        scanf("%d", &carpilha);
        int dif = inicial-carpilha;
        if(dif<0){
            dif = dif*(-1);
        }

        if (dif <= limite)
        {
            if(i%2 == 0){
                pontoa+=dif;
            }else{
                pontob+=dif;
            }
            inicial = carpilha;
        }
    
    }
    printf("%d %d\n", pontoa, pontob);
    return 0;
}