package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int N = Integer.parseInt(br.readLine());

        LinkedList<Integer> q = new LinkedList<>();

        for(int i=1; i<=N; i++){
            q.addLast(i);
        }

        while(true){
            if(q.size()==1){
                System.out.println(q.peek());
                break;
            }

            q.removeFirst();
            q.addLast(q.removeFirst());
        }
    }
}