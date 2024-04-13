package com.akai.dao;

import com.akai.pojo.Dept;

import java.util.List;

public interface DeptDao {
    List<Dept> findAll();

    void addDept(Dept dept);
}
