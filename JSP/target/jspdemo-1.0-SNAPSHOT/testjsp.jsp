<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
    <style>
        table {
            border: 1px solid green;
            width: 50%;
            margin: 0px auto;
        }

        table td {
            border: 1px solid blue;
        }
    </style>
</head>
<body>
<%
    int h = Integer.parseInt(request.getParameter("h"));
    int l = Integer.parseInt(request.getParameter("l"));
    StringBuilder sbd = new StringBuilder();
    sbd.append("<table>");
    for (int i = 1; i <= h; i++) {
        sbd.append("<tr>");
        for (int j = 1; j <= l; j++) {
            sbd.append("<td>");
            sbd.append(String.valueOf(i));
            sbd.append(String.valueOf(j));
            sbd.append("</td>");
        }
        sbd.append("</tr>");
    }
    sbd.append("</table>");
    out.print(sbd.toString());
%>
</body>
</html>
