package com.company;

import java.awt.*;
import java.util.Arrays;
import java.util.Date;
import java.util.function.DoubleToIntFunction;

public class Main {

    public static void main(String[] args) {
        // Below are examples of primitve variable types
        // Type     Bytes       Range
        // byte     1           [-128, 127]
        // short    2           [-32K, 32K]
        // int      4           [-2B, 2B]
        // long     8
        // float    4
        // double   8
        // char     2           A,B,C...
        // boolean  1           true/ false
        int myAge = 30;
        int herAge = myAge;
        byte age = 30;
        int viewsCount = 123_456_789;
        long viewsCountLong = 3_123_456_789L;
        double price = 10.99;
        float priceFloat = 10.99F;
        char letter = 'A';
        boolean isEligible = true;

        // below is an example of reference variable type. Reference variable types have methods
        Date now = new Date();
        // now.getTime();
	    //System.out.println(now);
	    int x = 1;
	    int y = 1;
        Point point1 = new Point(x,y);
        Point point2 = point1;
        point1.x = 2;
        //System.out.println(point2);
        String message = "Hello \"World\"" + "!!";
        message.endsWith("!!");
        //System.out.println(message);
        //System.out.println(message.endsWith("!!"));
        //System.out.println(message.indexOf("H"));
        //System.out.println(message.replace("!", "*"));
        //System.out.println(message);

        // Arrays
        int[] numbers = new int[5];
        numbers[0] = 1;
        numbers[1] = 2;
        String num_arr = Arrays.toString(numbers);
        System.out.println(num_arr);
    }
}
