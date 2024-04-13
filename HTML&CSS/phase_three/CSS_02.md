# 基础篇3

## CSS_02

### 1. Emmet语法

#### 1）快速生成HTML结构语法

1. `div*3` 可以快速生成 `3` 个 `div`

2. 有父子级关系的标签，可以用 `>` ，比如 `ul > li`
3. 兄弟关系的标签，可以用 `+` ，比如 `div + p`
4. 带有类名或者 `id` 名字的，直接写 `.demo` 或者 `#two` ，按 `table` 键就可，默认生成 `div` ，生成 `p` ，`p.demo`
5. 在生成的标签内部写内容可以用 `{}` 表示
6. `$` 自增符号

#### 2）快速生成css样式

采取简写形式，比如 `w200` ，可以生成，`width: 200px;` ，比如 `lh26` ，可以生成，`line-height: 26px;` 。

### 2. 复合选择器

#### 1）后代选择器

可以选择父元素里面子元素，其写法就是把外层标签写在前面，内层标签写在后面，中间用空格分割。

例如：

```css
div p {
  color: blue;
}
```

这个规则选择了所有在 `<div>` 元素内的 `<p>` 元素，并将它们的文本颜色设置为蓝色。

解释步骤如下：

1. 选择所有 `<div>` 元素。
2. 在这些选中的 `<div>` 元素中，再选择所有 `<p>` 元素。

后代选择器选择指定元素的后代元素，无论后代元素在多深的嵌套层次中。

#### 2）子选择器

子元素选择器只选择指定元素的直接子元素。

```css
ul > li {
  list-style-type: square;
}
```

上述规则选择了所有 `<ul>` 下的直接子元素 `<li>`。

#### 3）并集选择器

并集选择器（Union Selector）允许选择多个选择器所匹配的所有元素，然后为它们一起应用相同的样式。并集选择器使用逗号分隔不同的选择器，将它们组合在一起。

语法结构如下：

```css
selector1, selector2, selector3 {
  /* styles */
}
/* 这表示所有匹配 selector1、selector2 或 selector3 的元素都会应用相同的样式 */
```

```css
h1, h2, h3 {
  color: red;
}
```

这个规则选择了所有 `<h1>`、`<h2>` 和 `<h3>` 元素，并将它们的文本颜色设置为红色。

解释步骤如下：

1. 选择所有 `<h1>` 元素。
2. 选择所有 `<h2>` 元素。
3. 选择所有 `<h3>` 元素。

然后，为上述选择的所有元素应用相同的样式，即将文本颜色设置为红色。

再如：

```css
div,
p,
.pig li {
		color: red;
}
```

#### 4）伪类选择器

允许选择处于特定状态的元素，或者选择某个元素的特定部分。伪类选择器以冒号 `:` 开头，用于向某些元素应用特殊的样式。

##### 2.4.1 链接伪类

**链接伪类（Link Pseudo-classes）：**

- `:link`：选择未被访问的链接。
- `:visited`：选择已被访问的链接。
- `:hover`：选择鼠标悬停的链接。
- `:active`：选择被激活的链接，通常是在用户点击时。

注意事项：

1. 为了确保生效，要按照顺序声明
2. `a` 链接在浏览器中具有默认样式，实际开发中需要给链接单独指定样式

```css
/* a 是标签选择器 所有链接 */
a {
	color: gray;
}
/* :hover 是链接伪类选择器 鼠标经过 */
a:hover {
	color: blue;
}
```

##### 2.4.2 表单伪类

**表单伪类（Form Pseudo-classes）：**

- `:checked`：选择被选中的表单元素，如复选框或单选按钮。
- `:focus`：选择当前获取焦点的表单元素。

```css
input:checked {
  border: 2px solid green;
}

input:focus {
  background-color: #e0e0e0;
}
```

### 3. 元素显示模式

元素显示模式就是元素（标签）以什么方式进行显示，比如 `<div>` 自己占一行，一行可以放多个 `<span>`。

HTML元素一般分为**块元素**和**行内元素**两种类型。

#### 1）块元素

一些常见的块元素包括 `<div>`、`<p>`、`<h1>` 到 `<h6>`、`<ul>`、`<ol>`、`<li>`、`<table>` 等。

块元素特点：

1. **独占一行：** 块元素会在页面上独占一行，从而使其后续元素出现在新的一行上。这使得块元素在页面布局中常用于分隔和组织内容。
2. **宽度默认为父元素宽度：** 块元素的宽度默认会占满其父元素的宽度，除非显式地设置了宽度属性。
3. **高度由内容和内边距决定：** 块元素的高度通常由其内容的高度以及内边距（padding）、边框（border）、外边距（margin）等属性的设置来决定。
4. **可包含内联元素和其他块元素：** 块元素可以包含其他块元素和内联元素。这种嵌套关系允许你以层次结构的方式组织和布局页面内容。
5. **默认情况下自动换行：** 块元素在默认情况下会自动换行，即在页面上垂直排列。内联元素则会在同一行上水平排列。

文字类的元素内不能使用块元素。

#### 2）行内元素

相对于块元素，行内元素不会在页面上独占一行，而是在同一行上水平排列。不会强制换行，而是尽可能占据所需的宽度。

以下是行内元素的一些特点：

