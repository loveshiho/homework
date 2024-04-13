package com.akai.reflection;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;

public class Test03 {
    public static void main(String[] args) throws Exception{
        Class cls = Student.class;
        // 获取属性
        // getFields：获取运行时类和父类中被public修饰的属性
        Field[] fields = cls.getFields();
        for (Field field : fields) {
            System.out.println(field);
            // public java.lang.String com.akai.reflection.Student.sex
            // public java.lang.String com.akai.reflection.Person.name
        }
        System.out.println("--------------------------------------------------");
        // getDeclaredFields：获取运行时类的所有属性
        Field[] declaredFields = cls.getDeclaredFields();
        for (Field declaredField : declaredFields) {
            System.out.println(declaredField);
        }
        System.out.println("--------------------------------------------------");
        // 获取指定属性
        // getField：只能获取被public修饰的 属性
        // getDeclaredField：获取所有属性
        Field sex = cls.getField("sex");
        System.out.println(sex);
        Field sno = cls.getDeclaredField("sno");
        System.out.println(sno);
        System.out.println("--------------------------------------------------");
        // 属性的具体结构
        // 获取修饰符
        int modifiers = sno.getModifiers();
        System.out.println(modifiers); // 数字 2
        System.out.println(Modifier.toString(modifiers)); // private
        // 获取属性的数据类型
        Class<?> type = sno.getType();
        System.out.println(type);
        // 获取属性名
        String name = sno.getName();
        System.out.println(name);
        // 给属性赋值，私有属性不可赋值
        Object o = cls.newInstance();
        sex.set(o, "1");
        System.out.println(o);  // Student{sno=0, height=0.0, weight=0.0, sex='1'}
    }
}
