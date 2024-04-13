package com.akai.servlet;

import com.akai.pojo.User;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
@WebServlet(urlPatterns = "/setInfo.do")
public class LoginServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String username = req.getParameter("username");    // 是可以获取post提交的数据的
        String pwd = req.getParameter("pwd");
        User user = new User(username, pwd);
        req.getSession().setAttribute("user", user);
        resp.getWriter().println("setAttribute invoked!");
    }
}
