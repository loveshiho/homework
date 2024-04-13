package com.akai.pay;

public class TestPay {
    public static void main(String[] args) {
        new WeChat().pay();
        new Ali().pay();
        /*
         * 正在使用微信支付
         * 正在使用支付宝支付
         * */
        // 定义一个字符串，来模拟前台的支付方式
        System.out.println("-------------");
        String payMethod = "微信";
        if ("微信".equals(payMethod)) {   // payMethod.equals("微信") 可能会抛空指针异常
            pay(new WeChat());
        }
        if ("支付宝".equals(payMethod)) {
            pay(new Ali());
        }
    }
//    public static void pay(WeChat wc) {
//        wc.pay();
//    }
//    public static void pay(Ali al) {
//        al.pay();
//    }
    public static void pay(Mtwm m) {
        m.pay();
    }
}
