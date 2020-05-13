#include<cstdio>
#include<iostream>
#include<vector>
#include<array>
//~ #include<utility>
#include<array>

using namespace std;

string getKey(string s){
    string ans;
    array<int, 26> ca {};
    for(char ci: s) ca[ci-'a'] += 1;
    for(int i = 0; i<(int)ca.size(); ++i){
        for(int j = 0; j<ca[i]; ++j)
            ans += ('a'+i);
    }
    return ans;
}
int main(){
    //~ vector of strings
    //~ std::vector<string> s = {"abc", "bcd", "efg", "ghi", "ijk"};
    //~ std::vector<string> v(5, "abc");
    //~ for(unsigned i=0;i<s.size();++i){
        //~ printf("%s", s[i].c_str());
        //~ cout<<v[i];
    //~ }
    
    /*
     * stl::array of characters
     * */
    
    return 0;
}
