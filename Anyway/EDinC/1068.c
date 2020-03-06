#include <stdio.h>
#include <string.h>

int main (void){
  int i, j, n;
  while(scanf("%d", &n) != EOF){
    int count = 0, tru = 0;
    char exp[1001];
    scanf("%s", exp);
    for(i =0; exp[i] !='\0'; i++){
      if(exp[i] == '(' || exp[i] == ')') count++;

      if(exp[i] == '('){
        tru = 1;
      }
      if(exp[i] == ')' && tru == 1){
        tru = 0;
      }
    }
    if(count%2 != 0)
      printf("incorrect\n");
    else if(tru == 1)
      printf("incorrect\n");
    else
      printf("correct\n");
  }
}