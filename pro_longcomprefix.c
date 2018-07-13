#include<stdio.h>
#include<string.h>

void main(){
int N,i;
scanf("%d",&N);
char name[N][100000];
for(i=0;i<N;i++){
scanf("%s",name[i]);
}
int len,M=0;
for(i=0;i<N;i++){
len=strlen(name[i]);
if(M==0){
M=len;
}
if(M<len){
M=len;
}
}

char ch,newstr[len];
for(i=0;i<len;i++){
int tempN=0;
int count=0;
char MK=NULL;
 while(tempN<N){
if(MK==0 || MK==name[tempN][i]){
MK=name[tempN][i];
count++;
}
tempN++;
 }
if(count==N){
printf("%C",MK);
}
}

}
