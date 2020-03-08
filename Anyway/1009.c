#include<stdio.h>

int main() {
    char nome[50];
    scanf("%s", nome);
    double sal;
    scanf("%lf", &sal);
    double vendas;
    scanf("%lf", &vendas);
    double comi = 0.15;
    printf("TOTAL = R$ %.2lf\n", sal+(vendas*comi));  
    return 0;
}