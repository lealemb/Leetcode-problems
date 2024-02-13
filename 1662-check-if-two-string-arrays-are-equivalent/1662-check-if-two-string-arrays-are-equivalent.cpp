class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        
        string s1,s2;
        
        int n=word1.size();
        int m=word2.size();
        for(int i=0;i<n;i++){
            s1=s1+word1[i];
            
        }
        for(int i=0;i<m;i++){
            s2=s2+word2[i];
        }
        if(s1==s2)
            return true;
        else
            return false;
        
    }
};
