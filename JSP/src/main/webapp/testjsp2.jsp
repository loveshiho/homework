<%@ page import="java.io.PrintWriter" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%--
    ctrl +shift + /
    JSP中通过<%%>来穿插JAVA代码
    <%=变量/值%>将变量/值打印到页面上的标签显示的位置
--%>
<%
    int score = (int) (Math.random() * 101);
%>
分数:
<%--
    <%
        //PrintWriter out = response.getWriter();
        out.print(score);
    %>
--%>
<%=score%>
<br/>
等级:
<%
    int grade = score / 10;
    switch (grade) {
        case 10:
        case 9:
%>
<%="A"%>
<%
        break;
    case 8:
%>
<%="B"%>
<%
        break;
    case 7:
%>
<%="C"%>
<%
        break;
    case 6:
%>
<%="D"%>
<%
        break;
    default:
%>
<%="E"%>
<%
    }
%>
</body>
</html>