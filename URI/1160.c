#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, anos;
    int i = 0;
    long pa, pb;
    double g1, g2, tA, tB;
    scanf("%d", &n);
    while(i < n)
    {
        scanf("%ld %ld %lf %lf", &pa, &pb, &g1, &g2);
        tA = 1+(g1 / 100);
        tB = 1+(g2 / 100);
        anos = 1;
        pa = (long)(pa * tA);
        pb = (long)(pb * tB);
        while (pa <= pb)
        {
            anos++;
            pa = (long)(pa * tA);
            pb = (long)(pb * tB);
            if (anos > 100)
            {
                printf("Mais de 1 seculo.\n");
                break;
            }
        }
        if (anos <= 100)
        {
            printf("%d anos.\n", anos);
        }
    i++;
    }
    return 0;
}