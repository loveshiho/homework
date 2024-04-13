## 基础篇2

### CSS_01

#### 1. CSS简介

##### 1）网页美容师

CSS是层叠样式表的简称，CSS主要用于设置HTML页面中的文本内容（字体、大小、对齐方式等）、图片的外形（宽高、边框样式、边距等）以及版面的布局和外观显示样式。

CSS可以美化HTML，让HTML更漂亮，让页面布局更简单。

##### 2）CSS语法规范

CSS规则由两个主要的部分构成：选择器以及一条或多条声明。

选择器 {样式} = 给谁改样式 {改什么样式}

- 选择器是用于指定CSS样式的HTML标签，花括号内是对该对象设置的具体样式
- 属性和属性值以 “键值对” 的形式出现
- 属性是对指定的对象设置的样式属性，例如字体大小、文本颜色等
- 属性和属性值之间用英文 “ : ” 分开
- 多个 “键值对” 之间用英文 ” ; “ 分开

#### 2. CSS基础选择器

选择器就是根据不同需求把不同的标签选出来，和就是选择器的作用。

选择器分为**基础选择器**和**复合选择器**两个大类。

- 基础选择器是由单个选择器组成的
- 基础选择器又包括：标签选择器、类选择器、id选择器和通配符选择器

##### 1） 标签选择器

**基本语法：** 使用标签名称作为选择器，直接在样式表中定义样式规则。

```css
p {
  color: blue;
}
```

在这个例子中，`p` 是段落元素 `<p>` 的标签选择器。这个规则会将所有 `<p>` 元素的文本颜色设置为蓝色。

优点：能快速为页面中同类型的标签统一设置样式。

缺点：不能设计差异化样式，只能选择全部的当前标签。

##### 2） 类选择器

类选择器以点号 `.` 开头，后面紧跟着类名。它允许你为页面上具有相同类的多个元素定义相同的样式。

以下是类选择器的基本语法：

```css
/* 根据类名选择元素 */
.className {
  /* 样式规则 */
}
```

```html
<!-- 具有单个类名的元素 -->
<div class="className">这是一个具有类名的元素</div>

<!-- 具有多个类名的元素 -->
<div class="class1 class2 class3">这是一个具有多个类名的元素</div>
```

类选择器的主要特点和使用方法包括：

1. **可复用性：** 类选择器允许你定义一组样式，并将其应用于页面上的多个元素，提高了样式的可复用性。
2. **命名约定：** 类名通常采用有意义的、描述性的名称，以反映元素的用途或内容，这有助于提高代码的可读性和维护性。
3. **多类名：** 一个元素可以拥有多个类名，每个类名用空格分隔。这个元素分别具有这些类名的样式。

##### 3） id选择器

ID 在文档中应该是**唯一的**，因此 ID 选择器通常用于选择唯一的一个元素。

```css
#myId {
  /* 样式规则 */
}
```

```html
<div id="myId">这是一个具有 ID 的元素</div>
```

通过 `#` 符号后跟 ID 名称，可以选择并定义具有该 ID 的元素的样式规则。

不得重复，好比人的身份证。

##### 4） 通配符选择器

用一个星号 `*` 表示，匹配文档中的所有元素，为所有元素定义相同的样式规则（设置默认样式）。

```css
* {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
}
```

#### 3. CSS字体属性

1. **`font-family`：** 指定文本的字体系列。可以设置一个或多个字体名称，浏览器会按照顺序依次尝试使用这些字体。如果用户计算机上没有第一个字体，则会尝试使用下一个字体。

   ```css
   body {
     font-family: "Arial", sans-serif;
     /* sans-serif 为浏览器默认字体*/
   }
   ```

2. **`font-size`：** 设置文本的字体大小。可以使用像素（`px`）、em、rem等单位。

   ```css
   p {
     font-size: 16px;
   }
   ```

​	注意：标题标签特殊，需要单独指定文字大小。

3. **`font-weight`：** 设置文本的字体粗细。常用值有 `normal`、`bold`、`bolder`、`lighter`，也可以使用数字值（例如 `400` 表示 `normal`，`700` 表示 `bold`）。

   ```css
   h1 {
     font-weight: bold;
   }
   ```

4. **`font-style`：** 设置文本的字体风格，如斜体。常用值有 `normal`、`italic`、`oblique`。

   ```css
   em {
     font-style: italic;
   }
   ```

**复合属性：**

**`font`：** 用于设置字体样式，包括 `font-style`、`font-weight`、`font-size` / `line-height`、`font-family`。

```css
p {
  font: italic bold 16px/1.5 "Arial", sans-serif;
}
```

不可更换顺序

必须保留 `font-size` 和 `font-family` 属性

#### 4. CSS文本属性

1. **`color`：** 设置文本的颜色。

   ```css
   p {
     color: #333;
   }
   ```

2. **`text-align`：** 设置文本的水平对齐方式。

   ```css
   div {
     text-align: center;
   }
   ```

3. **`text-decoration`：** 设置文本的装饰效果，如下划线（underline）、删除线（line-through）、无（none）等。

   ```css
   a {
     text-decoration: underline;
   }
   ```

4. **`text-indent`：** 设置文本的首行缩进。指定长度、百分比（相对于元素宽度的缩进）。

   ```css
   p {
     text-indent: 2em; /* 使用em单位进行缩进 */
   }
   ```

   `em`是一个相对单位，就是当前元素（ `font-size` ）1个文字的大小。

5. **`line-height`：** 设置文本行的高度。

   ```css
   p {
     line-height: 1.5;
   }
   ```

#### 5. CSS引入方式

##### 1）**内联样式**

**内联样式（Inline Styles）：** 在 HTML 元素中使用 `style` 属性直接定义样式。

```html
<p style="color: blue; font-size: 16px;">这是一段内联样式的文本。</p>
```

这种方式适用于仅对一个元素应用样式的情况。

##### 2）内部样式表

**内部样式表（Internal Style Sheet）：** 在 HTML 文档的 `<head>` 部分使用 `<style>` 标签定义样式。

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      background-color: #f0f0f0;
      font-family: Arial, sans-serif;
    }
    h1 {
      color: blue;
    }
  </style>
  <title>Internal Style Sheet</title>
</head>
<body>
  <h1>Hello, World!</h1>
</body>
</html>
```

内部样式表适用于单个 HTML 文档，可以在 `<style>` 标签中定义整个文档的样式。

##### 3）外部样式表

**外部样式表（External Style Sheet）：** 将样式定义在一个独立的外部 CSS 文件中，并通过 `<link>` 标签引入到 HTML 文档中。

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles.css">
  <title>External Style Sheet</title>
</head>
<body>
  <h1>Hello, World!</h1>
</body>
</html>
```

```css
/* styles.css */
body {
  background-color: #f0f0f0;
  font-family: Arial, sans-serif;
}
h1 {
  color: blue;
}
```

案例：`<div>` 中样式，**不会传给**，表单标签、超链接标签，只传文本。

单给 `<img>` 加 `text-align` 没用，得给 `<img>` 父类（`<p>`）加。

