#include <stdio.h>

int main(void)
{
    int n, i;
    while (scanf("%d", &n) != EOF)
    {
        int virus[n];
        for (i = 0; i < n; i++)
        {
            scanf("%d", &virus[i]);
        }
        for (i = 0; i < n; i++)
        {
            int atual = virus[i];
            int anterior = i - 1;
            while (anterior >= 0 && virus[anterior] > atual)
            {
                virus[anterior + 1] = virus[anterior];
                anterior--;
            }
            virus[anterior + 1] = atual;
        }
        int m = 0, esq = 0, dir = n - 1, letal = 0;
        if ((n - 1) % 2 == 0)
        {
            m = (n + 1) / 2;
            for (i = 0; i < m; i++)
            {
                letal += (virus[dir] - virus[esq]);
                dir--;
                esq++;
            }
        }
        else
        {
            for (i = 0; i < n / 2; i++)
            {
                letal += (virus[dir] - virus[esq]);
                dir--;
                esq++;
            }
        }
        printf("%d\n", letal);
    }
}