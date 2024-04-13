package com.akai.reflection;

public class Student extends Person implements Comparable{
    private int sno;
    private double height;
    private double weight;

    public String sex;

    public void showStudent() {
        System.out.println("我是学生");
    }

    public void work() {
        System.out.println("我爱学JAVA");
    }

    @Override
    public String toString() {
        return "Student{" +
                "sno=" + sno +
                ", height=" + height +
                ", weight=" + weight +
                ", sex='" + sex + '\'' +
                '}';
    }

    public Student() {
    }

    public Student(int sno, double height, double weight) {
        this.sno = sno;
        this.height = height;
        this.weight = weight;
    }
    private Student(int sno) {
        this.sno = sno;
    }
    public int getSno() {
        return sno;
    }

    public void setSno(int sno) {
        this.sno = sno;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    @Override
    public int compareTo(Object o) {
        return 0;
    }
}
