#include<bits/stdc++.h>
#define FOR(i, s, e) for(int i = s; i<e; ++i)
#define PB push_back
#define SZ(c) ((int)c.size())
using namespace std;

int findPivotOfRotated(vector<int> &arr){
    int l = 0, r = SZ(arr)-1, m;
    if(arr[l]<arr[r]) return -1;
    if(l==r) return l;
    while(arr[l]>arr[r]){
        cout<<l<<" "<<r<<endl;
        m = (l+r)/2;
        //cout<<arr[m]<< " " << arr[l]<<" "<<arr[r]<<endl;
        if(arr[m]>=arr[l]) l = m+1;
        else r = m;
    }
    return l;
}

int leftBound(vector<int> arr, int l, int r, int target){
    int m;
    while(l<r)

}



int binarySearch(vector<int> arr, int l, int r, int target){
    int m;
    while(l<r){
        m = (l+r)/2;
        if(arr[m]>=target) r = m;
        else l = m+1;
    }
    return arr[r] == target ? r : -1;
}

int main(){
    vector<int> arr{4, 4, 4, 4, 4, 4,4,4};
    //FOR(i, 0, 20) arr.PB(i);
    //rotate(arr.begin(), arr.begin()+4, arr.end());
    //FOR(i, 0, 20) cout<<arr[i];
    cout<<findPivot(arr);
    //cout<<findPivot(arr);
    return 0;
}
