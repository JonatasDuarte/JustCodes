#include<stdio.h>
//Maria Cara 0
// João Coroa 1
int main(){
    int n, i, mary, jon, moeda;
    
    while(n!=0){
        scanf("%d", &n);
        mary = 0;
        jon = 0;
        i = 0;
        while(i<n){
            scanf("%d", &moeda);
            if(moeda == 0){
                mary++;
            } else{
                jon++;
            }
            i++;
        }
        if(n==0){
            break;
        }
        printf("Mary won %d times and John won %d times\n", mary, jon);
    }

    return 0;
}