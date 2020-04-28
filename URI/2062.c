#include <stdio.h>
#include <ctype.h>

int main()
{
    int n, i, j, tam;
    scanf("%d", &n);
    char pa[9999];

    for (i = 0; i < n; i++){
        scanf("%s", pa);
        tam = strlen(pa);
        for(j=0; j<tam-1; j++){
            toupper(pa[j]);
        }
        if (tam == 3)
        {
            if (pa[0] == 'U' && pa[1] == 'R')
            {
                printf("URI");
            }
            else if (pa[0] == 'O' && pa[1] == 'B')
            {
                printf("OBI");
            }
            else
            {
                printf("%s", pa);
            }
        }
        else
        {
            printf("%s", pa);
        }
        if (i < n - 1){
            printf(" ");
        }
}
printf("\n");
return 0;
}