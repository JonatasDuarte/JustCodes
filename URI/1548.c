#include <stdio.h>

int main(void)
{
    int n, i, alunos, j;
    scanf("%d", &n);
    for (j = 0; j < n; j++)
    {
        scanf("%d", &alunos);
        int notas[alunos], verificar[alunos], cont= 0;
        for (i = 0; i < alunos; i++)
        {
            scanf("%d", &notas[i]);
            verificar[i] = notas[i];
        }

        for (i = 0; i < alunos; i++)
        {
            int atual = notas[i];
            int anterior = i - 1;
            while (anterior >= 0 && notas[anterior] < atual)
            {
                notas[anterior + 1] = notas[anterior];
                anterior--;
            }
            notas[anterior + 1] = atual;
        }
        for (i = 0; i < alunos; i++)
        {
            if (notas[i] == verificar[i])
                cont++;
        }
        printf("%d\n", cont);
    }
}