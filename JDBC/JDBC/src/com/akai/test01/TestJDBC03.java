package com.akai.test01;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class TestJDBC03 {
    private static String driver = "com.mysql.cj.jdbc.Driver";
    private static String url = "jdbc:mysql://127.0.0.1:3306/db_01?useSSL=false&useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai";
    private static String user = "root";
    private static String password = "zt20040801.";

    public static void main(String[] args) {
        update();
    }

    private static void update() {
        Connection connection = null;
        Statement statement = null;
        try {
            Class.forName(driver);
            connection = DriverManager.getConnection(url, user, password);
            statement = connection.createStatement();
            String sql = "update db_01.dept set DNAME = '总部',LOC = '北京' where DEPTNO = 30;";
            int rows = statement.executeUpdate(sql);
            System.out.println("影响数据行数为:" + rows);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (null != statement) {
                try {
                    statement.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (null != connection) {
                try {
                    connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void delete() {
        Connection connection = null;
        Statement statement = null;
        try {
            Class.forName(driver);
            connection = DriverManager.getConnection(url, user, password);
            statement = connection.createStatement();
            String sql = "delete from db_01.dept where deptno = 40;";
            int rows = statement.executeUpdate(sql);
            System.out.println("影响数据行数为:" + rows);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (null != statement) {
                try {
                    statement.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (null != connection) {
                try {
                    connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
