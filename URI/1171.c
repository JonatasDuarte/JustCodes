#include<stdio.h>

int main (){
    int n, i, j, var;
    scanf("%d", &n);
    int numeros[n];
    for(i=0; i<n;i++){
        scanf("%d", &numeros[i]);
    }

    for (i =0; i<n;i++){
        for(j=i+1; j<n; j++){
            if(numeros[i] > numeros[j]){
                var = numeros[i];
                numeros[i] = numeros[j];
                numeros[j] = var;
            }
        }
    }
    int cont = 1;
    for(i=0; i<n; i++){
        if(i+1 < n && numeros[i] == numeros[i+1]){
            cont++;
        }else{
            printf("%d aparece %d vez(es)\n", numeros[i], cont);
            cont = 1;
        }
    }
    return 0;
}