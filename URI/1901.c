#include <stdio.h>

int main()
{
    int n, i, ero, um, j, k, dos;
    scanf("%d", &n);
    int res;
    int floresta[n][n];
    ero = 0;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &floresta[i][j]);
        }
    }
    for (j = 0; j < (2 * n); j++)
    {
        scanf("%d %d", &um, &dos);
        res = floresta[um - 1][dos - 1];
        if (res != 0)
        {
            ero++;
            for (j = 0; j < n; j++)
            {
                for (k = 0; k < n; k++)
                {
                    if (floresta[j][k] == res)
                    {
                        floresta[j][k] = 0;
                    }
                }
            }
        }
    }
    printf("%d\n", ero);
    return 0;
}