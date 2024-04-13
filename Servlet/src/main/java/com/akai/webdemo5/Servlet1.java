package com.akai.webdemo5;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(urlPatterns = "/servlet1.do")
public class Servlet1 extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("servlet1 invoked");     // servlet1 invoked
        String money = req.getParameter("money");
        System.out.println(money);      // 100
        resp.sendRedirect("servlet2.do");
        /*
         * 响应重定向总结
         * 1重定向是服务器给浏览器重新指定请求方向 是一种浏览器行为 地址栏会发生变化
         * 2重定向时,请求对象和响应对象都会再次产生,请求中的参数是不会携带
         * 3重定向也可以帮助我们完成页面跳转
         * 4重定向不能帮助我们访问WEB-INF中的资源
         * 5重定向可以定向到外部资源
         *
         * */
    }
}
