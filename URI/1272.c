#include <stdio.h>
#include<string.h>
#include<math.h>

int main()
{
    int i, n, k, ind, len1;
    scanf("%d", &n);
    getchar();
    for (i = 0; i < n; i++)
    {
        char pa[51], nova[51];
        ind = 0;
        gets(pa);
        len1 = strlen(pa);
        for (k = 0; k < len1; k++)
        {
            if(k == 0 && pa[0] != ' '){
                nova[ind] = pa[0];
                ind++;
            }
            if(pa[k] == ' ' && pa[k+1] == ' '){
                continue;
            } 
            if(pa[k] == ' ' && pa[k+1] != ' '){
                nova[ind] = pa[k+1];
                ind++;
            }
        }
        nova[ind] = '\0';
        puts(nova);
    }
    return 0;
}