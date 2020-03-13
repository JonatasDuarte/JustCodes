#include<stdio.h>
#include <math.h>

int main() {

    int num;
    scanf("%d", &num);
    int aux = num;
    int cont=0;

    while(num > 0){
        cont++;
        if(aux%cont== 0){
            printf("%d\n", cont);
        }
        num--;
    }
    return 0;
}