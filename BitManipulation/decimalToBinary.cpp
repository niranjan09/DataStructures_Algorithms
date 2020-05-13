#include<iostream>
#include<string>

using namespace std;

string bin(int n){
    string ans;
    for(int i=1<<30;i>0;i>>=1)
        ans+=(n&i ? '1' : '0');
    return ans;
}
int main(){
    int temp=12;
    cout<<"converting...";
    string tempans = bin(temp);
    cout<<tempans;
    return 0;
}
