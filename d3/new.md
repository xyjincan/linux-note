你也可以导入多个模块然后将这些模块集合到 d3 对象中, 此时使用 Object.assign:

V5

d3.csv("file.csv").then(function(data) {
    console.log(data);
});

要注意的是不需要重新抛出错误，因为 Promise 会自动 reject，并且需要的话可以使用 promise.catch。使用 await 的话代码会更简单：
    const data = await d3.csv("file.csv");
    console.log(data);

    D3 不再提供 d3.schemeCategory20* 颜色方案。因为这些颜色有缺陷，可能会错误的暗示数据中的关系：色调相近的可能被认为是一个分组，而亮度可能被错认为是排序。作为替换，D3 5.0 使用 d3-scale-chromatic，它实现了 ColorBrewer 的方案设计，包括 categorical, diverging, sequential single-hue 和 sequential multi-hue 方案。这些颜色方案在连续式和分散式都是可用的。

    D3 提供了通过 d3-contour 实现的 marching squares(生成二维轮廓的算法) 和 density estimation(密度估计). 并且添加了两个新的 d3-selection  方法：selection.clone 用来克隆已选择的节点，d3.create 用来创建分离的元素。 Geographic projections 也支持  projection.angle，一种由 Philippe Rivière 提出的梦幻般的新的多面体投影。

    最后，D3 的 package.json 不再引用依赖的精确版本，解决了重复安装 D3 模块的问题。


V4
    d3.csv("file.csv", function(error, data) {
        if (error) throw error;
        console.log(data);
    });

D3 现在使用 Fetch API 来代替 XMLHttpRequest



v3 与 v4

    D3 4.0是由各个模块协同工作的，而不是一个单独的库。你可以按需加载独立的模块，默认的大库包含了大概30个子库。