package com.akai.webdemo4;

import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.List;

public class Servlet2 extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        ServletContext servletContext = this.getServletContext();
        // 1 获取web.xml中配置的全局的初始信息
//        String username = servletContext.getInitParameter("username");
//        String password = servletContext .getInitParameter("pwd");
//        System.out.println(username + ":" + password);  // akai:zt20040801
        // 2 当你不知道 param-name标签中的值
        // 2 获取web.xml中配置的全局的初始信息
        Enumeration<String> pnames = servletContext.getInitParameterNames();
        while (pnames.hasMoreElements()) {
            String e = pnames.nextElement();
            System.out.println(e + ":" + servletContext.getInitParameter(e));
//            pwd:zt20040801
//            username:akai
        }
        // 3 从ServletContext对象中获取数据
        List<String> list = (List<String>) servletContext.getAttribute("list");
        System.out.println(Arrays.toString(list.toArray()));    // [张三, 李四, 王五]
        String gender = (String) servletContext.getAttribute("gender");
        System.out.println(gender);     // boy
    }
}
