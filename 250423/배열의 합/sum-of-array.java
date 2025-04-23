import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Please write your code here.

        int n = 4;
        int[][] arr2d = new int[4][4];
        for(int i = 0 ; i < n ; i++){
            for (int j = 0 ; j < n ; j++){
                arr2d[i][j] = sc.nextInt();
            }

        }


        for(int i = 0 ; i < n ; i++){
            int sum = 0;
            for (int j = 0 ; j < n ; j++){
                sum += arr2d[i][j];
            }
            System.out.println(sum);
        }
    }
}