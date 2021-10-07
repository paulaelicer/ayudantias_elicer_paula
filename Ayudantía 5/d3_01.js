var dataset=[4,2,7,2,3,8,6,3,5,6];
const WIDTH=880;
const HEIGHT=500;
var container=d3.select("body")
    .append("svg")
    .attr("width", WIDTH)
    .attr("height",HEIGHT)
container.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("height", function(datum,index){return datum*30})
    .attr("width", 20)
    .attr("x",function(datum,index){return index*40})
    .attr("y",function(datum,index){return (d3.max(dataset)-datum)*30})
    .attr("fill","blue");
