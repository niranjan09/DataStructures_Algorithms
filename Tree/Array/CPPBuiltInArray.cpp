#include<stdio.h>
#include<iostream>
#include<vector>
#include<utility>

using namespace std;

int main(){
    // std::vector<string> s = {"abc", "bcd", "efg", "ghi", "ijk"};
    // std::vector<string> v(5, "abc");
    // for(int i=0;i<s.size();++i){
    //   printf("%s", s[i].c_str());
    //   cout<<v[i];
    // }
//    for(iterator it = )
int x = 5;
int *ptr = &x;
int * &ptr1 = ptr;
int y = 6;
ptr1 = &y;
cout<<x<<endl<<*ptr<<endl<<ptr1;
return 0;
}
