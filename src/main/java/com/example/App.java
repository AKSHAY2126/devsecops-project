// package com.example;

// public class App {
//     public static void main(String[] args) {
//         System.out.println("Hello SonarQube!");
//     }

//     // A simple method to trigger sonar analysis
//     public int addNumbers(int a, int b) {
//         return a + b;
//     }
// }




package com.example;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello SonarQube!");

        // Code smell: Resource not closed (Scanner not closed)
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = sc.nextLine();
        System.out.println("Welcome " + name);

        // Code smell: Hardcoded credentials (security hotspot)
        // String password = "Admin@123";

        // Bug: Possible division by zero
        int x = 10;
        int y = 0; // risky
        int result = x / y; // runtime error risk
        System.out.println("Result = " + result);
    }

    // Code smell: Unused method
    public int multiplyNumbers(int a, int b) {
        return a * b;
    }

    // Code smell: Duplicated code
    public int addNumbers(int a, int b) {
        return a + b;
    }

    // Duplicate of addNumbers
    public int sumNumbers(int a, int b) {
        return a + b;
    }
}
