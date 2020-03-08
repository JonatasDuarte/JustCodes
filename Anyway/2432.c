#include <stdlib.h>
#include <stdio.h>
#include <math.h>
typedef struct
{
    long long int x, y;
} Tiro;

int main(void)
{
    long int c, t, i;
    long int pontos = 0;
    scanf("%ld %ld", &c, &t);
    long int circles[c];
    Tiro tiros[t];
    
    for (i = 0; i < c; i++)
        scanf("%ld", &circles[i]);

    for (i = 0; i < t; i++)
        scanf("%lld %lld", &tiros[i].x, &tiros[i].y);

    for (i = 0; i < t; i++)
    {
        double tiro_centro = sqrt((tiros[i].x * tiros[i].x) + (tiros[i].y * tiros[i].y));
        
        int m, j = 0, f = c - 1, ponto = 0;
        while (j <= f)
        {
            m = (j + f) / 2;
            if (tiro_centro <= circles[m])
            {
                ponto = c - m;
                f = m - 1;
            }
            else if (tiro_centro > circles[m])
                j = m + 1;
            else
                f = m - 1;
        }
        pontos += ponto;
    }
    printf("%ld\n", pontos);
}