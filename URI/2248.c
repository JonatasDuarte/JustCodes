#include<stdio.h>

int main(){
    int n, i;
    int cont= 0;
    scanf("%d", &n);

    while(n != 0){
        int notas[n], id[n], maior;
        maior = 0;
        cont ++;
        for (i =0; i<n; i++){
            scanf("%d %d", &id[i], &notas[i]);
            if(notas[i] >= maior){
                maior = notas[i];
            }
        }
        
        printf("Turma %d\n", cont);
        for(i=0; i<n; i++){
            if(notas[i] == maior){
                printf("%d ", id[i]);
            }
        } 
        
        printf("\n\n");
        scanf("%d", &n);
    }
    return 0;
}