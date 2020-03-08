#include<stdio.h>
#include <math.h>

int main() {

    float x1, y1;
    scanf("%f %f", &x1, &y1);

    float x2, y2;
    scanf("%f %f", &x2, &   y2);

    double distancia = pow(
    (pow((x2-x1), 2) + pow((y2-y1), 2)
    ), 0.5);
    
    printf("%.4lf\n", distancia);  
    return 0;
}