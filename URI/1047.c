#include<stdio.h>
int main(){
    int hi, mi, hf, mf, mti, mtf;
    int horas, minutos;
    scanf("%d %d %d %d", &hi, &mi, &hf, &mf);
    mti = (hi*60) + mi;
    mtf = (hf*60) + mf;
    if (mtf > mti){
        horas = (mtf - mti)/60;
        minutos = (mtf - mti)%60;
    }
    else{
        minutos = 1440 - (mti - mtf);
        horas = minutos/60;
        minutos %= 60;
    }
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", horas, minutos);
    return 0;
}