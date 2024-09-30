package org.elice;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 공백을 기준으로 정수를 입력받을 때 버퍼리더 말고 스캐너
        int N = sc.nextInt();
        int K = sc.nextInt();

        // 1~N까지 숫자를 저장할 list
        // list에서 K번째 수를 삭제하고 저장할 res
        LinkedList<Integer> list = new LinkedList<>();
        LinkedList<Integer> res = new LinkedList<>();

        // 1~N까지 list에 추가
        for(int i=1; i<=N; i++) list.addLast(i);

        /*
        list가 비워질때까지 반복하며 idx위치에 있는 요소를 삭제하고 res에 추가
        idx는 삭제한 위치로부터 3칸 떨어진 요소의 위치를 나타냄
        idx가 list의 사이즈보다 클 경우 idx%=list.size()로 다시 앞에서부터

        예를들어 최초 리스트가 아래와 같고,
        idx = 0
        list = {1, 2, 3, 4, 5, 6, 7}
        res = {}

        ----------------------------
        1회 Before
        idx = 2, size = 7, list[idx] = 3
        list = {1, 2, 3, 4, 5, 6, 7}
        res = {}
        1회 after
        idx = 2, size = 6, list[idx] = 4
        list = {1, 2, 4, 5, 6, 7}
        res = {3}
        ----------------------------
        2회 Before
        idx = 4, size = 6, list[idx] = 6
        list = {1, 2, 4, 5, 6, 7}
        res = {3}
        2회 after
        idx = 4, size = 5, list[idx] = 7
        list = {1, 2, 4, 6, 7}
        res = {3, 6}
        ----------------------------
        3회 Before
        idx = 6 -> idx%=list.size() -> 1, size = 5, list[idx] = 2
        list = {1, 2, 4, 6, 7}
        res = {3, 6}
        3회 after
        idx = 1, size = 4, list[idx] = 4
        list = {1, 4, 6, 7}
        res = {3, 6, 2}
         */
        int idx = 0;
        while(!list.isEmpty()){
            idx = idx + (K-1);
            if(idx >= list.size()){
                idx %= list.size();
            }
            res.addLast(list.remove(idx));
        }

        System.out.println(formatList(res));
    }

    // [1, 2, 3, 4, 5] -> <1, 2, 3, 4, 5> 출력 포맷 바꾸기
    public static String formatList(LinkedList<?> list) {
        StringBuilder sb = new StringBuilder();
        sb.append("<");  // 여는 괄호를 '<'로 변경
        for (int i = 0; i < list.size(); i++) {
            sb.append(list.get(i));
            if (i < list.size() - 1) {
                sb.append(", ");  // 마지막 요소가 아니면 콤마 추가
            }
        }
        sb.append(">");  // 닫는 괄호를 '>'로 변경
        return sb.toString();
    }
}