package com.akai.enum_;

public enum Gender implements TestInterface{
    // enum枚举类 要求对象必须放在最开始位置
    MAN("1") {
        @Override
        public void show() {
            System.out.println("MAN");
        }
    },
    WOMAN("0");
    private final String sex;

    Gender(String sex) {
        this.sex = sex;
    }

    public String getSex() {
        return sex;
    }

    /*@Override
    public String toString() {
        return "gender{" +
                "sex='" + sex + '\'' +
                '}';
    }*/

    @Override
    public void show() {
        System.out.println("测试接口...");
    }
}
