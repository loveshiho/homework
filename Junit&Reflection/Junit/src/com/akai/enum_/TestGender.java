package com.akai.enum_;

public class TestGender {
    public static void main(String[] args) {
        Gender man = Gender.MAN;

        System.out.println(man);
        System.out.println(man.getSex());

        System.out.println(Gender.class.getSuperclass().getName()); // java.lang.Enum

        System.out.println("---------------");
        Gender[] values = Gender.values();
        for(Gender g : values) {
            System.out.println(g.toString());
            /*
            * MAN
            * WOMEN
            * */
        }
        System.out.println("---------------");
        man.show();
    }
}
