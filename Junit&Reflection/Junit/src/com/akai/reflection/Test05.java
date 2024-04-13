package com.akai.reflection;

import java.lang.annotation.Annotation;

public class Test05 {
    public static void main(String[] args) {
        Class<Student> studentClass = Student.class;
        // 获取运行时类的接口
        Class<?>[] interfaces = studentClass.getInterfaces();
        for (Class<?> anInterface : interfaces) {
            System.out.println(anInterface);    // interface java.lang.Comparable
        }
        // 获取运行时类的所在包
        Package aPackage = studentClass.getPackage();
        System.out.println(aPackage);               // package com.akai.reflection
        System.out.println(aPackage.getName());     // com.akai.reflection
        // 获取运行时类的注解
        Annotation[] annotations = studentClass.getAnnotations();
        for (Annotation annotation : annotations) {
            System.out.println(annotation);
        }
    }
}
