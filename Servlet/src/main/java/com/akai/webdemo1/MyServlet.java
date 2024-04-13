package com.akai.webdemo1;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;

public class MyServlet extends HttpServlet {
    /*
     * 可以接收浏览器的请求
     * 并作出运算和响应
     * service Servlet服务方法
     * */

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 动态生成数据
        int num = new Random().nextInt();
        String message = num % 2 == 0 ? "happy birthday" : "happy new year";
        // 对浏览器作出响应
        PrintWriter writer = resp.getWriter();  // 该打印流指向了浏览器
        writer.write(message);
    }
}
