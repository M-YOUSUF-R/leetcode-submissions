class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int number = 0;
        for(auto &itr:nums){
            number^= itr;
        }
        return number;
    }
};
