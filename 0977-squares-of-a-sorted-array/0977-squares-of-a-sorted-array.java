class Solution {
    public int[] sortedSquares(int[] nums) {
        int n=nums.length;
        int[] res=new int[n];
        int index=n-1;
        int left=0;
        int right=n-1;
        while(left<=right){
            int Ls=nums[left]*nums[left];
            int Rs=nums[right]*nums[right];
            if(Ls>Rs){
                res[index]=Ls;
                left++;
            }
            else{
                res[index]=Rs;
                right--;
            }
            index--;
        }
        return res;
    }
}