package com.akai.dao.impl;

import com.akai.dao.StudentDao;
import com.akai.pojo.Student;

import java.util.ArrayList;
import java.util.List;

public class StudentDaoImpl implements StudentDao {
    @Override
    public List<Student> findByPage(int currentPage, int pageSize) {
        return new ArrayList<>();
    }

    @Override
    public int findTotalSize() {
        return 0;
    }
}
