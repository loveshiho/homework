package com.akai.dao;

import com.akai.pojo.Emp;

import java.util.List;

public interface EmpDao {
    int addEmp(Emp emp);
    int deleteByEmpno(int Empno);

    List<Emp> findAll();

    int updateEmp(Emp emp);
}
