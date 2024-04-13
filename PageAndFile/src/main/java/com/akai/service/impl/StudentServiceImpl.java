package com.akai.service.impl;

import com.akai.dao.StudentDao;
import com.akai.dao.impl.StudentDaoImpl;
import com.akai.pojo.PageBean;
import com.akai.pojo.Student;
import com.akai.service.StudentService;

import java.util.List;

public class StudentServiceImpl implements StudentService {
    private StudentDao studentDao = new StudentDaoImpl();
    @Override
    public PageBean findByPage(int currentPage, int pageSize) {
        List<Student> stuList = studentDao.findByPage(currentPage, pageSize);
        int totalSize = studentDao.findTotalSize();
        int totalPage = totalSize % pageSize == 0 ? totalSize / pageSize : totalSize / pageSize + 1;
        return new PageBean(stuList, totalPage, currentPage, pageSize, totalSize);
    }
}
