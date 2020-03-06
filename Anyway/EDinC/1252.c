#include <stdlib.h>
#include <stdio.h>

int m;
int compare(const void *n1, const void *n2){
    int *v1 = (int*)n1, *v2 = (int*)n2;
    int a = *(v1), b = *(v2);      
    
    if((a % m) > (b % m)) return 1;

    else if((a % m) < (b % m)) return -1;

    else{
        if(abs(a)%2 != abs(b)%2){
            if(abs(a)%2 == 0) return 1;
            else return -1;

        } else if(abs(a)%2 == 0){
            if(a > b) return 1;
            else return -1;

        } else {
            if(a < b) return 1;
            else return -1;
        }
    }
}


int main(void){
    int n;
    while(1){
        scanf("%d %d", &n, &m);
        if(n == 0 && m == 0) {
            printf("0 0\n");
            break;
        }
        int nums[n], i;

        for(i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
        }
        qsort(nums, n, sizeof(int), compare);

        printf("%d %d\n", n, m);
        for(i = 0; i < n; i++){ 
            printf("%d\n", nums[i]);
        }
    }
}