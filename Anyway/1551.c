#include<stdio.h>

int main(){
    int n, i, j ,k, len, ind, letras;
    scanf("%d", &n);
    char pa[1001], nova[1001];
    getchar();
    
    for(i=0; i<n; i++){
        gets(nova);
        char dic[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        letras = ind = 0;
        len = strlen(nova);
       
        for(j=0; j<strlen(nova);j++){
            for(k=0; k<26; k++){
                if((nova[j] == dic[k]) && (nova[j] != ',') && (nova[j] != ' ')){
                    letras++;
                    dic[k] = '0';
                }
            }
        }
       
        if(letras == 26){
            printf("frase completa\n");
        } else if(letras<26 && letras>=13){
    
            printf("frase quase completa\n");
        } else{
            printf("frase mal elaborada\n");
        }
    }
    return 0;
}