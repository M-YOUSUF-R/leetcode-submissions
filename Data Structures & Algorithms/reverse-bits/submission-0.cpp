class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int rs = 000000000000000000000000000000000;
        for(int i = 0 ; i < 32 ; i++){
            if(n & (1 << i)){
                rs |=(1 <<(31 - i));
            }
        }
        return rs;
    }
};
