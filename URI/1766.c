#include <stdio.h>
#include <stdlib.h>
#include<string.h>

typedef struct
{
    int peso;
    int idade;
    char nome[101];
    float altura;
} Rena;

int comparacao(Rena *r1, Rena *r2)
{
    if (r2->peso > r1->peso)
        return 1;
    else if (r1->peso > r2->peso)
        return 2;

    if (r1->idade < r2->idade)
        return 2;
    else if (r1->idade > r2->idade)
        return 1;

    if (r1->altura < r2->altura)
        return 2;
    else if (r1->altura > r2->altura)
        return 1;

    int name = strcmp(r1->nome, r2->nome);
    if (name < 0)
        return 2;
    else if (name > 0)
        return 1;
    else
        return 0;
}

int main(void)
{
    int n, i, j;
    scanf("%d", &n);
    for (j = 0; j < n; j++)
    {
        int nr, rt;
        scanf("%d %d", &nr, &rt);
        Rena renas[nr];
        for (i = 0; i < nr; i++)
        {
            Rena rena;
            scanf("%s %d %d %f", rena.nome, &rena.peso, &rena.idade, &rena.altura);
            renas[i]  = rena;
        }
        Rena atual;
        int anterior;
        for (i = 0; i < nr; i++)
        {
            atual = renas[i];
            anterior = i - 1;
            while (anterior >= 0 && comparacao(&renas[anterior], &atual) == 1)
            {
                renas[anterior + 1] = renas[anterior];
                anterior--;
            }
            renas[anterior + 1] = atual;
        }
        printf("CENARIO {%d}\n", j + 1);
        for (i = 0; i < rt; i++)
        {
            printf("%d - %s\n", i + 1, renas[i].nome);
        }
    }
}