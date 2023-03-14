import java.util.Scanner;

public class MinuteToSecond {
    public static int MinuteToSecond(int minutes) {
        int result = 0;
        result = minutes * 60;

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        sc.close();
        System.out.println(MinuteToSecond(input));
    }
}
