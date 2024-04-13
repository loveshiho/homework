package com.akai.controller;

import com.akai.pojo.PageBean;
import com.akai.service.StudentService;
import com.akai.service.impl.StudentServiceImpl;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(urlPatterns = "/showstudent.do")
public class ShowStudentController extends HttpServlet {
    private StudentService studentService = new StudentServiceImpl();

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 接收数据
        // 页码数 + 页大小
        int currentPage = Integer.parseInt(req.getParameter("currentPage"));
        int pageSize = Integer.parseInt(req.getParameter("pageSize"));
        // 调用 service层服务处理业务逻辑
        PageBean pageBean = studentService.findByPage(currentPage, pageSize);
        req.setAttribute("pageBean", pageBean);
    }
}
