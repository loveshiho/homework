# 基础篇5

## CSS_04

### 1. 浮动

#### 1.1 传统网页布局的三种方式

CSS提供了三种传统布局方式（简单说，就是盒子如何进行排列）：

- 普通流（标准流）
- 浮动
- 定位

所谓的标准流，就是标签按照规定好的默认方式排列。

1. 块级元素会独占一行，从上向下顺序排列。
2. 行内元素会按照顺序，从左到右顺序排列，碰到父元素边缘则自动换行。

这三种布局方式都是用来摆放盒子的，盒子摆放到合适位置，布局自然就完成了。

#### 1.2 为什么需要浮动

有很多的布局效果，标准流没有办法完成，此时可以利用浮动完成布局，浮动可以改变元素标签默认的排列方式。

浮动最典型应用：可以让多个块级元素一行内排列显示。

网页布局第一准则：多个块级元素纵向排列找标准流，多个块级元素横向排列找浮动。

#### 1.3 什么是浮动

浮动是一种布局技术，允许元素在其容器中沿着页面的左侧或右侧移动（`left / right`），直到遇到容器的边缘或另一个浮动元素。浮动通常用于实现文本环绕图片、多列布局等效果。

使用 `float` 属性可以将元素浮动。该属性接受以下值：

- `left`：元素向左浮动。
- `right`：元素向右浮动。
- `none`（默认值）：元素不浮动。

示例：

```css
img {
  float: left; /* 图片向左浮动 */
}
```

#### 1.4 浮动特性（重难点）

1. 浮动元素会脱离标准流（脱标）

​	浮动的元素会**脱离正常的文档流**，不再占据其在文档中的位置。这意味着其他非浮动的元素会忽略浮动元素的存在，导致浮动元素之后的元素会填补原先的空白，或漂浮在普通流的上面，不占位置，脱标。

2. 浮动的元素会一行内显示并且元素顶部对齐（不管底部对齐）

​	浮动的元素互相贴靠在一起（不会有缝隙），如果父级宽度装不下这些浮动的盒子，多出的盒子会另起一行对齐。

3. 浮动的元素会具有行内块元素的特性

​	任何元素都可以浮动，不管原先是什么模式的元素，添加浮动之后具有**行内块元素相似**的特性。

> 行内块元素 给多宽 撑多宽

#### 1.5 标准流父级

为了约束浮动元素位置，网页布局一般采取的策略是：

先用标准流的父元素排列上下位置，之后内部子元素采取浮动排列左右位置，符合网页布局第一准则。

> 网页布局第二准则 先设置盒子大小 之后设置盒子的位置

#### 1.6 浮动的两个注意点

**1. 浮动和标准流的父盒子搭配**

先用标准流的父元素排列上下位置，之后内部子元素采取浮动排列左右位置。

**2. 一个元素浮动了，理论上其余的兄弟元素也要浮动**

一个盒子里面有多个子盒子，如果其中一个盒子浮动了，那么其他子盒子也应该浮动。

浮动的盒子只会影响浮动盒子后面的标准流，不会影响前面的标准流。

#### 1.7 清除浮动

> 思考 所有的父盒子都必须有高度吗

案例一：产品可能很多

案例二：新闻不知字数

理想中的状态，让子盒子撑开父盒子，子盒子多高，父盒子就有多高。（让父盒子被浮动的子盒子撑开，使得父盒子的高度更加灵活）

**1. 为什么需要清除浮动**

由于父级盒子很多情况下，不方便给高度，但是子盒子浮动又不占有位置，最后父级盒子高度为 `0` 时，就会影响下面的标准流盒子。

- 由于浮动元素不再占用原文档流的位置，所以它会对后面的元素排版产生影响

**2. 清除浮动本质**

- 清除浮动的本质是清除浮动元素造成的影响
- 如果父盒子本身有高度，则不需要清除浮动
- 清除浮动之后，父级就会根据浮动的子盒子自动检测高度。父级有了高度，就不会影响下面的标准流了

清除浮动是为了解决浮动元素可能引起的父容器高度塌陷的问题。

1. 使用空的块级元素清除浮动：

在浮动元素后面插入一个空的块级元素，然后通过设置这个**块级元素**的 `clear` 属性来清除浮动。

示例：

```html
<div class="float-left">浮动元素</div>
<div class="clearfix"></div>
```

```css
.clearfix {
  clear: both;
}
```

上述示例中，`clearfix` 类是一个空的块级元素，通过设置其 `clear` 属性为 `both`，清除了前面浮动元素的影响。

2. 使用 `overflow` 属性清除浮动：

- 使用 `overflow: hidden;` 清除浮动：

```css
.container {
  overflow: hidden;
}
```

