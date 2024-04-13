package com.akai.webdemo3;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

public class MyServlet extends HttpServlet {
    public MyServlet() {    // 构造
        System.out.println("constructor invoked");
    }

    @Override
    public void init() throws ServletException {    // 初始化
        System.out.println("init invoked");
    }

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException { // 服务
        System.out.println("service invoked");
    }

    @Override
    public void destroy() {     // 销毁
        System.out.println("destroy invoked");
    }
}
