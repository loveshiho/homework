package com.akai.reflection;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

public class Test04 {
    public static void main(String[] args) throws Exception {
        Class<Student> studentClass = Student.class;
        // 获取方法
        // getMethods：获取运行时类的方法还有父类中的方法（被public修饰）
        Method[] methods = studentClass.getMethods();
        for (Method method : methods) {
            System.out.println(method);
        }
        System.out.println("______________________________________________________________");
        // getDeclaredMethods：获取运行时类的所有方法
        Method[] declaredMethods = studentClass.getDeclaredMethods();
        for (Method declaredMethod : declaredMethods) {
            System.out.println(declaredMethod);
        }
        // 获取指定方法
        // getMethod：被public修饰的方法
        System.out.println("______________________________________________________________");
        Method showStudent = studentClass.getMethod("showStudent");
        System.out.println(showStudent);
        // getDeclaredMethod：所有方法
        Method getHeight = studentClass.getDeclaredMethod("getHeight");
        System.out.println(getHeight);
        // 获取方法的具体结构
        // 方法名
        System.out.println(showStudent.getName());  // showStudent
        // 修饰符
        int modifiers = showStudent.getModifiers();
        System.out.println(Modifier.toString(modifiers));   // public
        // 返回类型
        System.out.println(showStudent.getReturnType());    // void
        // 参数列表
        Class<?>[] parameterTypes = showStudent.getParameterTypes();
        for (Class<?> parameterType : parameterTypes) {
            System.out.println(parameterType);
        }
        // 获取注解
        Annotation[] annotations = showStudent.getAnnotations();
        for (Annotation annotation : annotations) {
            System.out.println(annotation);
        }
        // 获取异常
        Class<?>[] exceptionTypes = showStudent.getExceptionTypes();
        for (Class<?> exceptionType : exceptionTypes) {
            System.out.println(exceptionType);
        }

        // 调用方法
        Student student = studentClass.newInstance();
        showStudent.invoke(student);   // 我是学生
        // 调用 student对象的 showStudent方法
    }
}
