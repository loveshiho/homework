package com.akai.filter;
import jakarta.servlet.*;

import java.io.IOException;
// 处理所有controller中post提交乱码问题
public class Filter0_EncodingFilter implements Filter {
    private String charset;
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        charset = filterConfig.getInitParameter("charset");
    }
    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        servletRequest.setCharacterEncoding(charset);
        filterChain.doFilter(servletRequest, servletResponse);
    }
    @Override
    public void destroy() {

    }
}
