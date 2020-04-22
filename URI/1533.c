#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n, j, temp;
    scanf("%d", &n);
    while (n!=0)
    {
        if(n ==0){
            break;
        }
        int i;
        int numeros[n + 1], posi[n + 1];
        for (i = 0; i < n; i++)
        {
            scanf("%d", &numeros[i]);
            posi[i] = i + 1;
        }
        for (i = 0; i < n; i++)
        {
            for (j = i + 1; j < n; j++)
            {
                if (numeros[i] > numeros[j])
                {
                    temp = numeros[i];
                    numeros[i] = numeros[j];
                    numeros[j] = temp;
                    temp = posi[i];
                    posi[i] = posi[j];
                    posi[j] = temp;
                }
            }
        }
        printf("%d\n", posi[n-2]);
        scanf("%d", &n);
       
    }
return 0;
}