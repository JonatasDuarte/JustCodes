#include<stdio.h>
#include <math.h>

int main() {
    
    int N, hora, minutos, segundos;
    scanf("%d", &N);

    hora = N/3600;
    minutos = (N/60)%60; 
    segundos = N%60; 
    printf("%d:%d:%d\n", hora, minutos, segundos);

    return 0;
}