package com.akai.filter;

import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
@WebFilter(urlPatterns = "/*")  // 任何资源都要进行过滤
public class Filter1_LoginFilter implements Filter {
    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        // 无论是否登录都要放行的资源
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;
        String requestURI = request.getRequestURI();
        // 登录页  登录校验Controller  和一些静态资源
        if (requestURI.contains("login.jsp") || requestURI.contains("login.do") || requestURI.contains("/static/")) {
            // 直接放行
            filterChain.doFilter(request, servletResponse);
            return;
        }
        // 需要登录后才能访问的资源，如果没登录，重定向到 login.jsp，提示用户进行登录
        HttpSession session = request.getSession();
        Object user = session.getAttribute("user");
        if (user != null) {
            filterChain.doFilter(request, servletResponse);
        } else {
            response.sendRedirect("login.jsp");
        }
    }

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        Filter.super.init(filterConfig);
    }

    @Override
    public void destroy() {
        Filter.super.destroy();
    }
}
