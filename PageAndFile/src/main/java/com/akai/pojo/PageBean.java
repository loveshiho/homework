package com.akai.pojo;

import java.util.List;

public class PageBean {
    private List<Student> stuList;
    private Integer totalPage;
    private Integer currentPage;
    private Integer pageSize;
    private Integer totalSize;

    public PageBean(List<Student> stuList, Integer totalPage, Integer currentPage, Integer pageSize, Integer totalSize) {
        this.stuList = stuList;
        this.totalPage = totalPage;
        this.currentPage = currentPage;
        this.pageSize = pageSize;
        this.totalSize = totalSize;
    }

    public PageBean() {
    }

    @Override
    public String toString() {
        return "PageBean{" +
                "stuList=" + stuList +
                ", totalPage=" + totalPage +
                ", currentPage=" + currentPage +
                ", pageSize=" + pageSize +
                ", totalSize=" + totalSize +
                '}';
    }

    public List<Student> getStuList() {
        return stuList;
    }

    public void setStuList(List<Student> stuList) {
        this.stuList = stuList;
    }

    public Integer getTotalPage() {
        return totalPage;
    }

    public void setTotalPage(Integer totalPage) {
        this.totalPage = totalPage;
    }

    public Integer getCurrentPage() {
        return currentPage;
    }

    public void setCurrentPage(Integer currentPage) {
        this.currentPage = currentPage;
    }

    public Integer getSize() {
        return pageSize;
    }

    public void setSize(Integer pageSize) {
        this.pageSize = pageSize;
    }

    public Integer getTotalSize() {
        return totalSize;
    }

    public void setTotalSize(Integer totalSize) {
        this.totalSize = totalSize;
    }
}