1. **不会独占一行：** 行内元素在页面上不会独占一行，而是尽可能在同一行上显示，直到达到宽度的极限。
2. **宽度由内容决定：** 行内元素的宽度通常由其包含的内容决定，而不会占满整个父元素的宽度。
3. **不会强制换行：** 行内元素不会强制换行，只有在容器宽度不足以容纳内容时才会进行换行。
4. **可包含其他行内元素：** 行内元素可以包含其他行内元素，但通常不能包含块元素。
5. **高度由字体和行高决定：** 行内元素的高度通常由其包含的文本字体和行高（line height）的设置来决定。
6. **不支持宽度和高度设置：** 在一般情况下，行内元素不支持显式设置宽度和高度，它们的尺寸通常由内容决定。

一些常见的行内元素包括 `<span>`、`<a>`、`<strong>`、`<em>`、`<img>`、`<br>` 等。这些元素通常用于在文本中添加样式、链接、强调等，或者用于插入行内图片。

只能容纳文本或其他行内元素。

注意：

- 链接里面不能再放链接
- 特殊情况链接里面可以放块级元素

#### 3）行内块元素

在行内元素中有几个特殊的标签—`<img>`、`<input>`、`<td>` ，它们同时具有块元素和行内元素的特点。

以下是行内块元素的一些特点：

1. **水平排列：** 行内块元素在同一行上水平排列，类似于行内元素，不会强制换行。
2. **块元素特性：** 行内块元素具有块元素的盒模型，可以设置宽度、高度、内边距、外边距等属性，这使得其在布局上更加灵活。
3. 盒子宽度和元素宽度一致。

#### 4）元素显示模式的转换

特殊情况下，我们需要元素模式的转换，理解：一个模式的元素需要另外一种模式的特性。

比如想要增加链接 `<a>` 的触发范围。

**1. 转换为块级元素（Block-level Element）：**

要将行内元素转换为块级元素，可以将其 `display` 属性设置为 `block`。

```css
span {
  display: block;
}
```

上述 CSS 规则将所有 `<span>` 元素的 `display` 属性设置为 `block`，使其变成块级元素。

**2. 转换为行内块元素（Inline-Block Element）：**

要将行内元素转换为行内块元素，可以将其 `display` 属性设置为 `inline-block`。

```css
span {
  display: inline-block;
}
```

上述 CSS 规则将所有 `<span>` 元素的 `display` 属性设置为 `inline-block`，使其变成行内块元素。

单行文字垂直居中的原理：设置行高，且与盒子高度相等。

### 4. CSS的背景

CSS 背景属性用于控制和设置 HTML 元素的背景样式。

#### 1）背景属性

以下是一些常见的 CSS 背景属性：

**1. `background-color`：**

用于设置元素的背景颜色，默认透明（`transparent`），图层位于最底层。

```css
div {
  background-color: #f0f0f0;
}
```

**2. `background-image`：**

用于设置元素的背景图片。

```css
div {
  background-image: url('background.jpg');
}
```

优点是非常便于控制位置。

**3. `background-repeat`：**

用于设置背景图片是否重复及重复的方式。

```css
div {
  background-repeat: repeat-x; /* 水平重复 */
  /* repeat-y 垂直重复 */
  /* no-repeat 不重复 */
  /* repeat 默认重复 */
}
```

**4. `background-position`：**

用于设置背景图片的起始位置。

```css
div {
  background-position: center top; /* 水平位置 垂直位置 */
}
```

精确单位（x坐标，y坐标）

只指定一个数值，那该数值一定是x坐标，另一个默认垂直居中。

**5. `background-attachment`：**

用于设置背景图片是否随页面滚动。

```css
div {
  background-attachment: fixed;
  /* 默认滚动（scroll） */
}
```

#### 2）背景复合写法

`background: 背景颜色 背景图片地址 背景重复 背景图像滚动 背景图片位置`

`background: transparent url(image.jpg) repeat-y fixed top`

#### 3）背景色半透明

使用 `rgba` 表示颜色：

```css
div {
  background-color: rgba(255, 0, 0, 0.5); /* 红色，透明度为0.5 */
}
```

上述 CSS 规则将 `<div>` 元素的背景色设置为红色，透明度为 0.5，即半透明。

### 5）案例总结

#### 1）案例一

```css
<style>
    .nav ul a{
        color: red;
    }
    /* .nav 已经在 div 这一层了 切勿 div .nav */
    .hot>a{
        color: red;
    }
    /* .hot = div 切勿 div .hot>a */ 
</style>
```

```html
<body>
    <div class="nav">
        <ul>
            <li><a href="#">百度</a></li>
            <li><a href="#">百度</a></li>
        </ul>
    </div>
    <div class="hot">
        <a href="#">大肘子</a>
        <ul>
            <li><a href="#">猪头</a></li>
            <li><a href="#">猪尾巴</a></li>
        </ul>
    </div>
</body>
```

#### 2）案例三

```css
<style>
    div {
        background-color: gray;
        width: 230px;
    }
    a {
        width: 230px;
        height: 40px;
        font-size: 14px;
        color: white;
        text-decoration: none;
        display: block;
        text-indent: 2em;
        line-height: 40px;
    }

    a:hover {
        background-color: #ff6700;
    }
    /* color background-color 不同 字体色 背景色 */
</style>
```

#### 3）案例五

```css
.nav .bg1:hover {
        background: url(bg2.png) no-repeat;
    }
    /* .bg1 = a 切勿出现 .nav .blg:hover */
```

```html
<div class="nav">
    <a href="#" class="bg1">五彩导航</a>
    <a href="#" class="bg2">五彩导航</a>
    <a href="#" class="bg3">五彩导航</a>
    <a href="#" class="bg4">五彩导航</a>
</div>
```

