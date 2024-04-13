package com.akai.test01;

import com.akai.pojo.Emp;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class TestJDBC04 {
    private static String driver = "com.mysql.cj.jdbc.Driver";
    private static String url = "jdbc:mysql://127.0.0.1:3306/db_01?useSSL=false&useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai";
    private static String user = "root";
    private static String password = "zt20040801.";

    public static void main(String[] args) {
        List<Emp> empList = search();
        empList.forEach(System.out::println);
    }

    private static List<Emp> search() {
        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;
        List<Emp> empList = new ArrayList<>();
        try {
            Class.forName(driver);
            connection = DriverManager.getConnection(url, user, password);
            statement = connection.createStatement();
            String sql = "select * from db_01.emp;";
            resultSet = statement.executeQuery(sql);
            while (resultSet.next()) {
                int empno = resultSet.getInt("empno");
                String ename = resultSet.getString("ename");
                String job = resultSet.getString("job");
                int mgr = resultSet.getInt("mgr");
                Date hiredate = resultSet.getDate("hiredate");
                double sal = resultSet.getDouble("sal");
                double comm = resultSet.getDouble("comm");
                int deptno = resultSet.getInt("deptno");
                empList.add(new Emp(empno, ename, job, mgr, hiredate, sal, comm, deptno));
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (null != resultSet) {
                try {
                    resultSet.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
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
        return empList;
    }
}
