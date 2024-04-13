package com.akai.pay;

import java.lang.reflect.Method;

public class TestReflection {
    public static void main(String[] args) throws Exception{
        String str = "com.akai.pay.WeChat"; // 微信类的全限定路径
        // 反射演示
        Class cls = Class.forName(str);
        Object o = cls.newInstance();
        Method method = cls.getMethod("pay");
        method.invoke(o); // 正在使用微信支付
    }
}
