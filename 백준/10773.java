package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int N = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();

        for(int i=1; i<=N; i++){
            int num = Integer.parseInt(br.readLine());

            if(num == 0) stack.pop();
            else stack.push(num);
        }

        System.out.println(stack.stream().mapToInt(Integer::intValue).sum());
    }
}