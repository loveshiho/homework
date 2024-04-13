package com.akai.webdemo6;

import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;

@WebServlet(urlPatterns = "/testSession")
public class testSession extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 获取HTTPSession
        HttpSession session = req.getSession();
        // 尝试从HTTPSession中获取数据
        String username = (String) session.getAttribute("username");
        String password = (String) session.getAttribute("password");
        String level = (String) session.getAttribute("level");
        System.out.println(username);
        System.out.println(password);
        System.out.println(level);
        // 获取Session对象的其他信息
        System.out.println("创建时间:" + session.getCreationTime());
        System.out.println("最后一次访问时间:" + session.getLastAccessedTime());
        System.out.println("最大不活动时间:" + session.getMaxInactiveInterval());
    }
}
