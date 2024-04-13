<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<form action="setInfo.do" method="post">
    用户名：<input type="text" name="username"><br>
    密码：<input type="password" name="pwd"><br>
    <input type="submit" value="提交">
</form>
<%
    System.out.println("jsp invoked " + request.hashCode());
%>
当前在线人数为:${applicationScope.count}
</body>
</html>
