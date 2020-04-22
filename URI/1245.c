#include<stdio.h>

int main(){
    int n, i, j;

    while ( scanf ("%d", &n) != EOF ) {
        char tipos[n];
        int botas[n], par;
        par = 0;
        for(i=0;i<n;i++){
            scanf("%d %c", &botas[i], &tipos[i]);
        
        }
        for (i=0; i<n; i++){
            if(tipos[i] != 'N'){
                for(j=i+1; j<n; j++){
                    if(botas[i] == botas[j] && tipos[i] != tipos[j] && tipos[j] != 'N'){
                        par++;
                        tipos[j] = 'N';
                        break;
                    }
                }
            }
        }
        printf("%d\n", par);
    }

    return 0;
}