package com.akai.service;

import com.akai.pojo.PageBean;

public interface StudentService {

    PageBean findByPage(int currentPage, int pageSize);
}
