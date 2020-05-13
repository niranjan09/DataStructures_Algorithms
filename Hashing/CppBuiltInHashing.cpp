#include"cstdio"
#include<iostream>
#include<map>
#include<utility>
#include <unordered_map>
#include <functional>
#include <utility>
#define FOR(i, s, e) for(int i=s; i<e; ++i)
using UMii=std::unordered_map<int, int>;
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
    
    // Unordered map of unordered maps
    unordered_map<int, UMii> u1;
    FOR(i, 0, 10){
        //UMii u2;
        // No need to explicitly create new object and then assign, we can directly
        // assign the value, unless and untill types are matching.
        FOR(j, 0, 10){
            u1[i][j] = i*j;
        }
        //cout<<u1[i].size()<<u1.size();
    }
    FOR(i, 0, 10){
        FOR(j, 0, 10){
            cout<<u1[i][j]<<" ";
        }   
        cout<<endl;
    }
    
    
    return 0;    
}
