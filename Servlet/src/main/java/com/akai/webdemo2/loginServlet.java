package com.akai.webdemo2;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.Map;
import java.util.Set;

public class loginServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String email = req.getParameter("email");
        String pwd = req.getParameter("pwd");
        System.out.println(email);
        System.out.println(pwd);
        String res = email.equals("zhongkai429@gmail.com") && pwd.equals("zt20040801.") ? "Nice!" : "Fuck!";
        resp.getWriter().write(res);
    }


}
