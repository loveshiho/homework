package com.akai.webdemo6;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
@WebServlet(urlPatterns = "/Cookie.do")
public class testCookie extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 通过响应对象，给浏览器响应一些Cookie
        Cookie age = new Cookie("age", "10");
        Cookie height = new Cookie("height", "175");
        height.setMaxAge(60);   // 持久化Cookie，让浏览器保留60秒
        resp.addCookie(age);
        resp.addCookie(height);
    }
}