在这个例子中，`.container` 是包含浮动元素的容器，通过设置 `overflow: hidden;`，使得容器能够正确地包含浮动元素。

- 使用 `overflow: auto;` 清除浮动：

```css
.container {
  overflow: auto;
}
```

同样地，设置 `overflow: auto;` ，也可以达到清除浮动的效果。这个方法的优势是当内容超过容器时，会自动显示滚动条，保持内容的可访问性。

当容器内的内容超过容器的尺寸时，这个属性可以触发滚动条，允许用户滚动查看剩余的内容。以下是一个简单的例子：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .container {
      width: 200px;
      height: 100px;
      overflow: auto;
      border: 1px solid #ccc;
    }
  </style>
</head>
<body>

  <div class="container">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vel urna sed ex varius tincidunt. Nullam ac tincidunt lectus, eget euismod ligula. Suspendisse potenti.</p>
  </div>

</body>
</html>
```

优势：

1. **防止内容溢出：** `overflow: auto;` 可以防止内容溢出容器，保持页面整洁，确保所有内容都可以被访问。
2. **滚动条仅在需要时出现：** 使用 `auto` 值的优势是滚动条仅在内容溢出时才会显示，否则它会自动隐藏，不会占据页面的额外空间。这提供了一种在需要时提供滚动的方式，而不会一直显示滚动条。
3. **适应不同屏幕尺寸：** 在响应式设计中，`overflow: auto;` 可以帮助处理不同屏幕尺寸下的内容溢出问题，确保在较小的屏幕上用户能够滚动查看全部内容。

------

3. 使用伪元素清除浮动（复制粘贴即可）

```css
.clearfix::after {
    content: "";
    display: block;
    height: 0;
    clear: both;
    visibility: hidden;
}

.clearfix {
    /* IE6、7 专有 */
    *zoom: 1;
}
```

```html
<div class="box clearfix">
```

4. 使用双伪元素清除浮动（复制粘贴即可）

```css
.clearfix::before,
.clearfix::after {
    content: "";
    display: table;
}

.clearfix::after {
    clear: both;
}

.clearfix {
    *zoom: 1;
}
```

```html
<div class="box clearfix">
```

### 2. 规范

#### 2.1 CSS属性书写顺序

遵循以下顺序：

1. 布局定位属性
2. 自身属性（盒子）
3. 文本属性
4. 其他属性

#### 2.2 页面布局整体思路

有以下思路：

1. 必须确定页面的版心（可视区）。
2. 分析页面中的行模块，以及每个行模块中的列模块。
3. 一行中的列模块经常浮动布局，先确定每个列的大小，之后确定列的位置。
4. 制作HTML结构，先有结构，后有样式。

### 3. 案例制作

#### 3.1 导航栏制作

实际开发中，我们不会直接用链接 `a` 而是用 `li` 包含链接，（ `li + a` ）的做法，`a` 一般需搭配其它元素。

导航栏里面文字不一样多，所以最好给链接 `a` 左右 `padding` 撑开盒子，而不是指定宽度。 

行内块元素，之间会有缝隙。

浮动的盒子不会有外边距合并的问题。

### 4. 定位

 #### 4.1 为什么需要定位

定位是可以让盒子自由的在某个盒子内移动位置或者固定在屏幕中某个位置，并且可以压住其他盒子。

定位（positioning）是一种控制元素在页面中布局的方式。通过使用不同的定位属性，你可以将元素放置在页面上的特定位置。

定位 = 定位模式 + 边偏移。

#### 4.2 定位属性

以下是一些常用的定位属性：

**`static`：**

- 这是元素的默认定位方式，元素按照它们在文档中的正常流进行布局。即元素出现在页面上的位置与它们在HTML文档中的顺序一致。

```css
div {
  position: static;
}
```

**`relative`：**

- 相对定位是**相对于元素在正常文档流中的位置**进行定位。使用`top`、`right`、`bottom`和`left`属性来指定相对于其正常位置的偏移量。
- 原来在标准流的位置继续占有，不脱标，继续保留原来位置。
- 最典型的应用，给绝对定位当爹（子绝父相）。

```css
div {
  position: relative;
  top: 10px;
  left: 20px;
}
```

**`absolute`：**

- 绝对定位是相对于**最近的已定位祖先元素**进行定位，如果没有**已定位的祖先元素**，则相对于最初的包含块（通常是 `<html>` 元素）进行定位。
- 如果没有祖先元素或者祖先元素没有定位，则以浏览器为准定位（Document文档）。
- 绝对定位不再占有原先的位置（脱标）。
- 加了绝对定位的盒子不能通过 `margin: 0 auto` 水平居中。

```css
div {
  position: absolute;
  top: 50px;
  left: 100px;
}
```

**`fixed`：**

- 固定定位是相对于**浏览器窗口**进行定位的。元素的位置在页面滚动时不会改变。
- 跟父元素没有任何关系。
- 规定定位不再占有原先的位置。

**小算法：**

1. 让固定定位的盒子 `left：50%` ，走到浏览器可视区的一半位置。
2. 让固定定位的盒子 `margin-left` 版心宽度的一半距离。

```css
div {
  position: fixed;
  top: 10px;
  right: 10px;
}
```

**`sticky`：**

- 粘性定位是相对定位和固定定位的混合。元素在跨越特定阈值前为相对定位，之后为固定定位。
- 粘性定位占有原先的位置。

```css
div {
  position: sticky;
  top: 10px;
}
```

子绝父相：

绝对定位和相对定位的使用场景。

子级是绝对定位的话，父级要用相对定位。

- 子级绝对定位，不会占有位置，可以放到父盒子里面的任何一个地方，不会影响其他兄弟盒子。
- 父盒子需要加定位限制子盒子在父盒子内显示。
- 父盒子布局时，需要占有位置，因此父亲只能是相对定位。

相对定位经常用来作为绝对定位的父级。

#### 4.3 z-index属性

- `z-index`是一个CSS属性，用于控制元素的叠放次序。具有较高`z-index`值的元素会显示在具有较低`z-index`值的元素之上。如果两个元素的`z-index`相同，那么它们将按照它们在HTML文档中的顺序叠放。

```css
div {
  position: absolute;
  z-index: 2;
}

