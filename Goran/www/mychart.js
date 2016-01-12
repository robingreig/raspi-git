d3.json('jsondata.php', function(data) {
  nv.addGraph(function() {
    var chart = nv.models.lineWithFocusChart()
                  .margin({left: 80})  //Adjust chart margins to give the x-axis some breathing room.
                  .x(function(d) { return d[0] })   //We can modify the data accessor functions...
                  .y(function(d) { return d[1] })
                  // .color(d3.scale.category10().range())
                  // .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
                  // .showYAxis(true)        //Show the y-axis
                  // .showXAxis(true)        //Show the x-axis
                  // .useInteractiveGuideline(true)
                  ;

    chart.xAxis
        //.axisLabel('Date/Time')
        .tickFormat(function(d) { return d3.time.format('%b-%d %H:%M')(new Date(d)) })
        //.tickFormat(function(d) { return d3.time.format(d).parse(new Date(d)) })
        ;
    
    chart.x2Axis
        .axisLabel('Date/Time')
        .tickFormat(function(d) { return d3.time.format('%Y-%m-%d')(new Date(d)) })
        //.tickFormat(function(d) { return d3.time.format(d).parse(new Date(d)) })
        ;
        
    chart.yAxis
        .axisLabel('Temperature [C]')
        ;

    d3.select('#chart svg')
        .datum(data)
        .transition().duration(500)
        .call(chart);

    //TODO: Figure out a good way to do this automatically
    nv.utils.windowResize(chart.update);

    return chart;
  });
});