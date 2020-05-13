#include<bits/stdc++.h>
using namespace std;

#define FOR(i, s, e) for(int i = s; i<e; ++i)
#define SZ(container) ((int)container.size())
#define PB(vi) push_back(vi)

using VI = vector<int>;

void leftRotateInPlace(VI &a, int d){
    int start = 0, cnt = 0;
    while(cnt<SZ(a)){
        int ni = start, nv = a[ni];
        do{
            swap(nv, a[(ni+SZ(a)-d)%SZ(a)]);
            ni = (ni+SZ(a)-d)%SZ(a);
            cnt += 1;
        }while(ni != start);
        start+=1;
    }    
}

int main(){
        VI a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        // My Left rotate Function
        leftRotateInPlace(a, 3);
        FOR(i, 0, SZ(a)){
            cout<<a[i]<<" ";
        }
        cout<<endl;
        // C++ built in function for rotating containers
        rotate(a.begin(), a.begin()+3, a.end());
        FOR(i, 0, SZ(a)){
            cout<<a[i]<<" ";
        }        
        
    return 0;
}
