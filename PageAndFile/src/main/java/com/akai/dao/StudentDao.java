package com.akai.dao;

import com.akai.pojo.Student;

import java.util.List;

public interface StudentDao {
    List<Student> findByPage(int currentPage, int pageSize);

    int findTotalSize();
}
