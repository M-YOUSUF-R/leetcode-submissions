class Solution {
public:
    int missingNumber(vector<int>& nums) {
    
        int ts = 0;
        int r = nums.size();
        ts = r * (r + 1) / 2;
        int vs = 0;
        for(auto &itr:nums){
            vs += itr;
        }
        return(ts - vs);
    }
};
