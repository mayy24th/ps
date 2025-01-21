package org.elice;

import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static int[] A;
    static int[] B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        A = new int[N];
        B = new int[N];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(binarySearch());
    }

    public static int findRes(int mid){
        int res = 0;
        for(int i=0; i<N; i++){
            if(A[i] + mid >= B[i]) {
                res ++;
            }
        }

        return res;
    }

    public static int binarySearch(){
        int left = 0, right = (int)1e9;

        while(left <= right){
            int mid = (left + right) / 2;

            if(findRes(mid) >= K){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
}
