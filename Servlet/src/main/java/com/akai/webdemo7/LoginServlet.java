package com.akai.webdemo7;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
@WebServlet(urlPatterns = "/loginServlet.do")
public class LoginServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 获取用户名和密码
        String username = req.getParameter("username");
        String password = req.getParameter("password");
        // 登录成功跳转到 main.html
        if (username.equals("akai") && password.equals("zt")) {
            // 将用户信息放在 HTTPSession中
            HttpSession session = req.getSession();
            session.setAttribute("username","akai");
            session.setAttribute("password","zt");
            resp.sendRedirect("MainServlet");
        } else {
            resp.sendRedirect("login.html");
        }
    }
}
