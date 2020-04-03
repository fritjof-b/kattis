import java.util.Scanner;

class Stones {
    public static void main(String[] args) {
        var winner = "";
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLong()) {
            long a = sc.nextLong();
            if (a % 2 != 0) {
                winner = "Alice";
            } else {
                winner = "Bob";
            }
            System.out.println(winner);
        }
    }
}
