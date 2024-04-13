package com.akai.enum_;

public class TestPerson {
    public static void main(String[] args) {
        Person p = new Person();
        p.setAge(19);
        p.setName("shiho");
        p.setGender(Gender.WOMAN);
        System.out.println(p);  // Person{age=19, name='shiho', gender=WOMEN}
        Gender sex = Gender.WOMAN;
        switch (sex) {
            case MAN -> System.out.println("MAN");
            case WOMAN -> System.out.println("WOMAN");
        }
    }
}
