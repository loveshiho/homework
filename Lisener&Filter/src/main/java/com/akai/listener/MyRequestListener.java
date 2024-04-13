package com.akai.listener;

import jakarta.servlet.*;

public class MyRequestListener implements ServletRequestListener, ServletRequestAttributeListener {
    @Override
    public void attributeAdded(ServletRequestAttributeEvent srae) {
        // 任何一个Request对象中调用 setAttribute方法增加了数据都会触发该方法
        ServletRequest servletRequest = srae.getServletRequest();
        String name = srae.getName();
        Object value = srae.getValue();
        System.out.println("request " + servletRequest.hashCode() + " 对象增加了数据: " + name + "=" + value);
    }

    @Override
    public void attributeRemoved(ServletRequestAttributeEvent srae) {
        ServletRequest servletRequest = srae.getServletRequest();
        String name = srae.getName();
        Object value = srae.getValue();
        System.out.println("request " + servletRequest.hashCode() + " 对象删除了数据: " + name + "=" + value);
        // 任何一个Request对象中调用 removeAttribute方法移除了数据都会触发该方法
    }

    @Override
    public void attributeReplaced(ServletRequestAttributeEvent srae) {
        ServletRequest servletRequest = srae.getServletRequest();
        String name = srae.getName();
        Object value = srae.getValue();
        Object newValue = servletRequest.getAttribute(name);
        System.out.println("request " + servletRequest.hashCode() + " 对象增修改了数据: " + name + "=" + value + "设置为:" + newValue);
        // 任何一个Request对象中调用 setAttribute方法修改了数据都会触发该方法
    }

    @Override
    public void requestDestroyed(ServletRequestEvent sre) {
        // 监听HttpServletRequest对象的销毁，项目中任何一个Request对象的销毁都会触发该方法的执行
        ServletRequest servletRequest = sre.getServletRequest();
        System.out.println("requestDestroyed invoked " + servletRequest.hashCode());
    }

    @Override
    public void requestInitialized(ServletRequestEvent sre) {
        // 监听HttpServletRequest对象的创建并初始化，项目中任何一个Request对象的创建并初始化都会触发该方法的执行
        ServletRequest servletRequest = sre.getServletRequest();
        System.out.println("requestInitialized invoked " + servletRequest.hashCode());
    }
}
