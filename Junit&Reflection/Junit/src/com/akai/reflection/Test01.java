package com.akai.reflection;

import java.lang.reflect.Constructor;

public class Test01 {
    public static void main(String[] args) throws Exception{
        // person
        // 方式1：通过getClass()方法
        Person p = new Person();
        Class c_1 = p.getClass();
        System.out.println(c_1);

        // 方式2：通过内置class属性
        Class c_2 = Person.class;
        System.out.println(c_2);
        // 方式1和方式2  不常用

        // 方式3：用的最多，调用Class类提供的静态方法forName
        Class c_3 = Class.forName("com.akai.reflection.Person");
        System.out.println(c_3);

        // 获取字节码信息
        Class c_4 = Student.class;

        // 通过字节码信息获取构造器
        // getConstructors：只能获取运行时类的 被public修饰的构造器
        Constructor[] constructors = c_4.getConstructors();
        for(Constructor c : constructors) {
            System.out.println(c);
        }

        // getDeclaredConstructors：获取运行时类的所有构造器
        Constructor[] declaredConstructors = c_4.getDeclaredConstructors();
        for (Constructor d : declaredConstructors) {
            System.out.println(d);
        }

        // 获取指定构造器
        // 得到空构造器
        Constructor constructor = c_4.getConstructor();
        System.out.println(constructor);

        // 得到有参构造器
        Constructor constructor1 = c_4.getConstructor(int.class, double.class, double.class);
        System.out.println(constructor1);

        // 得到有参构造器，并且是private修饰的
        Constructor declaredConstructor = c_4.getDeclaredConstructor(int.class);
        System.out.println(declaredConstructor);

        // 有了构造器以后，我们就可以创建对象
        Object o = constructor.newInstance();
        System.out.println(o);
    }
}
