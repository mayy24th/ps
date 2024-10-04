package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

class Pair{
    int topNumber;
    int topIndex;

    Pair(int topNumber, int topIndex){
        this.topNumber = topNumber;
        this.topIndex = topIndex;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(100000001, 0));

        for(int i=1; i<=N; i++){
            int num = Integer.parseInt(st.nextToken());

            while(stack.peek().topNumber < num) stack.pop();

            System.out.print(stack.peek().topIndex + " ");
            stack.push(new Pair(num, i));
        }
    }
}