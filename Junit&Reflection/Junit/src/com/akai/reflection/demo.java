package com.akai.reflection;

public class demo {
    public static void main(String[] args) {
        Class c_1 = Person.class;
        Class c_2 = Comparable.class;
        Class c_3 = Override.class;
        int[] arr_1 = {1, 2, 3};
        int[] arr_2 = {4, 5, 6};
        Class a_1 = arr_1.getClass();
        Class a_2 = arr_2.getClass();
        System.out.println(a_1);
        System.out.println(a_1 == a_2); // true，同一个纬度，同一个元素类型，得到的字节码就是同一个
        Class c_4 = int.class;
        Class c_5 = void.class;
        System.out.println(c_1);    // class com.akai.reflection.Person
        System.out.println(c_2);    // interface java.lang.Comparable
        System.out.println(c_3);    // interface java.lang.Override
        System.out.println(c_4);    // int
        System.out.println(c_5);    // void
    }
}
