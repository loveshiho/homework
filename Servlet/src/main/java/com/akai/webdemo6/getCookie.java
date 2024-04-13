package com.akai.webdemo6;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(urlPatterns = "/getCookie.do")
public class getCookie extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 读取请求中的Cookie
        Cookie[] cookies = req.getCookies();
        if (cookies == null) return;
        for (Cookie cookie : cookies) {
            System.out.println(cookie.getName() + ":" + cookie.getValue());
        }
    }
    /*
    * JSESSIONID:4D197906FB5DB1FF146BCF64A9BB72BC
    * age:10
    * height:175
    * */
}
