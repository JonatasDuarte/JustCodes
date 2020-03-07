#include<stdio.h>
#include <math.h>

int main() {

    int horas;
    scanf("%d", &horas);
    float km;
    scanf("%f", &km);
    double litros = (km/12)*horas;
    printf("%.3lf\n", litros);  
    return 0;
}