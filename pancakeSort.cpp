class Solution {
public:
    vector<int> pancakeSort(vector<int>& A) {
        vector<int> flips;
        for(int i=0; i<A.size(); i++){
            auto max_pos = max_element(A.begin(),A.end()-i);
            flips.push_back(max_pos-A.begin()+1);
            flips.push_back(A.size()-i);
            reverse(A.begin(), max_pos+1);
            reverse(A.begin(), A.end()-i);
        }
        return flips;
    }
};
