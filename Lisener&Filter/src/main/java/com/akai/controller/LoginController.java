package com.akai.controller;

import com.akai.pojo.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(urlPatterns = "/login.do")
public class LoginController extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String username = req.getParameter("username");
        String pwd = req.getParameter("pwd");
        System.out.println(username);
        System.out.println(pwd);
        User user = new User(username, pwd);
        req.getSession().setAttribute("user", user);
        // 跳转到欢迎页
        resp.sendRedirect("welcome.jsp");
    }
}
