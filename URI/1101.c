#include <stdio.h>

int main()
{
    int n1, n2, soma, temp;
    while (1)
    {
        soma = 0;
        scanf("%d %d", &n1, &n2);
        if ((n1 <= 0) | (n2 <= 0))
        {
            break;
        }
        if (n1>n2){
            temp = n2;
            n2 = n1;
            n1 = temp;
        }
        while (n1 <= n2)
        {
            soma += n1;
            printf("%d ",n1);
            n1++;
            
        }
        
        printf("Sum=%d\n", soma); 
        
    }

    return 0;
}