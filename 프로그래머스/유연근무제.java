class Solution {
    // 2025 프로그래머스 코드챌린지 1차 예선 > 유연근무제
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;

        int[] admitTime = new int[schedules.length];
        for(int i=0; i<schedules.length; i++){
            admitTime[i] = schedules[i] + 10;
            if(admitTime[i] % 100 >= 60){
                admitTime[i] += 40;
            }
        }

        for(int i=0; i<timelogs.length; i++){
            int cnt = 0;
            for(int j=0; j<7; j++){
                int cur = (startday+j) % 7;
                if(cur == 6 || cur == 0) continue;

                if(timelogs[i][j] <= admitTime[i]) cnt ++;
            }
            if(cnt == 5) answer ++;
        }
        return answer;
    }
}