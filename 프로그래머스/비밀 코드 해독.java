import java.util.*;

class Solution {
    static List<List<Integer>> allCase = new ArrayList<>();

    public int solution(int n, int[][] q, int[] ans) {
        int answer = 0;

        List<Integer> nums = new ArrayList<>();
        for(int i=1; i<=n; i++) nums.add(i);

        generateCombi(nums, new ArrayList<>(), 0);

        for(List<Integer> oneCase : allCase){
            if(findAns(oneCase, q, ans) == 1){
                answer ++;
            }
        }
        return answer;
    }

    private int findAns(List<Integer> oneCase, int[][] q, int[] ans){
        int[] res = new int[ans.length];
        int index = 0;
        for(int[] qq : q){
            int cnt = 0;
            for(int num : qq){
                if(oneCase.contains(num)){
                    cnt ++;
                }
            }

            res[index++] = cnt;
        }

        return Arrays.equals(ans, res) ? 1 : 0;
    }

    private void generateCombi(List<Integer> nums, List<Integer> cur, int index){
        if(cur.size() == 5){
            allCase.add(new ArrayList<>(cur));
            return;
        }

        for(int i=index; i<nums.size(); i++){
            cur.add(nums.get(i));
            generateCombi(nums, cur, i+1);
            cur.remove(cur.size()-1);
        }
    }

}