#include<bits/stdc++.h>
using namespace std;

/* Start of commonly used datatypes and constructs*/
using LL = long long;
#define FOR(i, s, e) for(LL i = s; i<e; ++i)
#define RFOR(i, s, e) for(LL i = s; i>e; --i)

#define F first
#define S second
#define SZ(container) ((int)container.size())
#define ALL(container) container.begin(), container.end()
#define MP(k, v) make_pair(k, v)
#define MT(i1, i2, i3) make_tuple(i1, i2, i3)
#define PB(vi) push_back(vi)
#define POP(vi) pop_back(vi)
#define UM unordered_map
#define US unordered_set

using PII = pair<int, int>; using PLL = pair<LL, LL>;
using VI = vector<int>; using VL = vector<LL>;
using VVI = vector<VI>; using VVL = vector<VL>;
using VPII = vector<PII>; using VPLL = vector<PLL>;
using UMII = UM<int, int>; using UMLL = UM<LL, LL>;
using UMCI = UM<char, int>; using UMCL = UM<char, LL>;
using USI = US<int>; using USL = US<LL>;
/* Start of commonly used functions */
void SC(int &i) {scanf("%d", &i);}
void SC(int &i, int &j) {scanf("%d %d", &i, &j);}
void SC(int &i, int &j, int &k) {scanf("%d %d %d", &i, &j, &k);}
void SC(LL &i) {scanf("%lld", &i);}
void SC(LL &i, LL &j) {scanf("%lld %lld", &i, &j);}
void SC(LL &i, LL &j, LL &k) {scanf("%lld %lld %lld", &i, &j, &k);}

void print(VL arr, const string sep = " ", const string end = "\n"){FOR(i, 0, SZ(arr)) printf("%lld%s", arr[i], sep.c_str()); printf("%s", end.c_str());}
void print(VI arr, const string sep = " ", const string end = "\n"){FOR(i, 0, SZ(arr)) printf("%d%s", arr[i], sep.c_str()); printf("%s", end.c_str());}


/* Start of commonly used constants */
const int INF = 1e9;
const int MOD = 1e9+7;

int main(){
    int T;
    SC(T);
    while(T--){
        int m, n;
        SC(m, n);
        
    }
    return 0;
}
