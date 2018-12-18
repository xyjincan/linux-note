# selections

    var paragraphs = document.getElementsByTagName("p");
    for (var i = 0; i < paragraphs.length; i++) {
    var paragraph = paragraphs.item(i);
    paragraph.style.setProperty("color", "white", null);
    }

    d3.selectAll("p").style("color", "white");

    d3.select("body").style("background-color", "black");

## data join


    Here’s the deal. Instead of telling D3 how to do something, tell D3 what you want. You want the circle elements to correspond to data. You want one circle per datum. Instead of instructing D3 to create circles, then, tell D3 that the selection "circle" should correspond to data. This concept is called the data join:

# Dynamic properties

    For example, to randomly color paragraphs:

    d3.selectAll("p").style("color", function() {
    return "hsl(" + Math.random() * 360 + ",100%,50%)";
    });
    To alternate shades of gray for even and odd nodes:

    d3.selectAll("p").style("color", function(d, i) {
    return i % 2 ? "#fff" : "#eee";
    });

    d3.selectAll("p")
    .data([4, 8, 15, 16, 23, 42])
        .style("font-size", function(d) { return d + "px"; });

# enter-exit

    d3.select("body")
    .selectAll("p")
    .data([4, 8, 15, 16, 23, 42])
    .enter().append("p")
        .text(function(d) { return "I’m number " + d + "!"; });

    // Update…
    var p = d3.select("body")
    .selectAll("p")
    .data([4, 8, 15, 16, 23, 42])
        .text(function(d) { return d; });

    // Enter…
    p.enter().append("p")
        .text(function(d) { return d; });

    // Exit…
    p.exit().remove();



# transformation



# transitions
    For example, to fade the background of the page to black:

    d3.select("body").transition()
        .style("background-color", "black");
    
    Or, to resize circles in a symbol map with a staggered delay:

    d3.selectAll("circle").transition()
        .duration(750)
        .delay(function(d, i) { return i * 10; })
        .attr("r", function(d) { return Math.sqrt(d * scale); });


# 