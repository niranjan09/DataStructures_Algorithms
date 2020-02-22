#include"cstdio"
#include<iostream>
#include <unordered_map>
#include <functional>
#include <utility>

using namespace std;


struct hash_pair { 
    template <class T1, class T2> 
    size_t operator()(const pair<T1, T2>& p) const
    { 
        auto hash1 = hash<T1>{}(p.first); 
        auto hash2 = hash<T2>{}(p.second); 
        return hash1 ^ hash2; 
    } 
}; 


int main(){
    unordered_map<pair<int, int>, int, hash_pair> u;
    for(int i = 0; i< 10; ++i){
        u[make_pair(i, i+1)] = i+2;
    }
    for(int i = 0; i< 10; ++i){
        cout<<u[make_pair(i, i+1)];
    }
    return 0;    
}
