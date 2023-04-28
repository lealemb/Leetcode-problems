
class Solution {
public:
    bool isPalindrome(int x) {
      
        string n = to_string(x);
        string ok = n;
        reverse(n.begin(),n.end());
        if(n==ok) return true;
        else return false; 
      
    }
};
