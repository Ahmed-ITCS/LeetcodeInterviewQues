class Solution {
public:
    int reverse(int x) {
        
        int answer = 0; 
        //int mul
        while(x!=0){
            answer += (x%10);
            answer *= 10;
            x /= 10;

        }
        answer /=10;
        
        return answer;
    }
};
