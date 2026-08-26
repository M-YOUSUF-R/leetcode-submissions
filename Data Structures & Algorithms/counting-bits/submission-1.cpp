class Solution {
public:
    vector<int> countBits(int n) {
        int count = 0;   
        vector<int>vec;
        for(int i = 0 ; i <= n ; i++){
            int temp = i;
            int p = 0;
            while(temp / 2){
                p++;
                temp/=2;
            }
            for(int j = p ; j >= 0 ;j-- ){
                if(i & (1 << j)){
                    count++;
                }
            }
            vec.push_back(count);
            count = 0;
        }
        return vec;
    }
};
