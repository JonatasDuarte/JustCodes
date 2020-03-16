#include<stdio.h>
#include <math.h>

int main() {

    int casos;
    scanf("%d", &casos);

    while(casos > 0){
        int num, qnt;
        scanf("%d %d", &num, &qnt);
        int soma = 0;
        while(qnt>0){
            if(num%2 != 0){
                soma += num;
                num+=2;
            } else{
                num += 1;
                qnt++;
            }
            qnt--;
        }
        printf("%d\n", soma);
        casos--;
    }

        
    return 0;
}