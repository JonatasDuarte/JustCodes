#include <stdio.h>
#include <string.h>
void main()
{
    int n, l, c;
    char pal[71];
    int Pag, Linhas, Chars, i;
    while (scanf("%d %d %d", &n, &l, &c)!=EOF)
    {

        Chars = Linhas = Pag = 0;

        for (i = 1; i <= n; i++)
        {
            scanf("%s", pal);
            Chars += strlen(pal);

            if (Chars > c)
            {
                Linhas++;
                Chars = strlen(pal) + 1;
            }
            else if (Chars == c)
            {
                Linhas++;
                Chars = 0;
            }
            else if (i < n)
            {
                Chars++;

                if (Chars == c)
                {
                    Chars = 0;
                    Linhas++;
                }
            }

            if (Linhas == l)
            {
                Linhas = 0;
                Pag++;
            }
        }
        if (Linhas > 0 || Chars > 0)
            Pag++;
        printf("%d\n", Pag);
    }
}