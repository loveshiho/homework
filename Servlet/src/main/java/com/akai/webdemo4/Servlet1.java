package com.akai.webdemo4;

import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Servlet1 extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 1 获取 Servlet对象
        // 1 通过 req对象获取
        ServletContext servletContext_1 = req.getServletContext();
        // 1 通过继承的方法
        ServletContext servletContext_2 = this.getServletContext();
        System.out.println(servletContext_1 == servletContext_2);   // true

        // 2 获取当前项目的部署名
        String contextPath = servletContext_1.getContextPath();
        System.out.println(contextPath);      // /webdemo
        // 3 将一个相对路径转化为项目的绝对路径
        String fileUpload = servletContext_1.getRealPath("fileUpload");
        System.out.println(fileUpload); // /Users/zhong/Desktop/Java/webdemo/target/webdemo-1.0-SNAPSHOT/fileUpload
        // 4
        String serverInfo = servletContext_1.getServerInfo();
        System.out.println("servletInfo:" + serverInfo);    // servletInfo:Apache Tomcat/10.1.18
        // 5
        int majorVersion = servletContext_1.getMajorVersion();
        int minorVersion = servletContext_1.getMinorVersion();
        System.out.println(majorVersion + ":" + minorVersion);  // 6:0

        // 6 获取web.xml中配置的全局的初始信息
        String username = servletContext_1.getInitParameter("username");
        String password = servletContext_1.getInitParameter("pwd");
        System.out.println(username + ":" + password);  // akai:zt20040801

        // 7 向ServletContext对象中增加数据 域对象
        List<String> data = new ArrayList<>();
        Collections.addAll(data, "张三", "李四", "王五");
        servletContext_1.setAttribute("list", data);
        servletContext_1.setAttribute("gender", "boy");
    }
}