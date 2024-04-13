package com.akai.webdemo6;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.text.CollationKey;

@WebServlet("/practiceCookie")
public class practiceCookie extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 如果是第一次访问当前 Servlet，向浏览器响应一个 Cookie
        // 如果是多次访问，就在次数上+1
        boolean flag = false;
        Cookie[] cookies = req.getCookies();
        if (cookies != null) {
            for (Cookie cookie : cookies) {
                if (cookie.getName().equals("practiceCookie")) {
                    Integer val = Integer.parseInt(cookie.getValue()) + 1;
                    Cookie practiceCookie = new Cookie("practiceCookie", String.valueOf(val));
                    resp.addCookie(practiceCookie);
                    System.out.println("欢迎您第 " + practiceCookie.getValue() + " 访问");
                    flag = true;
                }
            }
        }
        if (!flag) {
            System.out.println("欢迎您第 1次 访问");
            Cookie practiceCookie = new Cookie("practiceCookie", "1");
            resp.addCookie(practiceCookie);
        }
    }
}
