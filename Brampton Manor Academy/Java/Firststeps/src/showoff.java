public class showoff {

    public static void main(String[] args) {
        output_string(args[0]);
        simple_maths(args[1],args[2]);
        trueOrFalse(args[1]);
    }

    public static void output_string(String word) {
        System.out.println("You entered " + word);
    }

    public static void simple_maths(String first_number, String second_number) {
        int number1 = Integer.parseInt(first_number);
        int number2 = Integer.parseInt(second_number);
        System.out.println("Number 1 + number 2 is: " + (number1 + number2));
        System.out.println("Number 1 * number 2 is: " + (number1 * number2));
        System.out.println("Number 1 / number 2 is: " + (number1 / number2));
        System.out.println("Number 1 - number 2 is: " + (number1 - number2));
    }

    public static void trueOrFalse(String num) {
        int number1 = Integer.parseInt(num);
        System.out.println("The number is equal to 10: " + (number1 == 10));
    }

}

    
