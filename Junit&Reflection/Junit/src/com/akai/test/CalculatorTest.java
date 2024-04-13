package com.akai.test;

import com.akai.calculator.Calculator;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class CalculatorTest {
    @Before
    public void init() {
        System.out.println("测试开始~");
    }
    @After
    public void close() {
        System.out.println("测试结束~");
    }
    // 测试 add方法
    @Test
    public void testAdd() {
//        System.out.println("测试add方法");
        Calculator cal = new Calculator();
        int addRes = cal.add(1, 2);
//        System.out.println(addRes);
        Assert.assertEquals(3, addRes);
    }
    // 测试 sub方法
    @Test
    public void testSub() {
//        System.out.println("测试sub方法");
        Calculator cal = new Calculator();
        int subRes = cal.sub(1, 2);
        Assert.assertEquals(-1, subRes);
    }
}
