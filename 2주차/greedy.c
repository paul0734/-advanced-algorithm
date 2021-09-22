#include <stdio.h>

int main(){
    int n=0;//동전종류
    int k;//계산할돈
    int cnt=0;
    int i;
    int coinTypes[11];
    scanf("%d %d", &n, &k);
    for(i=0; i<n; i++){
        scanf("%d", &coinTypes[i]);
    }
    for(i = n; i > 0; i--){
        cnt += k/coinTypes[i];
        k %= coinTypes[i];
    }
    printf("count = %d", cnt);
}
