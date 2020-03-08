#include <stdio.h>

int main()
{
    int troco, valor;
    int cem, cinq, vinte, dez, cinco, dois, um;
    scanf("%d", &troco);
    valor = troco;
    cem = troco / 100;
    troco = troco - (cem * 100);
    cinq = troco / 50;
    troco = troco - (cinq * 50);
    vinte = troco / 20;
    troco = troco - (vinte * 20);
    dez = troco / 10;
    troco = troco - (dez * 10);
    cinco = troco / 5;
    troco = troco - (cinco * 5);
    dois = troco / 2;
    troco = troco - (dois * 2);
    um = troco / 1;

    printf("%d\n", valor);
    printf("%d nota(s) de R$ 100,00\n", cem);
    printf("%d nota(s) de R$ 50,00\n", cinq);
    printf("%d nota(s) de R$ 20,00\n", vinte);
    printf("%d nota(s) de R$ 10,00\n", dez);
    printf("%d nota(s) de R$ 5,00\n", cinco);
    printf("%d nota(s) de R$ 2,00\n", dois);
    printf("%d nota(s) de R$ 1,00\n", um);

    return 0;
}