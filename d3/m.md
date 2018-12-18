
# d3 可视化
    Bring data to life with SVG, Canvas and HTML.

    https://github.com/d3/d3/wiki/Tutorials

    https://github.com/d3/d3/wiki/Gallery

# v3 


# v4
    api

    D3 4.0 is modular. Instead of one library, D3 is now many small libraries that are designed to work together. 

    # 对比
        in D3 3.x you might say:
        var e = d3.ease("elastic-out-in", 1.2);

        The equivalent in D3 4.0 is:
        var e = d3.easeElastic.amplitude(1.2);

# v5
    promise
    then
    D3 5+ supports recent browsers, such as Chrome, Edge, Firefox and Safari.

    # 对比
        d3.csv("file.csv", function(error, data) {
        if (error) throw error;
        console.log(data);
        });
        In v5, using promises:

        d3.csv("file.csv").then(function(data) {
        console.log(data);
        });

    # 异步，
    const data = await d3.csv("file.csv");
    console.log(data);

## d3-selection 


### Gallery

    


## Tutorials
## Plugins


	d3.tsv("data/datacanline01.tsv", function(d) {
		//逐条格式化数据
	  return d;
	}).then(function(data) {
		// 数据与图表绑定

	});
