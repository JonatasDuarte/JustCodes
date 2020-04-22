#include<stdio.h>
#include<stdio.h>

int main(){
    int n, len1, len2;
    int i, j, k;
    i=k=j=len1=len2=0;
    char pa1[51], pa2[51], nova[101];
    scanf("%d", &n);
    for(k = 0; k<n; k++){    
        scanf("%s %s", &pa1, &pa2);
        len1 = strlen(pa1);
        len2 = strlen(pa2);
        
        for (i = 0, j=0; i < len1 && i < len2; i++, j+=2) {
            nova[j] = pa1[i];
            nova[j + 1] = pa2[i];
        }
        for (; i < len1; ++i, j++){
            nova[j] = pa1[i];
        }
        for (; i < len2; ++i, j++){
            nova[j] = pa2[i];
        }
        nova[j] = '\0';

        puts(nova);
    }
    return 0;
}