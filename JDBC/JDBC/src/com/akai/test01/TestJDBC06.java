package com.akai.test01;

import java.sql.*;

public class TestJDBC06 {
    private static String driver = "com.mysql.cj.jdbc.Driver";
    private static String url = "jdbc:mysql://127.0.0.1:3306/db_01?useSSL=false&useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai&allowPublicKeyRetrieval=true&useServerPrepStmts=true&cachePrepStmts=true&&rewriteBatchedStatements=true";
    private static String user = "root";
    private static String password = "zt20040801.";

    public static void main(String[] args) {
        testAddBatch();
    }

    public static void testAddBatch() {
        Connection connection = null;
        PreparedStatement preparedStatement = null;
        try {
            Class.forName(driver);
            connection = DriverManager.getConnection(url, user, password);
            connection.setAutoCommit(false);
            String sql = "update account set money = money - ? where id = ?";
            preparedStatement = connection.prepareStatement(sql);// 这里已经传入SQL语句
            // 设置参数
            preparedStatement.setInt(1, 100);
            preparedStatement.setInt(2, 1);
            preparedStatement.executeUpdate();
            int i = 1 / 0;
            preparedStatement.setInt(1, -100);
            preparedStatement.setInt(2, 2);
            preparedStatement.executeUpdate();
        } catch (Exception e) {
            if(null != connection){
                try {
                    connection.rollback();// 回滚事务
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
            e.printStackTrace();
        } finally {
            if (null != connection) {
                try {
                    connection.commit();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (null != preparedStatement) {
                try {
                    preparedStatement.close();
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