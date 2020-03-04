import java.util.Scanner;

public class Tarifa {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int monthlyAllowance = sc.nextInt();
    int months = sc.nextInt();
    int total = 0;

    for(int i = 0; i < months; i++){
        total += sc.nextInt();
    }

    System.out.println(monthlyAllowance * (months + 1) - total);
  }
}