span {
  position: absolute;
  z-index: 1;
}
```

在上面的例子中，`div`元素将显示在`span`元素的上方，因为它的`z-index`值更高。

**HTML文档中的顺序：**

- 如果两个元素的定位属性和`z-index`值相同，它们将按照它们在HTML文档中的顺序叠放，后出现的元素会显示在前面出现的元素之上

#### 4.4 定位特殊特性

1. 行内元素添加绝对或者固定定位，可以直接设置高度和宽度。
2. 块级元素添加绝对或者固定定位，如果不给宽度或者高度，默认大小是内容的大小。
3. 绝对定位（固定定位）会压住下面标准流所有内容。
4. 浮动的元素不会压住下面标准流的文字。

### 5. 其他

#### 5.1 网页布局总结

一个完整的网页，是**标准流、浮动、定位**一起完成布局的，每个都有自己的专门用法。

1. **标准流**

可以让盒子上下排列或者左右排列，垂直的块级盒子显示就用标准流布局。

2. **浮动**

可以让多个块级元素一行显示或者左右对齐盒子，多个块级盒子水平显示就用浮动布局。

3. **定位**

定位最大的特点是有层叠的概念，就是可以让多个盒子前后叠压来显示。如果元素自由在某个盒子内移动就用定位布局。

#### 5.2 元素的显示与隐藏

本质：让一个元素在页面中隐藏或者显示出来。

在CSS中，可以使用`display`属性来控制元素的显示与隐藏。

**`1. display: none;`：**

- 这个值会使元素在页面上完全隐藏，且不占据任何空间（不再占有原来的位置）。即使元素被隐藏，它的文档流位置仍然存在，但是对用户来说，看不到也无法与它交互。

```css
.hidden-element {
  display: none;
}
```

**`2. display: block;`：**

- 这是最常见的`display`属性值之一，它使元素显示为块级元素。块级元素会在新行上开始，并占据其父容器的整个宽度。

```css
.block-element {
  display: block;
}
```

**`3. visibility: hidden;`：**

- 使用`visibility`属性可以隐藏元素，但它仍然占据页面上的空间。与`display: none;`不同，元素的文档流位置仍然存在。

```css
.hidden-visibility {
  visibility: hidden;
}
```

如果要完全隐藏元素并使其不占据空间，使用`display: none;`。

如果要隐藏元素但保留其占用的空间，可以使用`visibility: hidden;`。

------

`overflow`属性用于控制元素内容溢出时的处理方式。当元素的内容大于容器的尺寸时，就会发生溢出。`overflow`属性允许你指定在这种情况下的处理方式。以下是常见的 `overflow` 属性值：

**`1. visible`：**

- 默认值。内容会溢出元素框，并且会在元素框外部可见。

```css
.example {
  overflow: visible;
}
```

**`2. hidden`：**

- 溢出的内容将被裁剪，不会显示在元素框外。

```css
.example {
  overflow: hidden;
}
```

**`3. scroll`：**

- 如果内容溢出，浏览器会显示滚动条以便查看溢出的内容。

```css
.example {
  overflow: scroll;
}
```

**`4. auto`：**

- 如果内容溢出，浏览器会自动添加滚动条，只在必要时显示。

```css
.example {
  overflow: auto;
}
```

