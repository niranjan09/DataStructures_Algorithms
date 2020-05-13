#include<bits/stdc++.h>

using namespace std;

int knapSack(vector<int> &items, vector<int> &weights, int W){
    int ilen = items.size();
    int m[ilen+1][W+1] = {};
    for(int i = 1; i< ilen+1; ++i){
        for(int j = 1; j<W+1; ++j){
            m[i][j] = max((j-weights[i-1])>=0?m[i-1][j-weights[i-1]] + items[i-1] : 0, m[i-1][j]);
            //cout<<m[i][j]<<" ";
        }
        //cout<<endl;
    }
    return m[ilen][W];
}

int main(){
    vector<int> items = {10, 40, 30, 50}, weights = {5, 4, 6, 3};
    cout<<knapSack(items, weights, 10);
    return 0;
}
