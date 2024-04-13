package com.akai.webdemo7;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@WebServlet(urlPatterns = "/MainServlet")
public class MainServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // HttpSession中如果有登录过的信息
        HttpSession session = req.getSession();
        Object username = session.getAttribute("username");
        Object password = session.getAttribute("password");
        if (username != null && password != null) {
            req.getRequestDispatcher("main.html").forward(req, resp);
        } else {
            req.getRequestDispatcher("login.html").forward(req, resp);
        }
        List<String> res = new ArrayList<>();
    }
}
