package org.elice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        ArrayDeque<Integer> deque;
        int tc = Integer.parseInt(br.readLine());

        while(tc --> 0) {
            String op = br.readLine();
            int len = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine(), "[],");

            deque = new ArrayDeque<>();
            for (int i = 0; i < len; i++)
                deque.add(Integer.parseInt(st.nextToken()));

            boolean left = true;
            boolean isError = false;

            for (int i = 0; i < op.length(); i++) {
                if (op.charAt(i) == 'R') {
                    if (left)
                        left = false;
                    else
                        left = true;
                } else if (op.charAt(i) == 'D') {
                    if (deque.isEmpty()) {
                        System.out.println("error");
                        isError = true;
                        break;
                    } else {
                        if (left) {
                            deque.pollFirst();
                        } else {
                            deque.pollLast();
                        }
                    }
                }
            }
            if(!isError) {
                sb.append('[');
                if(left) {
                    while(!deque.isEmpty()) {
                        sb.append(deque.pollFirst());
                        if(!deque.isEmpty()) sb.append(',');
                    }
                } else {
                    while(!deque.isEmpty()) {
                        sb.append(deque.pollLast());
                        if(!deque.isEmpty()) sb.append(',');
                    }
                }
                sb.append(']').append('\n');
                System.out.print(sb);
                sb.setLength(0);
            }
        }
    }
}