#include <stdio.h>

int sanduiches(int paes[], int pao, int tam)
{
    int cont = 0, i;
    for (i = 0; i < pao; i++)
    {
        cont += paes[i] / tam;
    }
    return cont;
}

int main(void)
{
    int people, pao, i;
    int maior = -1;
    scanf("%d", &people);
    scanf("%d", &pao);
    int paes[pao];
    for (i = 0; i < pao; i++)
    {
        scanf("%d", &paes[i]);
        if (paes[i] > maior) maior = paes[i];
    }
    int ini = 1, fim = maior, m, res = 0;
    while (ini <= fim)
    {
        m = (ini + fim) / 2;
        int va = sanduiches(paes, pao, m);
        if (va >= people && res < m)
        {
            ini = m + 1;
            res = m;
        }
        else fim = m - 1;
    }

    printf("%d\n", res);
}