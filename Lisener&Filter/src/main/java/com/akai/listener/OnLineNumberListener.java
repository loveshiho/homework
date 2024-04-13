package com.akai.listener;

import jakarta.servlet.ServletContext;
import jakarta.servlet.annotation.WebListener;
import jakarta.servlet.http.HttpSession;
import jakarta.servlet.http.HttpSessionEvent;
import jakarta.servlet.http.HttpSessionListener;
@WebListener
public class OnLineNumberListener implements HttpSessionListener {
    @Override
    public void sessionCreated(HttpSessionEvent se) {
        // 向application域中 增加一个数字
        HttpSession session = se.getSession();
        ServletContext application = session.getServletContext();
        Integer count = (Integer) application.getAttribute("count");
        if (count == null) application.setAttribute("count", 1);
        else application.setAttribute("count", ++count);
    }

    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        // 向application域中 减少一个数字
        HttpSession session = se.getSession();
        ServletContext application = session.getServletContext();
        Integer count = (Integer) application.getAttribute("count");
        application.setAttribute("count", --count);
    }
}
