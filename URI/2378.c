#include<stdio.h>

int main () {
    int n,c, i, s, e, pes;
    pes = 0;
    char max ='N';
    scanf("%d %d", &n, &c);
    for(i=0;i<n;i++){
        scanf("%d %d", &s, &e);
        pes = pes + e - s;
		if(pes>c){
            max = 'S';
        }
	}
	printf("%c\n",max);
}