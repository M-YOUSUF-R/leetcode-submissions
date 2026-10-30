#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& numbers, int target) {
        int i = 0 , j = numbers.size() - 1;
        while(i < j){
            if (numbers[i] + numbers[j] == target){
                return {i + 1,j + 1};
            }else if (numbers[i] + numbers[j] < target){
                i++;
            }else{
                j--;
            }
        }
        return {};
    }
};
