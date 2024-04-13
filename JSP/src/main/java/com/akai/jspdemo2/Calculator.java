package com.akai.jspdemo2;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class Calculator {
    public static void main(String[] args) throws Exception{
        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("JavaScript");
        String expression = "2 + 3 * 4"; // 表达式
        Object result = engine.eval(expression); // 执行表达式
        System.out.println("结果：" + result);
    }
}
