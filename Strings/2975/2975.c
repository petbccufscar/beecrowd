#include <stdio.h>
#include <string.h>

#define MAX 100010

#define min(a, b) (a < b ? a : b)





void computeLPSArray(char* pat, int M, int* lps) { 
    
    int len = 0; 
  
    lps[0] = 0;
  
    int i = 1; 
    while (i < M) { 
        if (pat[i] == pat[len]) { 
            len++; 
            lps[i] = len; 
            i++; 
        } 
        else {  
            if (len != 0) {
                len = lps[len - 1]; 
            } 
            else {
             
                lps[i] = 0; 
                i++; 
            } 
        } 
    } 
} 





int KMPSearch(char* pat, char* txt) { 
    int ret = 0;
    int M = strlen(pat);
    int N = strlen(txt);
  

    int lps[M];
    computeLPSArray(pat, M, lps); 
  
    int i = 0;
    int j = 0;


    while (i < N-1) {
        if (pat[j] == txt[i]) {
            j++; 
            i++; 
        } 
  
        if (j == M) {
            ret++; 
            j = lps[j - 1];
        } 
  
        else if (i < N && pat[j] != txt[i]) { 
            if (j != 0)
                j = lps[j - 1]; 
            else
                i = i + 1;
        } 
    } 
    return ret;
} 
  




int main(int argc, char **argv) {
    char str[2*MAX];
    scanf("%s", str);
    int i, j, k, len = strlen(str);

    i = 0, j = 1, k = 0;
    while (k < len && i < len && j < len) {
            int idx1 = (i+k)%len, idx2 = (j+k)%len;
            if (str[idx1] == str[idx2]) {
                k++;
            } else {
                if (str[idx1] < str[idx2]) {
                    i = i + k + 1;
                } else {
                    j = j + k + 1;
                }
                if (i == j) {
                    i++;
                }
                k = 0;
            } 
        }
    int maxIdx = min(i, j);
    
    char pat[MAX];
    int sz = 0;
    for(k = maxIdx; k < len+maxIdx; ++k) pat[sz++] = str[k%len];
    pat[sz] = '\0';
    for(i = 0; i < len; ++i) str[i + len] = str[i];
    str[2*len] = '\0';


    printf("%d %d\n", KMPSearch(pat, str), maxIdx+1);

    return 0;
}