package com.akai.test01;

import java.sql.Connection;

import java.sql.DriverManager;
import java.sql.Statement;

public class TestJDBC01 {
    public static void main(String[] args) throws Exception {
        // 给dept表增加一条数据
        // 1 通过反射加载驱动 driver
        Class.forName("com.mysql.cj.jdbc.Driver");
        // 2 获得连接 Connection
        /*
         * url：统一资源定位符 定位我们要连接的数据库的地址
         * user：用户名
         * password：密码
         * url
         *   1 协议         jdbc:mysql
         *   2 IP          127.0.0.1/localhost
         *   3 端口号       3306
         *   4 数据库名字   mydb
         *   5 参数
         *   协议://ip:端口/资源路径?参数名=参数值&参数名=参数值&....
         *   jdbc:mysql://127.0.0.1:3306/mydb
         * */
        String url = "jdbc:mysql://127.0.0.1:3306/db_01?useSSL=false&useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai";
        String user = "root";
        String password = "zt20040801.";
        Connection conn = DriverManager.getConnection(url, user, password);
        // 3 获得语句对象 statement
        Statement statement = conn.createStatement();
        // 4 执行sql语句，返回结果
        /*
         * insert delete update 操作都是调用statement.executeUpdate
         * executeUpdate返回一个int值，代表数据库多少行数据发生了变化
         * */
        String sql = "insert into dept values(60, '教学部', '北京')";
        int rows = statement.executeUpdate(sql);
        System.out.println("影响数据行数为：" + rows);
        // 5 释放资源
        /*
         * 注意顺序
         * 后获得的先关闭,先获得的后关闭
         * */
        statement.close();
        conn.close();
    }
}
