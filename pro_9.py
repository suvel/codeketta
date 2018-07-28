#include <iostream>
using namespace std;
int fun(int i){
	if(3<=i and i<=7);
	return i;
	if(i>7){
	i=fun(i-4)+4;	
	}
	return i;
}
int main() {
	int i;
	cin>>i;
	i=fun(i);
	cout<<i;
	return 0;
};
