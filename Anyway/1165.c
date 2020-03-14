#include <stdio.h>
int main()
{
    int q, i;
    int num, j, contDiv;
    scanf("%d", &q);
    for (i = 0; i < q; i++)
    {
        contDiv = 0;
        scanf("%d", &num);
        for (j = 1; j <= num; j++)
        {
            if (num % j == 0)
            {
                contDiv++;
            }
            if (contDiv > 2)
            {
                break;
            }
        }
        if (contDiv == 2)
        {
            printf("%d eh primo\n", num);
        }
        else
        {
            printf("%d nao eh primo\n", num);
        }
    }
    return 0;
}