#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);

    int array[1000];
    int i, j, key;
    for(i=0; i < n; i++){
        scanf("%d", &array[i]);
    }

    for(i=0; i<n-1; i++){
        j=i;
        while(j >=0 && array[j] > array[j+1]){
            key = array[j];
            array[j] = array[j+1];
            array[j+1] = key;
            j--;
        }
    }
    int sum=0, result=0;
    for(i=0;i<n;i++){
        sum+=array[i];
        result+=sum;
    }
    printf("%d", result);
}
