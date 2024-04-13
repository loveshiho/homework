package com.akai.listener;

import jakarta.servlet.ServletRequestEvent;
import jakarta.servlet.ServletRequestListener;
import jakarta.servlet.annotation.WebListener;
import jakarta.servlet.http.HttpServletRequest;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.Date;

@WebListener
public class RequestLogListener implements ServletRequestListener {
    private SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

    @Override
    public void requestDestroyed(ServletRequestEvent sre) {

    }

    @Override
    public void requestInitialized(ServletRequestEvent sre) {
        // 获得请求发出的 ip
        // 获得请求的 url
        // 获得请求的时间
        HttpServletRequest servletRequest = (HttpServletRequest) sre.getServletRequest();
        String remoteHost = servletRequest.getRemoteHost();
        String requestUrl = servletRequest.getRequestURL().toString();
        String requestDate = simpleDateFormat.format(new Date());
        try {
            String userHome = System.getProperty("user.home");
            System.out.println(userHome);   // /Users/zhong
            PrintWriter pw = new PrintWriter(new FileOutputStream(new File(userHome + "/Desktop/akai.txt"), true));
            pw.println(remoteHost + " " + requestUrl + " " + requestDate);
            pw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
