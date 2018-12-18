# D3 API Reference

`D3` 是一个相互协同工作的 [模块集合](https://github.com/d3); 你可以单独使用其中某些模块也可以使用默认构建的全部功能。每个模块的源码和文档都在对应的仓库中获取到。可以通过下面的链接获取更多信息。`d3` v3.x 和 4.x 之间的差异可以参考 [CHANGES](https://github.com/xswei/d3js_doc/tree/master/Release_Notes/CHANGES.MD); 3.x 的文档可以参考 [这里](https://github.com/d3/d3-3.x-api-reference/blob/master/API-Reference.md)

* [Arrays](#arrays-d3-array) ([Statistics](#statistics), [Search](#search), [Transformations](#transformations), [Histograms](#histograms))
* [Axes](#axes-d3-axis)
* [Brushes](#brushes-d3-brush)
* [Chords](#chords-d3-chord)
* [Collections](#collections-d3-collection) ([Objects](#objects), [Maps](#maps), [Sets](#sets), [Nests](#nests))
* [Colors](#colors-d3-color)
* [Color Schemes](#color-schemes-d3-scale-chromatic)
* [Contours](#contours-d3-contour)
* [Dispatches](#dispatches-d3-dispatch)
* [Dragging](#dragging-d3-drag)
* [Delimiter-Separated Values](#delimiter-separated-values-d3-dsv)
* [Easings](#easings-d3-ease)
* [Fetches](#fetches-d3-fetch)
* [Forces](#forces-d3-force)
* [Number Formats](#number-formats-d3-format)
* [Geographies](#geographies-d3-geo) ([Paths](#paths), [Projections](#projections), [Spherical Math](#spherical-math), [Spherical Shapes](#spherical-shapes), [Streams](#streams), [Transforms](#transforms))
* [Hierarchies](#hierarchies-d3-hierarchy)
* [Interpolators](#interpolators-d3-interpolate)
* [Paths](#paths-d3-path)
* [Polygons](#polygons-d3-polygon)
* [Quadtrees](#quadtrees-d3-quadtree)
* [Random Numbers](#random-numbers-d3-random)
* [Scales](#scales-d3-scale) ([Continuous](#continuous-scales), [Sequential](#sequential-scales), [Quantize](#quantize-scales), [Ordinal](#ordinal-scales))
* [Selections](#selections-d3-selection) ([Selecting](#selecting-elements), [Modifying](#modifying-elements), [Data](#joining-data), [Events](#handling-events), [Control](#control-flow), [Local Variables](#local-variables), [Namespaces](#namespaces))
* [Shapes](#shapes-d3-shape) ([Arcs](#arcs), [Pies](#pies), [Lines](#lines), [Areas](#areas), [Curves](#curves), [Links](#links), [Symbols](#symbols), [Stacks](#stacks))
* [Time Formats](#time-formats-d3-time-format)
* [Time Intervals](#time-intervals-d3-time)
* [Timers](#timers-d3-timer)
* [Transitions](#transitions-d3-transition)
* [Voronoi Diagrams](#voronoi-diagrams-d3-voronoi)
* [Zooming](#zooming-d3-zoom)

`D3` 使用 [语义化版本](https://semver.org/lang/zh-CN/). 当前的版本号通过 `d3.version` 暴露.

## [Arrays (d3-array)](https://github.com/xswei/d3-array)

数组操作，包括排序、查找、汇总等等

### [Statistics](https://github.com/xswei/d3-array/blob/master/README.md#statistics)

基本的静态统计计算方法

* [d3.min](https://github.com/xswei/d3-array/blob/master/README.md#min) - 计算数组中的最小值.
* [d3.max](https://github.com/xswei/d3-array/blob/master/README.md#max) - 计算数组中的最大值.
* [d3.extent](https://github.com/xswei/d3-array/blob/master/README.md#extent) - 计算数组中的最大值和最小值.
* [d3.sum](https://github.com/xswei/d3-array/blob/master/README.md#sum) - 计算数组元素之和.
* [d3.mean](https://github.com/xswei/d3-array/blob/master/README.md#mean) - 计算数组元素的算术中位数.
* [d3.median](https://github.com/xswei/d3-array/blob/master/README.md#median) - 计算数组元素的中位数 (也就是 0.5-分位数).
* [d3.quantile](https://github.com/xswei/d3-array/blob/master/README.md#quantile) - 计算有序数组的分位数.
* [d3.variance](https://github.com/xswei/d3-array/blob/master/README.md#variance) - 计算数组元素的方差.
* [d3.deviation](https://github.com/xswei/d3-array/blob/master/README.md#deviation) - 计算数组元素的标准差.

### [Search](https://github.com/xswei/d3-array/blob/master/README.md#search)

查找类方法

* [d3.scan](https://github.com/xswei/d3-array/blob/master/README.md#scan) - 使用指定的比较器进行线性查找指定的元素.
* [d3.bisect](https://github.com/xswei/d3-array/blob/master/README.md#bisect) - 二分查找有序数组中指定元素的索引.
* [d3.bisectRight](https://github.com/xswei/d3-array/blob/master/README.md#bisectRight) - 二分查找有序数组中指定元素的索引.
* [d3.bisectLeft](https://github.com/xswei/d3-array/blob/master/README.md#bisectLeft) - 二分查找有序数组中指定元素的索引.
* [d3.bisector](https://github.com/xswei/d3-array/blob/master/README.md#bisector) - 用指定的访问器或比较器对二分查找.
* [*bisector*.left](https://github.com/xswei/d3-array/blob/master/README.md#bisector_left) - 与 `bisectLeft` 类似, 可以指定比较器.
* [*bisector*.right](https://github.com/xswei/d3-array/blob/master/README.md#bisector_right) - 与 `bisectRight` 类似, 可以指定比较器.
* [d3.ascending](https://github.com/xswei/d3-array/blob/master/README.md#ascending) - 计算两个值的自然顺序.
* [d3.descending](https://github.com/xswei/d3-array/blob/master/README.md#descending) - 计算两个值的自然顺序.

### [Transformations](https://github.com/xswei/d3-array/blob/master/README.md#transformations)

数组变换和计算，返回新的数组

* [d3.cross](https://github.com/xswei/d3-array/blob/master/README.md#cross) - 计算两个数组的笛卡尔积.
* [d3.merge](https://github.com/xswei/d3-array/blob/master/README.md#merge) - 将多个数组合并为一个.
* [d3.pairs](https://github.com/xswei/d3-array/blob/master/README.md#pairs) - 将数组中相邻的两个元素两两结合.
* [d3.permute](https://github.com/xswei/d3-array/blob/master/README.md#permute) - 根据指定的索引返回对数组重排后的结果.
* [d3.shuffle](https://github.com/xswei/d3-array/blob/master/README.md#shuffle) - 随机打乱数组顺序
* [d3.ticks](https://github.com/xswei/d3-array/blob/master/README.md#ticks) - 从给定的区间范围内生成一系列值.
* [d3.tickIncrement](https://github.com/xswei/d3-array/blob/master/README.md#tickIncrement) - 从给定的区间范围内生成一系列值.
* [d3.tickStep](https://github.com/xswei/d3-array/blob/master/README.md#tickStep) - 从给定的区间范围内生成一系列值.
* [d3.range](https://github.com/xswei/d3-array/blob/master/README.md#range) - 根据指定的区间生成一系列值.
* [d3.transpose](https://github.com/xswei/d3-array/blob/master/README.md#transpose) - 将数组的数组进行转置.
* [d3.zip](https://github.com/xswei/d3-array/blob/master/README.md#zip) - 转置多个数组.

### [Histograms](https://github.com/xswei/d3-array/blob/master/README.md#histograms)

直方图将离散样本分成连续的，不重叠的区间

* [d3.histogram](https://github.com/xswei/d3-array/blob/master/README.md#histogram) - 创建一个新的直方图生成器.
* [*histogram*](https://github.com/xswei/d3-array/blob/master/README.md#_histogram) - 根据给定的数组计算直方图.
* [*histogram*.value](https://github.com/xswei/d3-array/blob/master/README.md#histogram_value) - 设置或获取直方图值访问器.
* [*histogram*.domain](https://github.com/xswei/d3-array/blob/master/README.md#histogram_domain) - 设置或获取直方图的可观测区间.
* [*histogram*.thresholds](https://github.com/xswei/d3-array/blob/master/README.md#histogram_thresholds) - 设置直方图阈值生成方式.
* [d3.thresholdFreedmanDiaconis](https://github.com/xswei/d3-array/blob/master/README.md#thresholdFreedmanDiaconis) - *Freedman–Diaconis* 阈值生成规则.
* [d3.thresholdScott](https://github.com/xswei/d3-array/blob/master/README.md#thresholdScott) - *Scott’s normal reference* 阈值生成规则.
* [d3.thresholdSturges](https://github.com/xswei/d3-array/blob/master/README.md#thresholdSturges) - *Sturges* 阈值生成规则.

## [Axes (d3-axis)](https://github.com/xswei/d3-axis)

基于比例尺提供人类友好的标尺刻度

* [d3.axisTop](https://github.com/xswei/d3-axis/blob/master/README.md#axisTop) - 创建一个新的刻度在上的坐标轴生成器
* [d3.axisRight](https://github.com/xswei/d3-axis/blob/master/README.md#axisRight) - 创建一个新的刻度在右的坐标轴生成器
* [d3.axisBottom](https://github.com/xswei/d3-axis/blob/master/README.md#axisBottom) - 创建一个新的刻度在下的坐标轴生成器
* [d3.axisLeft](https://github.com/xswei/d3-axis/blob/master/README.md#axisLeft) - 创建一个新的刻度在左的坐标轴生成器
* [*axis*](https://github.com/xswei/d3-axis/blob/master/README.md#_axis) - 为指定的选择器生成一个坐标轴
* [*axis*.scale](https://github.com/xswei/d3-axis/blob/master/README.md#axis_scale) - 设置坐标轴的比例尺
* [*axis*.ticks](https://github.com/xswei/d3-axis/blob/master/README.md#axis_ticks) - 自定义刻度的显示方式以及格式化刻度
* [*axis*.tickArguments](https://github.com/xswei/d3-axis/blob/master/README.md#axis_tickArguments) - 自定义如何生成刻度或者格式化刻度
* [*axis*.tickValues](https://github.com/xswei/d3-axis/blob/master/README.md#axis_tickValues) - 指定固定的刻度值
* [*axis*.tickFormat](https://github.com/xswei/d3-axis/blob/master/README.md#axis_tickFormat) - 指定固定的刻度格式化方式.
* [*axis*.tickSize](https://github.com/xswei/d3-axis/blob/master/README.md#axis_tickSize) - 设置刻度大小.
* [*axis*.tickSizeInner](https://github.com/xswei/d3-axis/blob/master/README.md#axis_tickSizeInner) - 设置内侧刻度大小.
* [*axis*.tickSizeOuter](https://github.com/xswei/d3-axis/blob/master/README.md#axis_tickSizeOuter) - 设置外侧(坐标轴两端)刻度大小.
* [*axis*.tickPadding](https://github.com/xswei/d3-axis/blob/master/README.md#axis_tickPadding) - 设置刻度和刻度文本之间的间距.

## [Brushes (d3-brush)](https://github.com/xswei/d3-brush)

使用鼠标或触摸选择一维或二维区域

* [d3.brush](https://github.com/xswei/d3-brush/blob/master/README.md#brush) - 创建一个新的二维刷取交互
* [d3.brushX](https://github.com/xswei/d3-brush/blob/master/README.md#brushX) - 创建一个新的 *x*- 维度的刷取交互
* [d3.brushY](https://github.com/xswei/d3-brush/blob/master/README.md#brushY) - 创建一个新的 *y*- 维度的刷取交互
* [*brush*](https://github.com/xswei/d3-brush/blob/master/README.md#_brush) - 将刷取操作应用到一个 `selection` 上
* [*brush*.move](https://github.com/xswei/d3-brush/blob/master/README.md#brush_move) - 移动刷取框选
* [*brush*.extent](https://github.com/xswei/d3-brush/blob/master/README.md#brush_extent) - 定义可刷取的范围
* [*brush*.filter](https://github.com/xswei/d3-brush/blob/master/README.md#brush_filter) - 过滤器定义哪些事件不触发刷取操作
* [*brush*.handleSize](https://github.com/xswei/d3-brush/blob/master/README.md#brush_handleSize) - 设置刷取把柄的大小
* [*brush*.on](https://github.com/xswei/d3-brush/blob/master/README.md#brush_on) - 注册刷取事件句柄
* [d3.brushSelection](https://github.com/xswei/d3-brush/blob/master/README.md#brushSelection) - 获取指定节点的刷取范围

## [Chords (d3-chord)](https://github.com/xswei/d3-chord)

* [d3.chord](https://github.com/xswei/d3-chord/blob/master/README.md#chord) - 创建一个新的弦图布局.
* [*chord*](https://github.com/xswei/d3-chord/blob/master/README.md#_chord) - 根据指定的方阵计算布局.
* [*chord*.padAngle](https://github.com/xswei/d3-chord/blob/master/README.md#chord_padAngle) - 设置相邻的分组之间的间隔
* [*chord*.sortGroups](https://github.com/xswei/d3-chord/blob/master/README.md#chord_sortGroups) - 定义分组排序规则
* [*chord*.sortSubgroups](https://github.com/xswei/d3-chord/blob/master/README.md#chord_sortSubgroups) - 定义分组内部子分组的排序规则
* [*chord*.sortChords](https://github.com/xswei/d3-chord/blob/master/README.md#chord_sortChords) - 定义弦之间的排序规则
* [d3.ribbon](https://github.com/xswei/d3-chord/blob/master/README.md#ribbon) - 创建一个 `ribbon`(弦)生成器
* [*ribbon*](https://github.com/xswei/d3-chord/blob/master/README.md#_ribbon) - 根据指定的数据返回一个 `path` 路径以表示弦.
* [*ribbon*.source](https://github.com/xswei/d3-chord/blob/master/README.md#ribbon_source) - 设置 `ribbon` 的源访问器.
* [*ribbon*.target](https://github.com/xswei/d3-chord/blob/master/README.md#ribbon_target) - 设置 `ribbon` 的目标访问器.
* [*ribbon*.radius](https://github.com/xswei/d3-chord/blob/master/README.md#ribbon_radius) - 设置 `ribbon` 的半径.
* [*ribbon*.startAngle](https://github.com/xswei/d3-chord/blob/master/README.md#ribbon_startAngle) - 设置 `ribbon` 的起始角度访问器.
* [*ribbon*.endAngle](https://github.com/xswei/d3-chord/blob/master/README.md#ribbon_endAngle) - 设置 `ribbon` 的终止角度访问器.
* [*ribbon*.context](https://github.com/xswei/d3-chord/blob/master/README.md#ribbon_context) - 设置渲染上下文(`canvas`).

## [Collections (d3-collection)](https://github.com/xswei/d3-collection)

一组方便的数据结构。

### [Objects](https://github.com/xswei/d3-collection/blob/master/README.md#objects)

将关联数组(对象)转为数组的一组方法

* [d3.keys](https://github.com/xswei/d3-collection/blob/master/README.md#keys) - 关联数组中所有的键
* [d3.values](https://github.com/xswei/d3-collection/blob/master/README.md#values) - 关联数组中所有的值
* [d3.entries](https://github.com/xswei/d3-collection/blob/master/README.md#entries) - 将关联数组转为 `key-value` 形式的对象数组

### [Maps](https://github.com/xswei/d3-collection/blob/master/README.md#maps)

与 `ES6` 的 `Map` 类似，但是有些不同

* [d3.map](https://github.com/xswei/d3-collection/blob/master/README.md#map) - 创建一个新的空的 `map` 映射.
* [*map*.has](https://github.com/xswei/d3-collection/blob/master/README.md#map_has) - 当 `map` 映射中有给定的 `key` 时返回 `true`
* [*map*.get](https://github.com/xswei/d3-collection/blob/master/README.md#map_get) - 根据指定的 `key` 返回对应的值
* [*map*.set](https://github.com/xswei/d3-collection/blob/master/README.md#map_set) - 设置指定的 `key` 对应的值为指定的值
* [*map*.remove](https://github.com/xswei/d3-collection/blob/master/README.md#map_remove) - 移除指定的 `key` 以及值
* [*map*.clear](https://github.com/xswei/d3-collection/blob/master/README.md#map_clear) - 清空 `map` 映射中所有的项
* [*map*.keys](https://github.com/xswei/d3-collection/blob/master/README.md#map_keys) - 以数组的形式获取 `map` 映射中的 `key`
* [*map*.values](https://github.com/xswei/d3-collection/blob/master/README.md#map_values) - 以数组的形式获取 `map` 映射中的 `value`
* [*map*.entries](https://github.com/xswei/d3-collection/blob/master/README.md#map_entries) - 以数组的形式获取 `map` 映射中的 `key-values` 对象
* [*map*.each](https://github.com/xswei/d3-collection/blob/master/README.md#map_each) - 遍历每一项并执行指定的方法.
* [*map*.empty](https://github.com/xswei/d3-collection/blob/master/README.md#map_empty) - 判断 `map` 映射是否为空
* [*map*.size](https://github.com/xswei/d3-collection/blob/master/README.md#map_size) - 计算 `map` 映射中项的数目

### [Sets](https://github.com/xswei/d3-collection/blob/master/README.md#sets)

与 `ES6`的 `Set` 类似，但是有些不同

* [d3.set](https://github.com/xswei/d3-collection/blob/master/README.md#set) - 创建一个新的空的集合
* [*set*.has](https://github.com/xswei/d3-collection/blob/master/README.md#set_has) - 判断集合中是否包含给定的值
* [*set*.add](https://github.com/xswei/d3-collection/blob/master/README.md#set_add) - 将指定的值添加到集合中
* [*set*.remove](https://github.com/xswei/d3-collection/blob/master/README.md#set_remove) - 移除集合中指定的值
* [*set*.clear](https://github.com/xswei/d3-collection/blob/master/README.md#set_clear) - 清空集合中所有的值
* [*set*.values](https://github.com/xswei/d3-collection/blob/master/README.md#set_values) - 以数组的形式获取集合中的所有值
* [*set*.each](https://github.com/xswei/d3-collection/blob/master/README.md#set_each) - 为集合中每一个值执行指定的函数
* [*set*.empty](https://github.com/xswei/d3-collection/blob/master/README.md#set_empty) - 判断集合是否为空
* [*set*.size](https://github.com/xswei/d3-collection/blob/master/README.md#set_size) - 获取集合中项的多少

### [Nests](https://github.com/xswei/d3-collection/blob/master/README.md#nests)

根据指定的规则将数组重组为层次结构

* [d3.nest](https://github.com/xswei/d3-collection/blob/master/README.md#nest) - 创建一个新的嵌套对象.
* [*nest*.key](https://github.com/xswei/d3-collection/blob/master/README.md#nest_key) - 为嵌套操作添加一个 `key` 作为分层依据
* [*nest*.sortKeys](https://github.com/xswei/d3-collection/blob/master/README.md#nest_sortKeys) - 根据 `key` 对当前层次的进行排序
* [*nest*.sortValues](https://github.com/xswei/d3-collection/blob/master/README.md#nest_sortValues) - 根据 `value` 对当叶节点进行排序
* [*nest*.rollup](https://github.com/xswei/d3-collection/blob/master/README.md#nest_rollup) - 为叶节点指定一个 `rollup` (归纳)函数
* [*nest*.map](https://github.com/xswei/d3-collection/blob/master/README.md#nest_map) - 生成嵌套结果，并返回一个 `map` 映射
* [*nest*.object](https://github.com/xswei/d3-collection/blob/master/README.md#nest_object) - 生成嵌套结果并返回一个关联数组
* [*nest*.entries](https://github.com/xswei/d3-collection/blob/master/README.md#nest_entries) - 生成嵌套结果，并返回一组  `key-value` 元组

## [Colors (d3-color)](https://github.com/xswei/d3-color)

颜色空间以及转换

* [d3.color](https://github.com/xswei/d3-color/blob/master/README.md#color) - 转换指定的 `CSS` 颜色字符串.
* [*color*.rgb](https://github.com/xswei/d3-color/blob/master/README.md#color_rgb) - 计算当前颜色值的 `RGB` 表示.
* [*color*.brighter](https://github.com/xswei/d3-color/blob/master/README.md#color_brighter) - 创建一个更亮的颜色副本.
* [*color*.darker](https://github.com/xswei/d3-color/blob/master/README.md#color_darker) - 创建一个更暗的颜色副本
* [*color*.displayable](https://github.com/xswei/d3-color/blob/master/README.md#color_displayable) - 判断当前设备是否支持当前颜色
* [*color*.hex](https://github.com/xswei/d3-color/blob/master/README.md#color_hex) - 返回十六进制的 `RGB` 字符串标识当前的颜色.
* [*color*.toString](https://github.com/xswei/d3-color/blob/master/README.md#color_toString) - 将当前颜色转为 `RGB` 颜色的十六进制表示
* [d3.rgb](https://github.com/xswei/d3-color/blob/master/README.md#rgb) - 创建一个新的 `RGB` 颜色.
* [d3.hsl](https://github.com/xswei/d3-color/blob/master/README.md#hsl) - 创建一个新的 `HSL` 颜色.
* [d3.lab](https://github.com/xswei/d3-color/blob/master/README.md#lab) - 创建一个新的 `Lab` 颜色.
* [d3.hcl](https://github.com/xswei/d3-color/blob/master/README.md#hcl) - 创建一个新的 `HCL` 颜色.
* [d3.lch](https://github.com/xswei/d3-color/blob/master/README.md#lch) - 创建一个新的 `HCL` 颜色.
* [d3.gray](https://github.com/xswei/d3-color/blob/master/README.md#gray) - 创建一个新的 `Lab` 灰色( `a` = `b` = 0).
* [d3.cubehelix](https://github.com/xswei/d3-color/blob/master/README.md#cubehelix) - 创建一个新的 `Cubehelix` 颜色.

## [Color Schemes (d3-scale-chromatic)](https://github.com/xswei/d3-scale-chromatic)

Color ramps and palettes for quantitative, ordinal and categorical scales.

### Categorical

* [d3.schemeCategory10](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeCategory10) -
* [d3.schemeAccent](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeAccent) -
* [d3.schemeDark2](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeDark2) -
* [d3.schemePaired](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePaired) -
* [d3.schemePastel1](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePastel1) -
* [d3.schemePastel2](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePastel2) -
* [d3.schemeSet1](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeSet1) -
* [d3.schemeSet2](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeSet2) -
* [d3.schemeSet3](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeSet3) -

### Diverging

* [d3.interpolateBrBG](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolatePiYG](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolatePRGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolatePuOr](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateRdBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateRdGy](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateRdYlBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateRdYlGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateSpectral](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.schemeBrBG](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeBrBG) -
* [d3.schemePiYG](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePiYG) -
* [d3.schemePRGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePRGn) -
* [d3.schemePuOr](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePuOr) -
* [d3.schemeRdBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeRdBu) -
* [d3.schemeRdGy](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeRdGy) -
* [d3.schemeRdYlBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeRdYlBu) -
* [d3.schemeRdYlGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeRdYlGn) -
* [d3.schemeSpectral](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeSpectral) -

### Sequential (Single Hue)

* [d3.interpolateBlues](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateGreens](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateGreys](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateOranges](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolatePurples](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateReds](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.schemeBlues](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeBlues) -
* [d3.schemeGreens](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeGreens) -
* [d3.schemeGreys](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeGreys) -
* [d3.schemeOranges](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeOranges) -
* [d3.schemePurples](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePurples) -
* [d3.schemeReds](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeReds) -

### Sequential (Multi-Hue)

* [d3.interpolateBuGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateBuPu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateCool](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateCubehelixDefault](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateGnBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateInferno](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateMagma](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateOrRd](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolatePlasma](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolatePuBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolatePuBuGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolatePuRd](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateRdPu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateViridis](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateWarm](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateYlGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateYlGnBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateYlOrBr](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.interpolateYlOrRd](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md) -
* [d3.schemeBuGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeBuGn) -
* [d3.schemeBuPu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeBuPu) -
* [d3.schemeGnBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeGnBu) -
* [d3.schemeOrRd](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeOrRd) -
* [d3.schemePuBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePuBu) -
* [d3.schemePuBuGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePuBuGn) -
* [d3.schemePuRd](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemePuRd) -
* [d3.schemeRdPu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeRdPu) -
* [d3.schemeYlGn](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeYlGn) -
* [d3.schemeYlGnBu](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeYlGnBu) -
* [d3.schemeYlOrBr](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeYlOrBr) -
* [d3.schemeYlOrRd](https://github.com/xswei/d3-scale-chromatic/blob/master/README.md#schemeYlOrRd) -

### Cyclical

* [d3.interpolateRainbow](https://github.com/d3/d3-scale-chromatic/blob/master/README.md#interpolateRainbow) - the “less-angry” rainbow
* [d3.interpolateSinebow](https://github.com/d3/d3-scale-chromatic/blob/master/README.md#interpolateSinebow) - the “sinebow” smooth rainbow

## [Contours (d3-contour)](https://github.com/xswei/d3-contour)

Compute contour polygons using marching squares.

* [d3.contours](https://github.com/d3/d3-contour/blob/master/README.md#contours) - create a new contour generator.
* [contours](https://github.com/d3/d3-contour/blob/master/README.md#_contours) - compute the contours for a given grid of values.
* [contours.contour](https://github.com/d3/d3-contour/blob/master/README.md#contours_contour) -
* [contours.size](https://github.com/d3/d3-contour/blob/master/README.md#contours_size) -
* [contours.smooth](https://github.com/d3/d3-contour/blob/master/README.md#contours_smooth) -
* [contours.thresholds](https://github.com/d3/d3-contour/blob/master/README.md#contours_thresholds) -
* [d3.contourDensity](https://github.com/d3/d3-contour/blob/master/README.md#contourDensity) - create a new density estimator.
* [density](https://github.com/d3/d3-contour/blob/master/README.md#_density) - estimate the density of a given array of samples.
* [density.x](https://github.com/d3/d3-contour/blob/master/README.md#density_x) -
* [density.y](https://github.com/d3/d3-contour/blob/master/README.md#density_y) -
* [density.cellSize](https://github.com/d3/d3-contour/blob/master/README.md#density_cellSize) -
* [density.thresholds](https://github.com/d3/d3-contour/blob/master/README.md#density_thresholds) -
* [density.bandwidth](https://github.com/d3/d3-contour/blob/master/README.md#density_bandwidth) -

## [Dispatches (d3-dispatch)](https://github.com/xswei/d3-dispatch)

使用命名回调函数分离关注点

* [d3.dispatch](https://github.com/xswei/d3-dispatch/blob/master/README.md#dispatch) - 创建一个自定义事件分发器
* [*dispatch*.on](https://github.com/xswei/d3-dispatch/blob/master/README.md#dispatch_on) - 注册或取消注册事件监听器
* [*dispatch*.copy](https://github.com/xswei/d3-dispatch/blob/master/README.md#dispatch_copy) - 创建分发器的副本
* [*dispatch*.*call*](https://github.com/xswei/d3-dispatch/blob/master/README.md#dispatch_call) - 分发事件到注册的事件监听器
* [*dispatch*.*apply*](https://github.com/xswei/d3-dispatch/blob/master/README.md#dispatch_apply) - 分发事件到注册事件监听器

## [Dragging (d3-drag)](https://github.com/xswei/d3-drag)

使用鼠标或触摸输入拖放 `SVG`, `HTML` 或者 `Canvas`

* [d3.drag](https://github.com/xswei/d3-drag/blob/master/README.md#drag) - 创建一个拖拽交互.
* [*drag*](https://github.com/xswei/d3-drag/blob/master/README.md#_drag) - 将拖拽交互应用于选择集上.
* [*drag*.container](https://github.com/xswei/d3-drag/blob/master/README.md#drag_container) - 设置拖拽坐标系统.
* [*drag*.filter](https://github.com/xswei/d3-drag/blob/master/README.md#drag_filter) - 忽略一些拖拽启动事件.
* [*drag*.touchable](https://github.com/xswei/d3-drag/blob/master/README.md#drag_touchable) - 设置触摸支持检测.
* [*drag*.subject](https://github.com/xswei/d3-drag/blob/master/README.md#drag_subject) - 设置被拖拽的主体.
* [*drag*.clickDistance](https://github.com/xswei/d3-drag/blob/master/README.md#drag_clickDistance) - 设置可触发 `click` 事件的阈值距离
* [*drag*.on](https://github.com/xswei/d3-drag/blob/master/README.md#drag_on) - 监听拖拽事件.
* [*event*.on](https://github.com/xswei/d3-drag/blob/master/README.md#event_on) - 在当前拖拽手势中监听拖拽事件.
* [d3.dragDisable](https://github.com/xswei/d3-drag/blob/master/README.md#dragDisable) - 阻止原生拖拽以及文本选择.
* [d3.dragEnable](https://github.com/xswei/d3-drag/blob/master/README.md#dragEnable) - 启用原生拖拽以及文本选择.

## [Delimiter-Separated Values (d3-dsv)](https://github.com/xswei/d3-dsv)

解析和格式化以分隔符隔开的特定格式文件或字符串，大多数情况下指 `CSV` 和 `TSV`.

* [d3.dsvFormat](https://github.com/xswei/d3-dsv/blob/master/README.md#dsvFormat) - 根据指定的分隔符创建一个新的解析器和格式化器.
* [*dsv*.parse](https://github.com/xswei/d3-dsv/blob/master/README.md#dsv_parse) - 解析指定的字符串并返回对象数组.
* [*dsv*.parseRows](https://github.com/xswei/d3-dsv/blob/master/README.md#dsv_parseRows) - 解析指定的字符串并返回行数组.
* [*dsv*.format](https://github.com/xswei/d3-dsv/blob/master/README.md#dsv_format) - 格式化指定的对象数组为字符串.
* [*dsv*.formatRows](https://github.com/xswei/d3-dsv/blob/master/README.md#dsv_formatRows) - 格式化指定的行数组为字符串.
* [d3.csvParse](https://github.com/xswei/d3-dsv/blob/master/README.md#csvParse) - 解析指定的 `CSV` 字符串并返回对象数组.
* [d3.csvParseRows](https://github.com/xswei/d3-dsv/blob/master/README.md#csvParseRows) - 解析指定的 `CSV` 字符串并返回行数组.
* [d3.csvFormat](https://github.com/xswei/d3-dsv/blob/master/README.md#csvFormat) - 格式化指定的对象数组为 `CSV`.
* [d3.csvFormatRows](https://github.com/xswei/d3-dsv/blob/master/README.md#csvFormatRows) - 格式化指定的行数组为 `CSV`.
* [d3.tsvParse](https://github.com/xswei/d3-dsv/blob/master/README.md#tsvParse) - 解析指定的 `TSV` 字符串并返回对象数组.
* [d3.tsvParseRows](https://github.com/xswei/d3-dsv/blob/master/README.md#tsvParseRows) - 解析指定的 `TSV` 字符串并返回行数组.
* [d3.tsvFormat](https://github.com/xswei/d3-dsv/blob/master/README.md#tsvFormat) - 格式化指定的对象数组为 `TSV`.
* [d3.tsvFormatRows](https://github.com/xswei/d3-dsv/blob/master/README.md#tsvFormatRows) - 格式化指定的行数组为 `TSV`.

## [Easings (d3-ease)](https://github.com/xswei/d3-ease)

平滑过渡的过渡函数.

* [*ease*](https://github.com/xswei/d3-ease/blob/master/README.md#_ease) - 计算标准时间经过缓动方法计算后的时间.
* [d3.easeLinear](https://github.com/xswei/d3-ease/blob/master/README.md#easeLinear) - `linear` 缓动; 恒等函数.
* [d3.easePolyIn](https://github.com/xswei/d3-ease/blob/master/README.md#easePolyIn) - `polynomial` 缓动.
* [d3.easePolyOut](https://github.com/xswei/d3-ease/blob/master/README.md#easePolyOut) - 反转 `polynomial` 缓动.
* [d3.easePolyInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easePolyInOut) - 对称 `polynomial` 缓动.
* [*poly*.exponent](https://github.com/xswei/d3-ease/blob/master/README.md#poly_exponent) - 指定 `polynomial` 的指数.
* [d3.easeQuad](https://github.com/xswei/d3-ease/blob/master/README.md#easeQuad) - `easeQuadInOut` 的别名.
* [d3.easeQuadIn](https://github.com/xswei/d3-ease/blob/master/README.md#easeQuadIn) - `quadratic` 缓动.
* [d3.easeQuadOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeQuadOut) - 反转 `quadratic` 缓动.
* [d3.easeQuadInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeQuadInOut) - 对称 `quadratic` 缓动.
* [d3.easeCubic](https://github.com/xswei/d3-ease/blob/master/README.md#easeCubic) - `easeCubicInOut` 的别名.
* [d3.easeCubicIn](https://github.com/xswei/d3-ease/blob/master/README.md#easeCubicIn) - `cubic` 缓动.
* [d3.easeCubicOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeCubicOut) - 反转 `cubic` 缓动.
* [d3.easeCubicInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeCubicInOut) - 对称 `cubic` 缓动.
* [d3.easeSin](https://github.com/xswei/d3-ease/blob/master/README.md#easeSin) - `easeSinInOut` 的别名.
* [d3.easeSinIn](https://github.com/xswei/d3-ease/blob/master/README.md#easeSinIn) - `sinusoidal` 缓动.
* [d3.easeSinOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeSinOut) - 反转 `sinusoidal` 缓动.
* [d3.easeSinInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeSinInOut) - 对称 `sinusoidal` 缓动.
* [d3.easeExp](https://github.com/xswei/d3-ease/blob/master/README.md#easeExp) - `easeExpInOut` 的别名.
* [d3.easeExpIn](https://github.com/xswei/d3-ease/blob/master/README.md#easeExpIn) - `exponential` 缓动.
* [d3.easeExpOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeExpOut) - 反转 `exponential` 缓动.
* [d3.easeExpInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeExpInOut) - 对称 `exponential` 缓动.
* [d3.easeCircle](https://github.com/xswei/d3-ease/blob/master/README.md#easeCircle) - `easeCircleInOut` 的别名.
* [d3.easeCircleIn](https://github.com/xswei/d3-ease/blob/master/README.md#easeCircleIn) - `circular` 缓动.
* [d3.easeCircleOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeCircleOut) - 反转 `circular` 缓动.
* [d3.easeCircleInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeCircleInOut) - 对称 `circular` 缓动.
* [d3.easeElastic](https://github.com/xswei/d3-ease/blob/master/README.md#easeElastic) - `easeElasticOut` 的别名.
* [d3.easeElasticIn](https://github.com/xswei/d3-ease/blob/master/README.md#easeElasticIn) - `elastic` 缓动, 就像是橡皮筋.
* [d3.easeElasticOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeElasticOut) - 反转 `elastic` 缓动.
* [d3.easeElasticInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeElasticInOut) - 对称 `elastic` 缓动.
* [*elastic*.amplitude](https://github.com/xswei/d3-ease/blob/master/README.md#elastic_amplitude) - 指定 `elastic` 的振幅.
* [*elastic*.period](https://github.com/xswei/d3-ease/blob/master/README.md#elastic_period) - 指定 `elastic` 的周期.
* [d3.easeBack](https://github.com/xswei/d3-ease/blob/master/README.md#easeBack) - `easeBackInOut` 的别名.
* [d3.easeBackIn](https://github.com/xswei/d3-ease/blob/master/README.md#easeBackIn) - `anticipatory` 缓动, 就像是舞者在跳跃之前先弯曲膝盖.
* [d3.easeBackOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeBackOut) - 反转 `anticipatory` 缓动.
* [d3.easeBackInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeBackInOut) - 对称 `anticipatory` 缓动.
* [*back*.overshoot](https://github.com/xswei/d3-ease/blob/master/README.md#back_overshoot) - 指定超调量.
* [d3.easeBounce](https://github.com/xswei/d3-ease/blob/master/README.md#easeBounce) - `easeBounceOut` 的别名.
* [d3.easeBounceIn](https://github.com/xswei/d3-ease/blob/master/README.md#easeBounceIn) - `bounce` 缓动, 就像是橡皮球.
* [d3.easeBounceOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeBounceOut) - 反转 `bounce` 缓动.
* [d3.easeBounceInOut](https://github.com/xswei/d3-ease/blob/master/README.md#easeBounceInOut) - 对称 `bounce` 缓动.

## [Fetches (d3-fetch)](https://github.com/xswei/d3-fetch)

基于 Fetch API 的更为便捷的获取数据方法.

* [d3.blob](https://github.com/xswei/d3-fetch/blob/master/README.md#blob) - 以 `blob` 的形式获取文件.
* [d3.buffer](https://github.com/xswei/d3-fetch/blob/master/README.md#buffer) - 以 `array buffer` 的形式获取文件.
* [d3.csv](https://github.com/xswei/d3-fetch/blob/master/README.md#csv) - 获取逗号分隔符 (`CSV`) 文件.
* [d3.dsv](https://github.com/xswei/d3-fetch/blob/master/README.md#dsv) - 获取分隔符 (`DSV`) 文件.
* [d3.image](https://github.com/xswei/d3-fetch/blob/master/README.md#image) - 获取图片.
* [d3.json](https://github.com/xswei/d3-fetch/blob/master/README.md#json) - 获取 `JSON` 文件.
* [d3.text](https://github.com/xswei/d3-fetch/blob/master/README.md#text) - 获取无格式文本.
* [d3.tsv](https://github.com/xswei/d3-fetch/blob/master/README.md#tsv) - 获取 `tab` 分隔符 (`TSV`) 文件.

## [Forces (d3-force)](https://github.com/xswei/d3-force)

使用速度 `Verlet` 积分的力模型仿真布局.

* [d3.forceSimulation](https://github.com/xswei/d3-force/blob/master/README.md#forceSimulation) - 创建一个新的力学仿真.
* [*simulation*.restart](https://github.com/xswei/d3-force/blob/master/README.md#simulation_restart) - 重新启动仿真的定时器.
* [*simulation*.stop](https://github.com/xswei/d3-force/blob/master/README.md#simulation_stop) - 停止仿真的定时器.
* [*simulation*.tick](https://github.com/xswei/d3-force/blob/master/README.md#simulation_tick) - 进行一步仿真模拟.
* [*simulation*.nodes](https://github.com/xswei/d3-force/blob/master/README.md#simulation_nodes) - 设置仿真的节点.
* [*simulation*.alpha](https://github.com/xswei/d3-force/blob/master/README.md#simulation_alpha) - 设置当前的 `alpha` 值.
* [*simulation*.alphaMin](https://github.com/xswei/d3-force/blob/master/README.md#simulation_alphaMin) - 设置最小 `alpha` 阈值.
* [*simulation*.alphaDecay](https://github.com/xswei/d3-force/blob/master/README.md#simulation_alphaDecay) - 设置 `alpha` 衰减率.
* [*simulation*.alphaTarget](https://github.com/xswei/d3-force/blob/master/README.md#simulation_alphaTarget) - 设置目标 `alpha` 值.
* [*simulation*.velocityDecay](https://github.com/xswei/d3-force/blob/master/README.md#simulation_velocityDecay) - 设置速度衰减率.
* [*simulation*.force](https://github.com/xswei/d3-force/blob/master/README.md#simulation_force) - 添加或移除一个力模型.
* [*simulation*.find](https://github.com/xswei/d3-force/blob/master/README.md#simulation_find) - 根据指定的位置找出最近的节点.
* [*simulation*.on](https://github.com/xswei/d3-force/blob/master/README.md#simulation_on) - 添加或移除事件监听器.
* [*force*](https://github.com/xswei/d3-force/blob/master/README.md#_force) - 应用力模型.
* [*force*.initialize](https://github.com/xswei/d3-force/blob/master/README.md#force_initialize) - 根据指定的节点初始化力模型.
* [d3.forceCenter](https://github.com/xswei/d3-force/blob/master/README.md#forceCenter) - 创建一个中心作用力.
* [*center*.x](https://github.com/xswei/d3-force/blob/master/README.md#center_x) - 设置中心作用力的 *x* -坐标.
* [*center*.y](https://github.com/xswei/d3-force/blob/master/README.md#center_y) - 设置中心作用力的 *y* -坐标.
* [d3.forceCollide](https://github.com/xswei/d3-force/blob/master/README.md#forceCollide) - 创建一个圆形区域的碰撞检测力模型.
* [*collide*.radius](https://github.com/xswei/d3-force/blob/master/README.md#collide_radius) - 设置碰撞半径.
* [*collide*.strength](https://github.com/xswei/d3-force/blob/master/README.md#collide_strength) - 设置碰撞检测力模型的强度.
* [*collide*.iterations](https://github.com/xswei/d3-force/blob/master/README.md#collide_iterations) - 设置迭代次数.
* [d3.forceLink](https://github.com/xswei/d3-force/blob/master/README.md#forceLink) - 创建一个 `link`(弹簧) 作用力.
* [*link*.links](https://github.com/xswei/d3-force/blob/master/README.md#link_links) - 设置弹簧作用力的边.
* [*link*.id](https://github.com/xswei/d3-force/blob/master/README.md#link_id) - 设置边元素中节点的查找方式是索引还是 `id` 字符串.
* [*link*.distance](https://github.com/xswei/d3-force/blob/master/README.md#link_distance) - 设置 `link` 的距离.
* [*link*.strength](https://github.com/xswei/d3-force/blob/master/README.md#link_strength) - 设置 `link` 的强度.
* [*link*.iterations](https://github.com/xswei/d3-force/blob/master/README.md#link_iterations) - 设置迭代次数.
* [d3.forceManyBody](https://github.com/xswei/d3-force/blob/master/README.md#forceManyBody) - 创建一个电荷作用力模型.
* [*manyBody*.strength](https://github.com/xswei/d3-force/blob/master/README.md#manyBody_strength) - 设置电荷力模型的强度.
* [*manyBody*.theta](https://github.com/xswei/d3-force/blob/master/README.md#manyBody_theta) - 设置 `Barnes–Hut` 算法的精度.
* [*manyBody*.distanceMin](https://github.com/xswei/d3-force/blob/master/README.md#manyBody_distanceMin) - 限制节点之间的最小距离.
* [*manyBody*.distanceMax](https://github.com/xswei/d3-force/blob/master/README.md#manyBody_distanceMax) - 限制节点之间的最大距离.
* [d3.forceX](https://github.com/xswei/d3-force/blob/master/README.md#forceX) - 创建一个 *x* -方向的一维作用力.
* [*x*.strength](https://github.com/xswei/d3-force/blob/master/README.md#x_strength) - 设置力强度.
* [*x*.x](https://github.com/xswei/d3-force/blob/master/README.md#x_x) - 设置目标 *x* -坐标.
* [d3.forceY](https://github.com/xswei/d3-force/blob/master/README.md#forceY) - 创建一个 *y* -方向的一维作用力.
* [*y*.strength](https://github.com/xswei/d3-force/blob/master/README.md#y_strength) - 设置力强度.
* [*y*.y](https://github.com/xswei/d3-force/blob/master/README.md#y_y) - 设置目标 *y* -坐标.
* [d3.forceRadial](https://github.com/xswei/d3-force/blob/master/README.md#forceRadial) - 创建一个环形布局的作用力.
* [*radial*.strength](https://github.com/xswei/d3-force/blob/master/README.md#radial_strength) - 设置力强度.
* [*radial*.radius](https://github.com/xswei/d3-force/blob/master/README.md#radial_radius) - 设置目标半径.
* [*radial*.x](https://github.com/xswei/d3-force/blob/master/README.md#radial_x) - 设置环形作用力的目标中心 *x* -坐标.
* [*radial*.y](https://github.com/xswei/d3-force/blob/master/README.md#radial_y) - 设置环形作用力的目标中心 *y* -坐标.

## [Number Formats (d3-format)](https://github.com/xswei/d3-format)

对人类友好的数值格式化.

* [d3.format](https://github.com/xswei/d3-format/blob/master/README.md#format) - 默认语言环境中的 *locale*.format 别名.
* [d3.formatPrefix](https://github.com/xswei/d3-format/blob/master/README.md#formatPrefix) - 默认语言环境中的 *locale*.formatPrefix 别名.
* [d3.formatSpecifier](https://github.com/xswei/d3-format/blob/master/README.md#formatSpecifier) - 解析指定的说明符.
* [d3.formatLocale](https://github.com/xswei/d3-format/blob/master/README.md#formatLocale) - 定义一个自定义语言环境.
* [d3.formatDefaultLocale](https://github.com/xswei/d3-format/blob/master/README.md#formatDefaultLocale) - 定义一个默认的语言环境.
* [*locale*.format](https://github.com/xswei/d3-format/blob/master/README.md#locale_format) - 创建一个数值格式化器.
* [*locale*.formatPrefix](https://github.com/xswei/d3-format/blob/master/README.md#locale_formatPrefix) - 创建一个估计度量标准的数值格式化器.
* [d3.precisionFixed](https://github.com/xswei/d3-format/blob/master/README.md#precisionFixed) - compute decimal precision for fixed-point notation.
* [d3.precisionPrefix](https://github.com/xswei/d3-format/blob/master/README.md#precisionPrefix) - compute decimal precision for SI-prefix notation.
* [d3.precisionRound](https://github.com/xswei/d3-format/blob/master/README.md#precisionRound) - compute significant digits for rounded notation.

## [Geographies (d3-geo)](https://github.com/xswei/d3-geo)

地理投影, 形状以及数学计算.

### [Paths](https://github.com/xswei/d3-geo/blob/master/README.md#paths)

* [d3.geoPath](https://github.com/xswei/d3-geo/blob/master/README.md#geoPath) - 创建一个新的地理路径生成器.
* [*path*](https://github.com/xswei/d3-geo/blob/master/README.md#_path) - 投影并渲染指定的地理特征.
* [*path*.area](https://github.com/xswei/d3-geo/blob/master/README.md#path_area) - 计算指定的二位地理特征面积.
* [*path*.bounds](https://github.com/xswei/d3-geo/blob/master/README.md#path_bounds) - 计算指定的二位地理特征包裹框.
* [*path*.centroid](https://github.com/xswei/d3-geo/blob/master/README.md#path_centroid) - 算指定的二位地理特征中心.
* [*path*.measure](https://github.com/xswei/d3-geo/blob/master/README.md#path_measure) - 算指定的二位地理特征周长.
* [*path*.projection](https://github.com/xswei/d3-geo/blob/master/README.md#path_projection) - 设置地理路径生成器的投影方式.
* [*path*.context](https://github.com/xswei/d3-geo/blob/master/README.md#path_context) - 设置渲染上下文.
* [*path*.pointRadius](https://github.com/xswei/d3-geo/blob/master/README.md#path_pointRadius) - 设置点特征的半径.

### [Projections](https://github.com/xswei/d3-geo/blob/master/README.md#projections)

* [*projection*](https://github.com/xswei/d3-geo/blob/master/README.md#_projection) - 将指定的球面上一点投影到平面.
* [*projection*.invert](https://github.com/xswei/d3-geo/blob/master/README.md#projection_invert) - 逆转投影，根据平面一点反向计算球面坐标.
* [*projection*.stream](https://github.com/xswei/d3-geo/blob/master/README.md#projection_stream) - wrap the specified stream to project geometry.
* [*projection*.clipAngle](https://github.com/xswei/d3-geo/blob/master/README.md#projection_clipAngle) - set the radius of the clip circle.
* [*projection*.clipExtent](https://github.com/xswei/d3-geo/blob/master/README.md#projection_clipExtent) - set the viewport clip extent, in pixels.
* [*projection*.angle](https://github.com/d3/d3-geo/blob/master/README.md#projection_angle) - set the post-projection rotation.
* [*projection*.scale](https://github.com/xswei/d3-geo/blob/master/README.md#projection_scale) - set the scale factor.
* [*projection*.translate](https://github.com/xswei/d3-geo/blob/master/README.md#projection_translate) - set the translation offset.
* [*projection*.fitExtent](https://github.com/xswei/d3-geo/blob/master/README.md#projection_fitExtent) - set the scale and translate to fit a GeoJSON object.
* [*projection*.fitSize](https://github.com/xswei/d3-geo/blob/master/README.md#projection_fitSize) - set the scale and translate to fit a GeoJSON object.
* [*projection*.fitWidth](https://github.com/xswei/d3-geo/blob/master/README.md#projection_fitWidth) - set the scale and translate to fit a GeoJSON object.
* [*projection*.fitHeight](https://github.com/xswei/d3-geo/blob/master/README.md#projection_fitHeight) - set the scale and translate to fit a GeoJSON object.
* [*projection*.center](https://github.com/xswei/d3-geo/blob/master/README.md#projection_center) - set the center point.
* [*projection*.rotate](https://github.com/xswei/d3-geo/blob/master/README.md#projection_rotate) - set the three-axis spherical rotation angles.
* [*projection*.precision](https://github.com/xswei/d3-geo/blob/master/README.md#projection_precision) - set the precision threshold for adaptive sampling.
* [*projection*.preclip](https://github.com/xswei/d3-geo/blob/master/README.md#projection.preclip) - set the spherical clipping stream transform.
* [*projection*.postclip](https://github.com/xswei/d3-geo/blob/master/README.md#projection.postclip) - set the planar clipping stream transform.
* [d3.geoClipAntimeridian](https://github.com/xswei/d3-geo/blob/master/README.md#geoClipAntimeridian) - cuts spherical geometries that cross the antimeridian.
* [d3.geoClipCircle](https://github.com/xswei/d3-geo/blob/master/README.md#geoClipCircle) - clips spherical geometries to a small circle.
* [d3.geoClipRectangle](https://github.com/xswei/d3-geo/blob/master/README.md#geoClipRectangle) - clips planar geometries to a rectangular viewport.
* [d3.geoAlbers](https://github.com/xswei/d3-geo/blob/master/README.md#geoAlbers) - the Albers equal-area conic projection.
* [d3.geoAlbersUsa](https://github.com/xswei/d3-geo/blob/master/README.md#geoAlbersUsa) - a composite Albers projection for the United States.
* [d3.geoAzimuthalEqualArea](https://github.com/xswei/d3-geo/blob/master/README.md#geoAzimuthalEqualArea) - the azimuthal equal-area projection.
* [d3.geoAzimuthalEquidistant](https://github.com/xswei/d3-geo/blob/master/README.md#geoAzimuthalEquidistant) - the azimuthal equidistant projection.
* [d3.geoConicConformal](https://github.com/xswei/d3-geo/blob/master/README.md#geoConicConformal) - the conic conformal projection.
* [d3.geoConicEqualArea](https://github.com/xswei/d3-geo/blob/master/README.md#geoConicEqualArea) - the conic equal-area (Albers) projection.
* [d3.geoConicEquidistant](https://github.com/xswei/d3-geo/blob/master/README.md#geoConicEquidistant) - the conic equidistant projection.
* [*conic*.parallels](https://github.com/xswei/d3-geo/blob/master/README.md#conic_parallels) - set the two standard parallels.
* [d3.geoEquirectangular](https://github.com/xswei/d3-geo/blob/master/README.md#geoEquirectangular) - the equirectangular (plate carreé) projection.
* [d3.geoGnomonic](https://github.com/xswei/d3-geo/blob/master/README.md#geoGnomonic) - the gnomonic projection.
* [d3.geoMercator](https://github.com/xswei/d3-geo/blob/master/README.md#geoMercator) - the spherical Mercator projection.
* [d3.geoOrthographic](https://github.com/xswei/d3-geo/blob/master/README.md#geoOrthographic) - the azimuthal orthographic projection.
* [d3.geoStereographic](https://github.com/xswei/d3-geo/blob/master/README.md#geoStereographic) - the azimuthal stereographic projection.
* [d3.geoTransverseMercator](https://github.com/xswei/d3-geo/blob/master/README.md#geoTransverseMercator) - the transverse spherical Mercator projection.
* [*project*](https://github.com/xswei/d3-geo/blob/master/README.md#_project) - project the specified point from the sphere to the plane.
* [*project*.invert](https://github.com/xswei/d3-geo/blob/master/README.md#project_invert) - unproject the specified point from the plane to the sphere.
* [d3.geoProjection](https://github.com/xswei/d3-geo/blob/master/README.md#geoProjection) - create a custom projection.
* [d3.geoProjectionMutator](https://github.com/xswei/d3-geo/blob/master/README.md#geoProjectionMutator) - create a custom configurable projection.
* [d3.geoAzimuthalEqualAreaRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoAzimuthalEqualAreaRaw) - the raw azimuthal equal-area projection.
* [d3.geoAzimuthalEquidistantRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoAzimuthalEquidistantRaw) - the raw azimuthal equidistant projection.
* [d3.geoConicConformalRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoConicConformalRaw) - the raw conic conformal projection.
* [d3.geoConicEqualAreaRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoConicEqualAreaRaw) - the raw conic equal-area (Albers) projection.
* [d3.geoConicEquidistantRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoConicEquidistantRaw) - the raw conic equidistant projection.
* [d3.geoEquirectangularRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoEquirectangularRaw) - the raw equirectangular (plate carreé) projection.
* [d3.geoGnomonicRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoGnomonicRaw) - the raw gnomonic projection.
* [d3.geoMercatorRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoMercatorRaw) - the raw Mercator projection.
* [d3.geoOrthographicRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoOrthographicRaw) - the raw azimuthal orthographic projection.
* [d3.geoStereographicRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoStereographicRaw) - the raw azimuthal stereographic projection.
* [d3.geoTransverseMercatorRaw](https://github.com/xswei/d3-geo/blob/master/README.md#geoTransverseMercatorRaw) - the raw transverse spherical Mercator projection.

### [Spherical Math](https://github.com/xswei/d3-geo/blob/master/README.md#spherical-math)

* [d3.geoArea](https://github.com/xswei/d3-geo/blob/master/README.md#geoArea) - 根据给定的地理特征计算球面面积.
* [d3.geoBounds](https://github.com/xswei/d3-geo/blob/master/README.md#geoBounds) - 根据指定的地理特征计算包裹框(经纬度).
* [d3.geoCentroid](https://github.com/xswei/d3-geo/blob/master/README.md#geoCentroid) - 根据给定的地理特征计算球面中心.
* [d3.geoContains](https://github.com/xswei/d3-geo/blob/master/README.md#geoContains) - 测试一个点是否在给定的地理特征轮廓内部.
* [d3.geoDistance](https://github.com/xswei/d3-geo/blob/master/README.md#geoDistance) - 计算两个点之间的大圆距离.
* [d3.geoLength](https://github.com/xswei/d3-geo/blob/master/README.md#geoLength) - 计算一条线的长度或者多边形的周长.
* [d3.geoInterpolate](https://github.com/xswei/d3-geo/blob/master/README.md#geoInterpolate) - 在两个点之间沿着大圆进行插值.
* [d3.geoRotation](https://github.com/xswei/d3-geo/blob/master/README.md#geoRotation) - 根据指定的角度创建一个旋转函数.
* [*rotation*](https://github.com/xswei/d3-geo/blob/master/README.md#_rotation) - 沿着指定的球面对指定点进行旋转.
* [*rotation*.invert](https://github.com/xswei/d3-geo/blob/master/README.md#rotation_invert) - 计算某个点在旋转之前的点.

### [Spherical Shapes](https://github.com/xswei/d3-geo/blob/master/README.md#spherical-shapes)

* [d3.geoCircle](https://github.com/xswei/d3-geo/blob/master/README.md#geoCircle) - 创建一个圆生成器.
* [*circle*](https://github.com/xswei/d3-geo/blob/master/README.md#_circle) - 以分段的多边形的形式生成一个圆.
* [*circle*.center](https://github.com/xswei/d3-geo/blob/master/README.md#circle_center) - 以经纬度的方式指定圆心.
* [*circle*.radius](https://github.com/xswei/d3-geo/blob/master/README.md#circle_radius) - 以度为单位指定圆的角半径.
* [*circle*.precision](https://github.com/xswei/d3-geo/blob/master/README.md#circle_precision) - 指定分段圆的精度.
* [d3.geoGraticule](https://github.com/xswei/d3-geo/blob/master/README.md#geoGraticule) - create a graticule generator.
* [*graticule*](https://github.com/xswei/d3-geo/blob/master/README.md#_graticule) - generate a MultiLineString of meridians and parallels.
* [*graticule*.lines](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_lines) - generate an array of LineStrings of meridians and parallels.
* [*graticule*.outline](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_outline) - generate a Polygon of the graticule’s extent.
* [*graticule*.extent](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_extent) - get or set the major & minor extents.
* [*graticule*.extentMajor](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_extentMajor) - get or set the major extent.
* [*graticule*.extentMinor](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_extentMinor) - get or set the minor extent.
* [*graticule*.step](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_step) - get or set the major & minor step intervals.
* [*graticule*.stepMajor](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_stepMajor) - get or set the major step intervals.
* [*graticule*.stepMinor](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_stepMinor) - get or set the minor step intervals.
* [*graticule*.precision](https://github.com/xswei/d3-geo/blob/master/README.md#graticule_precision) - get or set the latitudinal precision.
* [d3.geoGraticule10](https://github.com/xswei/d3-geo/blob/master/README.md#geoGraticule10) - generate the default 10° global graticule.

#### [Streams](https://github.com/xswei/d3-geo/blob/master/README.md#streams)

* [d3.geoStream](https://github.com/xswei/d3-geo/blob/master/README.md#geoStream) - convert a GeoJSON object to a geometry stream.
* [*stream*.point](https://github.com/xswei/d3-geo/blob/master/README.md#stream_point) - indicates a point with the specified coordinates.
* [*stream*.lineStart](https://github.com/xswei/d3-geo/blob/master/README.md#stream_lineStart) - indicates the start of a line or ring.
* [*stream*.lineEnd](https://github.com/xswei/d3-geo/blob/master/README.md#stream_lineEnd) - indicates the end of a line or ring.
* [*stream*.polygonStart](https://github.com/xswei/d3-geo/blob/master/README.md#stream_polygonStart) - indicates the start of a polygon.
* [*stream*.polygonEnd](https://github.com/xswei/d3-geo/blob/master/README.md#stream_polygonEnd) - indicates the end of a polygon.
* [*stream*.sphere](https://github.com/xswei/d3-geo/blob/master/README.md#stream_sphere) - indicates the sphere.

### [Transforms](https://github.com/xswei/d3-geo/blob/master/README.md#transforms)

* [d3.geoIdentity](https://github.com/xswei/d3-geo/blob/master/README.md#geoIdentity) - scale, translate or clip planar geometry.
* [*identity*.reflectX](https://github.com/xswei/d3-geo/blob/master/README.md#identity_reflectX) - reflect the *x*-dimension.
* [*identity*.reflectY](https://github.com/xswei/d3-geo/blob/master/README.md#identity_reflectY) - reflect the *y*-dimension.
* [d3.geoTransform](https://github.com/xswei/d3-geo/blob/master/README.md#geoTransform) - define a custom geometry transform.

## [Hierarchies (d3-hierarchy)](https://github.com/xswei/d3-hierarchy)

对层次数据进行可视化的一些布局算法.

* [d3.hierarchy](https://github.com/xswei/d3-hierarchy/blob/master/README.md#hierarchy) - 从给定的层次结构数据构造一个根节点并为各个节点指定深度等属性.
* [*node*.ancestors](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_ancestors) - 从当前节点开始返回其祖先节点数组.
* [*node*.descendants](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_descendants) - 从当前节点开始返回其后代节点数组.
* [*node*.leaves](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_leaves) - 返回当前节点为根节点的子树的叶节点.
* [*node*.path](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_path) - 返回从当前节点到指定目标节点的最短路径.
* [*node*.links](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_links) - 返回当前节点所在子树的所有边.
* [*node*.sum](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_sum) - 评估和汇总定量值.
* [*node*.sort](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_sort) - 排序所有的后代兄弟节点.
* [*node*.count](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_count) - 统计叶节点的个数.
* [*node*.each](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_each) - 广度优先遍历当前子树.
* [*node*.eachAfter](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_eachAfter) - 后续遍历当前子树.
* [*node*.eachBefore](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_eachBefore) - 前序遍历当前子树.
* [*node*.copy](https://github.com/xswei/d3-hierarchy/blob/master/README.md#node_copy) - 拷贝一个当前节点为根节点的子树的副本.
* [d3.stratify](https://github.com/xswei/d3-hierarchy/blob/master/README.md#stratify) - 创建一个新的分层操作.
* [*stratify*](https://github.com/xswei/d3-hierarchy/blob/master/README.md#_stratify) - 根据扁平数据创建一个分层数据.
* [*stratify*.id](https://github.com/xswei/d3-hierarchy/blob/master/README.md#stratify_id) - 设置节点 `id` 访问器.
* [*stratify*.parentId](https://github.com/xswei/d3-hierarchy/blob/master/README.md#stratify_parentId) - 设置父节点 `id` 访问器.
* [d3.cluster](https://github.com/xswei/d3-hierarchy/blob/master/README.md#cluster) - 创建一个新的集群(系统树图)布局.
* [*cluster*](https://github.com/xswei/d3-hierarchy/blob/master/README.md#_cluster) - 将指定的数据布局为系统树图.
* [*cluster*.size](https://github.com/xswei/d3-hierarchy/blob/master/README.md#cluster_size) - 设置布局尺寸.
* [*cluster*.nodeSize](https://github.com/xswei/d3-hierarchy/blob/master/README.md#cluster_nodeSize) - 设计节点尺寸.
* [*cluster*.separation](https://github.com/xswei/d3-hierarchy/blob/master/README.md#cluster_separation) - 设置两个叶节点之间的间距.
* [d3.tree](https://github.com/xswei/d3-hierarchy/blob/master/README.md#tree) - 创建一个新的整齐(同深度节点对齐)的树布局.
* [*tree*](https://github.com/xswei/d3-hierarchy/blob/master/README.md#_tree) - 将指定的层次数据布局为整齐的树布局.
* [*tree*.size](https://github.com/xswei/d3-hierarchy/blob/master/README.md#tree_size) - 设置布局尺寸.
* [*tree*.nodeSize](https://github.com/xswei/d3-hierarchy/blob/master/README.md#tree_nodeSize) - 设置节点尺寸.
* [*tree*.separation](https://github.com/xswei/d3-hierarchy/blob/master/README.md#tree_separation) - 设置两个相邻的节点之间的间距.
* [d3.treemap](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap) - 创建一个矩阵树图布局.
* [*treemap*](https://github.com/xswei/d3-hierarchy/blob/master/README.md#_treemap) - 将层次数据布局为矩阵树图.
* [*treemap*.tile](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_tile) - 设置矩阵树图布局的填铺方法.
* [*treemap*.size](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_size) - 设置布局尺寸.
* [*treemap*.round](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_round) - 设置输出坐标是否取整.
* [*treemap*.padding](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_padding) - 设置间隔参数.
* [*treemap*.paddingInner](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_paddingInner) - 设置同级节点之间的间隔.
* [*treemap*.paddingOuter](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_paddingOuter) - 设置父节点和子节点之间的间距.
* [*treemap*.paddingTop](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_paddingTop) - 设置父节点和子节点之间的顶部间距.
* [*treemap*.paddingRight](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_paddingRight) - 设置父节点和子节点之间的右侧间距.
* [*treemap*.paddingBottom](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_paddingBottom) - 设置父节点和子节点之间的底部间距.
* [*treemap*.paddingLeft](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemap_paddingLeft) - 设置父节点和子节点之间的左侧间距.
* [d3.treemapBinary](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemapBinary) - 平铺为平衡二叉树.
* [d3.treemapDice](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemapDice) - 以水平划分的形式平铺.
* [d3.treemapSlice](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemapSlice) - 以垂直划分的形式平铺.
* [d3.treemapSliceDice](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemapSliceDice) - 在 `slice` 和 `dice` 之间切换.
* [d3.treemapSquarify](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemapSquarify) - tile using squarified rows per Bruls *et. al.*
* [d3.treemapResquarify](https://github.com/xswei/d3-hierarchy/blob/master/README.md#treemapResquarify) - 与 ` d3.treemapSquarify` 类似, 但是更新时更稳定.
* [*squarify*.ratio](https://github.com/xswei/d3-hierarchy/blob/master/README.md#squarify_ratio) - 设置期望的矩形纵横比.
* [d3.partition](https://github.com/xswei/d3-hierarchy/blob/master/README.md#partition) - 创建一个新的分区布局.
* [*partition*](https://github.com/xswei/d3-hierarchy/blob/master/README.md#_partition) - 将层次数据布局为分区图(属性计算).
* [*partition*.size](https://github.com/xswei/d3-hierarchy/blob/master/README.md#partition_size) - 设置分区图的尺寸.
* [*partition*.round](https://github.com/xswei/d3-hierarchy/blob/master/README.md#partition_round) - 设置输出坐标是否取整.
* [*partition*.padding](https://github.com/xswei/d3-hierarchy/blob/master/README.md#partition_padding) - 设置间隙.
* [d3.pack](https://github.com/xswei/d3-hierarchy/blob/master/README.md#pack) - 创建一个新的圆形打包图.
* [*pack*](https://github.com/xswei/d3-hierarchy/blob/master/README.md#_pack) - 为指定的层次数据计算绘制打包图需要的属性.
* [*pack*.radius](https://github.com/xswei/d3-hierarchy/blob/master/README.md#pack_radius) - 设置半径访问器.
* [*pack*.size](https://github.com/xswei/d3-hierarchy/blob/master/README.md#pack_size) - 设置布局尺寸.
* [*pack*.padding](https://github.com/xswei/d3-hierarchy/blob/master/README.md#pack_padding) - 设置间隙.
* [d3.packSiblings](https://github.com/xswei/d3-hierarchy/blob/master/README.md#packSiblings) - 将一组圆进行打包.
* [d3.packEnclose](https://github.com/xswei/d3-hierarchy/blob/master/README.md#packEnclose) - 计算指定圆数组的最小包裹圆.

## [Interpolators (d3-interpolate)](https://github.com/xswei/d3-interpolate)

对数值、颜色、字符串、数组、对象等进行插值

* [d3.interpolate](https://github.com/xswei/d3-interpolate#interpolate) - 生成一个任意数值的插值器.
* [d3.interpolateArray](https://github.com/xswei/d3-interpolate#interpolateArray) - 生成一个数组插值器.
* [d3.interpolateDate](https://github.com/xswei/d3-interpolate#interpolateDate) - 生成一个时间类型插值器.
* [d3.interpolateNumber](https://github.com/xswei/d3-interpolate#interpolateNumber) - 生成一个时间类型插值器.
* [d3.interpolateObject](https://github.com/xswei/d3-interpolate#interpolateObject) - 生成一个对象类型插值器.
* [d3.interpolateRound](https://github.com/xswei/d3-interpolate#interpolateRound) - 生成一个数值类型插值器.
* [d3.interpolateString](https://github.com/xswei/d3-interpolate#interpolateString) - 生成一个字符串类型插值器.
* [d3.interpolateTransformCss](https://github.com/xswei/d3-interpolate#interpolateTransformCss) - 生成一个 `2D CSS` 样式过渡插值器.
* [d3.interpolateTransformSvg](https://github.com/xswei/d3-interpolate#interpolateTransformSvg) - 生成一个 `2D SVG` 过渡插值器.
* [d3.interpolateZoom](https://github.com/xswei/d3-interpolate#interpolateZoom) - 在两个缩放视图之间过渡的插值器.
* [d3.interpolateRgb](https://github.com/xswei/d3-interpolate#interpolateRgb) - 生成一个 `RGB` 类型插值器.
* [d3.interpolateRgbBasis](https://github.com/xswei/d3-interpolate#interpolateRgbBasis) - 根据一组颜色返回一个 *B*- 样条插值器.
* [d3.interpolateRgbBasisClosed](https://github.com/xswei/d3-interpolate#interpolateRgbBasisClosed) - 根据一组颜色返回一个 *B*- 样条插值器.
* [d3.interpolateHsl](https://github.com/xswei/d3-interpolate#interpolateHsl) - 生成一个 `Hsl` 类型插值器.
* [d3.interpolateHslLong](https://github.com/xswei/d3-interpolate#interpolateHslLong) - 生成一个 `Hsl` 类型插值器(反向模式).
* [d3.interpolateLab](https://github.com/xswei/d3-interpolate#interpolateLab) - 生成一个 `Lab` 类型插值器.
* [d3.interpolateHcl](https://github.com/xswei/d3-interpolate#interpolateHcl) - 生成一个 `Hcl` 类型插值器.
* [d3.interpolateHclLong](https://github.com/xswei/d3-interpolate#interpolateHclLong) - 生成一个 `Hcl` 类型插值器(反向模式).
* [d3.interpolateCubehelix](https://github.com/xswei/d3-interpolate#interpolateCubehelix) - 生成一个 Cubehelix 类型插值器.
* [d3.interpolateCubehelixLong](https://github.com/xswei/d3-interpolate#interpolateCubehelixLong) - 生成一个 `Cubehelix` 类型插值器(反向模式).
* [*interpolate*.gamma](https://github.com/xswei/d3-interpolate#interpolate_gamma) - 应用 `gamma` 修正.
* [d3.interpolateBasis](https://github.com/xswei/d3-interpolate#interpolateBasis) - 根据一组数值返回一个 *B*- 样条插值器.
* [d3.interpolateBasisClosed](https://github.com/xswei/d3-interpolate#interpolateBasisClosed) - 根据一组数值返回一个 *B*- 样条插值器.
* [d3.piecewise](https://github.com/xswei/d3-interpolate/blob/master/README.md#piecewise) - 根据指定的 `values` 生成一个分段插值器.
* [d3.quantize](https://github.com/xswei/d3-interpolate#quantize) - 插值器生成一组均匀采样.

## [Paths (d3-path)](https://github.com/xswei/d3-path)

将 `Canvas` 路径命令序列化为 `SVG` 路径字符串。

* [d3.path](https://github.com/xswei/d3-path/blob/master/README.md#path) - 创建一个新的路径序列化.
* [*path*.moveTo](https://github.com/xswei/d3-path/blob/master/README.md#path_moveTo) - 移动到指定的点.
* [*path*.closePath](https://github.com/xswei/d3-path/blob/master/README.md#path_closePath) - 闭合当前子路径.
* [*path*.lineTo](https://github.com/xswei/d3-path/blob/master/README.md#path_lineTo) - 绘制直线.
* [*path*.quadraticCurveTo](https://github.com/xswei/d3-path/blob/master/README.md#path_quadraticCurveTo) - 绘制二次 `Bézier` 曲线.
* [*path*.bezierCurveTo](https://github.com/xswei/d3-path/blob/master/README.md#path_bezierCurveTo) - 绘制三次 `Bézier` 曲线.
* [*path*.arcTo](https://github.com/xswei/d3-path/blob/master/README.md#path_arcTo) - 绘制弧线段.
* [*path*.arc](https://github.com/xswei/d3-path/blob/master/README.md#path_arc) - 绘制弧线段.
* [*path*.rect](https://github.com/xswei/d3-path/blob/master/README.md#path_rect) - 绘制矩形.
* [*path*.toString](https://github.com/xswei/d3-path/blob/master/README.md#path_toString) - 序列化为 `SVG` 路径字符串.

## [Polygons (d3-polygon)](https://github.com/xswei/d3-polygon)

二维多边形的几何操作.

* [d3.polygonArea](https://github.com/xswei/d3-polygon/blob/master/README.md#polygonArea) - 计算指定多边形的面积.
* [d3.polygonCentroid](https://github.com/xswei/d3-polygon/blob/master/README.md#polygonCentroid) - 计算指定多边形的几何中心.
* [d3.polygonHull](https://github.com/xswei/d3-polygon/blob/master/README.md#polygonHull) - 计算指定一系列点的凸包.
* [d3.polygonContains](https://github.com/xswei/d3-polygon/blob/master/README.md#polygonContains) - 测试某个点是否在某个多边形内部.
* [d3.polygonLength](https://github.com/xswei/d3-polygon/blob/master/README.md#polygonLength) - 计算指定多边形的周长.

## [Quadtrees (d3-quadtree)](https://github.com/xswei/d3-quadtree)

四叉树, 二维空间递归细分.

* [d3.quadtree](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree) - 创建一个新的空的四叉树.
* [*quadtree*.x](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_x) - 设置 *x* 访问器.
* [*quadtree*.y](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_y) - 设置 *y* 访问器.
* [*quadtree*.add](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_add) - 向四叉树中添加数据.
* [*quadtree*.addAll](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_addAll) - 向四叉树中添加数据数组.
* [*quadtree*.remove](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_remove) - 从四叉树中移除数据.
* [*quadtree*.removeAll](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_removeAll) - 从四叉树中移除一组数据.
* [*quadtree*.copy](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_copy) - 创建一个四叉树的拷贝.
* [*quadtree*.root](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_root) - 获取四叉树的根节点.
* [*quadtree*.data](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_data) - 从四叉树中取回数据.
* [*quadtree*.size](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_size) - 计算四叉树中的数据个数.
* [*quadtree*.find](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_find) - 从四叉树中快速查找最接近的数据.
* [*quadtree*.visit](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_visit) - 前序遍历四叉树中的所有节点.
* [*quadtree*.visitAfter](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_visitAfter) - 后序遍历四叉树中的所有节点.
* [*quadtree*.cover](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_cover) - 扩展四叉树直到覆盖指定的点.
* [*quadtree*.extent](https://github.com/xswei/d3-quadtree/blob/master/README.md#quadtree_extent) - 扩展四叉树以覆盖指定的区间.

## [Random Numbers (d3-random)](https://github.com/xswei/d3-random)

基于多种多样的分布模型生成随机数.

* [d3.randomUniform](https://github.com/xswei/d3-random/blob/master/README.md#randomUniform) - 一般分布.
* [d3.randomNormal](https://github.com/xswei/d3-random/blob/master/README.md#randomNormal) - 标准高斯分布.
* [d3.randomLogNormal](https://github.com/xswei/d3-random/blob/master/README.md#randomLogNormal) - 对数分布.
* [d3.randomBates](https://github.com/xswei/d3-random/blob/master/README.md#randomBates) - 贝茨分布.
* [d3.randomIrwinHall](https://github.com/xswei/d3-random/blob/master/README.md#randomIrwinHall) - `Irwin–Hall` 分布.
* [d3.randomExponential](https://github.com/xswei/d3-random/blob/master/README.md#randomExponential) - 指数分布.
* [*random*.source](https://github.com/xswei/d3-random/blob/master/README.md#random_source) - 设置随机数生成源.

## [Scales (d3-scale)](https://github.com/xswei/d3-scale)

将抽象数据映射到可视化表示的编码.

### [Continuous Scales](https://github.com/xswei/d3-scale/blob/master/README.md#continuous-scales)

将一个连续的，定量的输入映射到连续的输出区间.

* [*continuous*](https://github.com/xswei/d3-scale/blob/master/README.md#_continuous) - 根据给定的输入值计算对应的输出值.
* [*continuous*.invert](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_invert) - 根据输出值计算对应的输入值.
* [*continuous*.domain](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_domain) - 设置输入范围.
* [*continuous*.range](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_range) - 设置输出范围.
* [*continuous*.rangeRound](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_rangeRound) - 设置输出范围并且启用四舍五入.
* [*continuous*.clamp](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_clamp) - 启用输入或输出的范围限制(输入输出限制在定义的范围之内).
* [*continuous*.interpolate](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_interpolate) - 设置输出插值器.
* [*continuous*.ticks](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_ticks) - 从输入范围中提取具有代表意义的值.
* [*continuous*.tickFormat](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_tickFormat) - 将刻度格式化为人类友好的格式.
* [*continuous*.nice](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_nice) - 将输入范围扩展到漂亮的整数.
* [*continuous*.copy](https://github.com/xswei/d3-scale/blob/master/README.md#continuous_copy) - 创建一个当前比例尺的副本.
* [d3.scaleLinear](https://github.com/xswei/d3-scale/blob/master/README.md#scaleLinear) - 创建一个定量的线性比例尺.
* [d3.scalePow](https://github.com/xswei/d3-scale/blob/master/README.md#scalePow) - 创建一个定量的指数比例尺.
* [*pow*](https://github.com/xswei/d3-scale/blob/master/README.md#_pow) - 根据输入值计算对应的输出值.
* [*pow*.invert](https://github.com/xswei/d3-scale/blob/master/README.md#pow_invert) - 根据输出值计算对应的输入值.
* [*pow*.exponent](https://github.com/xswei/d3-scale/blob/master/README.md#pow_exponent) - 设置指数.
* [*pow*.domain](https://github.com/xswei/d3-scale/blob/master/README.md#pow_domain) - 设置输入范围.
* [*pow*.range](https://github.com/xswei/d3-scale/blob/master/README.md#pow_range) - 设置输出范围.
* [*pow*.rangeRound](https://github.com/xswei/d3-scale/blob/master/README.md#pow_rangeRound) - 设置输出范围并且启用四舍五入.
* [*pow*.clamp](https://github.com/xswei/d3-scale/blob/master/README.md#pow_clamp) - 启用输入或输出的范围限制.
* [*pow*.interpolate](https://github.com/xswei/d3-scale/blob/master/README.md#pow_interpolate) - 设置输出插值器.
* [*pow*.ticks](https://github.com/xswei/d3-scale/blob/master/README.md#pow_ticks) - 从输入范围中提取具有代表意义的值(作为刻度).
* [*pow*.tickFormat](https://github.com/xswei/d3-scale/blob/master/README.md#pow_tickFormat) - 将刻度格式化为人类友好的格式.
* [*pow*.nice](https://github.com/xswei/d3-scale/blob/master/README.md#pow_nice) - 将输入范围扩展到漂亮的整数.
* [*pow*.copy](https://github.com/xswei/d3-scale/blob/master/README.md#pow_copy) - 创建一个当前比例尺的副本.
* [d3.scaleSqrt](https://github.com/xswei/d3-scale/blob/master/README.md#scaleSqrt) - 创建一个指数为 `0.5` 的指数比例尺.
* [d3.scaleLog](https://github.com/xswei/d3-scale/blob/master/README.md#scaleLog) - 创建一个对数比例尺.
* [*log*](https://github.com/xswei/d3-scale/blob/master/README.md#_log) - 根据输入值计算对应的输出值.
* [*log*.invert](https://github.com/xswei/d3-scale/blob/master/README.md#log_invert) - 根据输出值计算对应的输入值.
* [*log*.base](https://github.com/xswei/d3-scale/blob/master/README.md#log_base) - 设置对数的基.
* [*log*.domain](https://github.com/xswei/d3-scale/blob/master/README.md#log_domain) - 设置输入范围.
* [*log*.range](https://github.com/xswei/d3-scale/blob/master/README.md#log_range) - 设置输出范围.
* [*log*.rangeRound](https://github.com/xswei/d3-scale/blob/master/README.md#log_rangeRound) - 设置输出范围并且启用四舍五入.
* [*log*.clamp](https://github.com/xswei/d3-scale/blob/master/README.md#log_clamp) - 启用输入或输出的范围限制.
* [*log*.interpolate](https://github.com/xswei/d3-scale/blob/master/README.md#log_interpolate) - 设置输出插值器.
* [*log*.ticks](https://github.com/xswei/d3-scale/blob/master/README.md#log_ticks) - 从输入范围中提取具有代表意义的值(作为刻度).
* [*log*.tickFormat](https://github.com/xswei/d3-scale/blob/master/README.md#log_tickFormat) - 将刻度格式化为人类友好的格式.
* [*log*.nice](https://github.com/xswei/d3-scale/blob/master/README.md#log_nice) - 将输入范围扩展到漂亮的整数.
* [*log*.copy](https://github.com/xswei/d3-scale/blob/master/README.md#log_copy) - 创建一个当前比例尺的副本.
* [d3.scaleIdentity](https://github.com/xswei/d3-scale/blob/master/README.md#identity) - 创建一个定量的恒等比例尺.
* [d3.scaleTime](https://github.com/xswei/d3-scale/blob/master/README.md#scaleTime) - 创建一个线性的时间比例尺.
* [*time*](https://github.com/xswei/d3-scale/blob/master/README.md#_time) - 根据输入值计算对应的输出值.
* [*time*.invert](https://github.com/xswei/d3-scale/blob/master/README.md#time_invert) - 根据输出值计算对应的输入值.
* [*time*.domain](https://github.com/xswei/d3-scale/blob/master/README.md#time_domain) - 设置输入范围.
* [*time*.range](https://github.com/xswei/d3-scale/blob/master/README.md#time_range) - 设置输出范围.
* [*time*.rangeRound](https://github.com/xswei/d3-scale/blob/master/README.md#time_rangeRound) - 设置输出范围并且启用四舍五入.
* [*time*.clamp](https://github.com/xswei/d3-scale/blob/master/README.md#time_clamp) - 启用输入或输出的范围限制.
* [*time*.interpolate](https://github.com/xswei/d3-scale/blob/master/README.md#time_interpolate) - 设置输出插值器.
* [*time*.ticks](https://github.com/xswei/d3-scale/blob/master/README.md#time_ticks) - 从输入范围中提取具有代表意义的值(作为刻度).
* [*time*.tickFormat](https://github.com/xswei/d3-scale/blob/master/README.md#time_tickFormat) - 将刻度格式化为人类友好的格式.
* [*time*.nice](https://github.com/xswei/d3-scale/blob/master/README.md#time_nice) - 扩展输入范围到一个友好的时间.
* [*time*.copy](https://github.com/xswei/d3-scale/blob/master/README.md#time_copy) - 创建一个当前比例尺的副本.
* [d3.scaleUtc](https://github.com/xswei/d3-scale/blob/master/README.md#scaleUtc) - 创建一个 `UTC` 线性比例尺.

### [Sequential Scales](https://github.com/xswei/d3-scale/blob/master/README.md#sequential-scales)

Map a continuous, quantitative domain to a continuous, fixed interpolator.

* [d3.scaleSequential](https://github.com/d3/d3-scale/blob/master/README.md#scaleSequential) - create a sequential scale.
* [*sequential*.interpolator](https://github.com/d3/d3-scale/blob/master/README.md#sequential_interpolator) - set the scale’s output interpolator.

### [Diverging Scales](https://github.com/d3/d3-scale/blob/master/README.md#diverging-scales)

Map a continuous, quantitative domain to a continuous, fixed interpolator.

* [d3.scaleDiverging](https://github.com/d3/d3-scale/blob/master/README.md#scaleDiverging) - create a diverging scale.
* [*diverging*.interpolator](https://github.com/d3/d3-scale/blob/master/README.md#diverging_interpolator) - set the scale’s output interpolator.

### [Quantize Scales](https://github.com/xswei/d3-scale/blob/master/README.md#quantize-scales)

Map a continuous, quantitative domain to a discrete range.

* [d3.scaleQuantize](https://github.com/xswei/d3-scale/blob/master/README.md#scaleQuantize) - create a uniform quantizing linear scale.
* [*quantize*](https://github.com/xswei/d3-scale/blob/master/README.md#_quantize) - 根据输入值计算对应的输出值.
* [*quantize*.invertExtent](https://github.com/xswei/d3-scale/blob/master/README.md#quantize_invertExtent) - compute the domain values corresponding to a given range value.
* [*quantize*.domain](https://github.com/xswei/d3-scale/blob/master/README.md#quantize_domain) - 设置输入范围.
* [*quantize*.range](https://github.com/xswei/d3-scale/blob/master/README.md#quantize_range) - 设置输出范围.
* [*quantize*.nice](https://github.com/xswei/d3-scale/blob/master/README.md#quantize_nice) - 将输入范围扩展到漂亮的整数.
* [*quantize*.ticks](https://github.com/xswei/d3-scale/blob/master/README.md#quantize_ticks) - 从输入范围中提取具有代表意义的值(作为刻度).
* [*quantize*.tickFormat](https://github.com/xswei/d3-scale/blob/master/README.md#quantize_tickFormat) - 将刻度格式化为人类友好的格式.
* [*quantize*.copy](https://github.com/xswei/d3-scale/blob/master/README.md#quantize_copy) - 创建一个当前比例尺的副本.
* [d3.scaleQuantile](https://github.com/xswei/d3-scale/blob/master/README.md#scaleQuantile) - create a quantile quantizing linear scale.
* [*quantile*](https://github.com/xswei/d3-scale/blob/master/README.md#_quantile) - 根据输入值计算对应的输出值.
* [*quantile*.invertExtent](https://github.com/xswei/d3-scale/blob/master/README.md#quantile_invertExtent) - compute the domain values corresponding to a given range value.
* [*quantile*.domain](https://github.com/xswei/d3-scale/blob/master/README.md#quantile_domain) - 设置输入范围.
* [*quantile*.range](https://github.com/xswei/d3-scale/blob/master/README.md#quantile_range) - 设置输出范围.
* [*quantile*.quantiles](https://github.com/xswei/d3-scale/blob/master/README.md#quantile_quantiles) - get the quantile thresholds.
* [*quantile*.copy](https://github.com/xswei/d3-scale/blob/master/README.md#quantile_copy) - 创建一个当前比例尺的副本.
* [d3.scaleThreshold](https://github.com/xswei/d3-scale/blob/master/README.md#scaleThreshold) - create an arbitrary quantizing linear scale.
* [*threshold*](https://github.com/xswei/d3-scale/blob/master/README.md#_threshold) - 根据输入值计算对应的输出值.
* [*threshold*.invertExtent](https://github.com/xswei/d3-scale/blob/master/README.md#threshold_invertExtent) - compute the domain values corresponding to a given range value.
* [*threshold*.domain](https://github.com/xswei/d3-scale/blob/master/README.md#threshold_domain) - 设置输入范围.
* [*threshold*.range](https://github.com/xswei/d3-scale/blob/master/README.md#threshold_range) - 设置输出范围.
* [*threshold*.copy](https://github.com/xswei/d3-scale/blob/master/README.md#threshold_copy) - 创建一个当前比例尺的副本.

### [