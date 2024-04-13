package com.akai.test02;

import com.akai.dao.EmpDao;
import com.akai.dao.impl.EmpDaoImpl;
import com.akai.pojo.Emp;

import java.util.Date;

public class testDAO {
    public static void main(String[] args) {
        Emp emp = new Emp(null, "cao", "java", 7839, new Date(), 30000., 10000., 30);
        EmpDao empDao = new EmpDaoImpl();
        int rows = empDao.addEmp(emp);
        System.out.println(rows);

    }
}
