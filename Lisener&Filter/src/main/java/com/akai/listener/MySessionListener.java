package com.akai.listener;

import jakarta.servlet.annotation.WebListener;
import jakarta.servlet.http.HttpSessionAttributeListener;
import jakarta.servlet.http.HttpSessionBindingEvent;
import jakarta.servlet.http.HttpSessionEvent;
import jakarta.servlet.http.HttpSessionListener;

@WebListener    // 通过注解声明
public class MySessionListener implements HttpSessionListener, HttpSessionAttributeListener {
    @Override
    public void sessionCreated(HttpSessionEvent se) {
        System.out.println("任何一个Session对象创建");
    }

    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        System.out.println("任何一个Session对象的销毁");
    }

    @Override
    public void attributeAdded(HttpSessionBindingEvent se) {
        System.out.println("任何一个Session对象中添加了数据");
    }

    @Override
    public void attributeRemoved(HttpSessionBindingEvent se) {
        System.out.println("任何一个Session对象中移除了数据");
    }

    @Override
    public void attributeReplaced(HttpSessionBindingEvent se) {
        System.out.println("任何一个Session对象中修改了数据");
    }
}
