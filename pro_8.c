#include <stdio.h>
int gcd(int n1,int n2){
	int i,gcd=0;
	 for(i=1; i <= n1 && i <= n2; ++i)
    {
        // Checks if i is factor of both integers
        if(n1%i==0 && n2%i==0)
            gcd = i;
    }
    return gcd;
}
int main(void) {
	int N,Q,i;
scanf("%d %d",&N,&Q);
int A[N];
for(i=0;i<N;i++){
	scanf("%d",&A[i]);
}
int L[N],R[N];
for(i=0;i<Q;i++){
	scanf("%d %d",&L[i],&R[i]);
}
for(i=0;i<Q;i++){
printf("%d\n",gcd(L[i],R[i]));	
}

	return 0;
}
