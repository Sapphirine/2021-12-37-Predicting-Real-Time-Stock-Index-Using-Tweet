function connection(nodes, edges) {
	var width = 1440;
	var height = 1080;


	var svg = d3.select("body")
				.append("svg")
				.attr(/* TO FINISH */"height", height)
				.attr(/* TO FINISH */"width", width);

	var force = d3.layout.force()
			.nodes(nodes)
			.links(edges)
			.size([width,height])
			.linkDistance(300)
			.charge(-200);

	force.start();

	console.log(nodes);
	console.log(edges);


	var svg_edges = svg.selectAll("line")
						.data(/* TO FINISH */edges)
						.enter()
						.append(/* TO FINISH */"line")
						.style("stroke","#ccc")
						.style("stroke-width",1);

	var color = d3.scale.category20();


	var svg_nodes = svg.selectAll("circle")
						.data(/* TO FINISH */nodes)
						.enter()
						.append(/* TO FINISH */"circle")
						.attr("r",20)
						.style("fill", /* TO FINISH */function (d){
							return color(d.index)
						})
						.call(force.drag);


	var svg_texts = svg.selectAll("text")
						.data(nodes)
						.enter()
						.append("text")
						.style("fill", "black")
						.attr("dx", 20)
						.attr("dy", 8)
						.text( /* TO FINISH */ function(d){
							return d.node;
						});


	force.on("tick", function(){
		 svg_edges.attr("x1", /* TO FINISH */function(d){
			 return d.source.x;
		 })
				.attr("y1", /* TO FINISH */function(d){
					return d.source.y;
				})
				.attr("x2", /* TO FINISH */function(d){
					return d.target.x;
				})
				.attr("y2", /* TO FINISH */function(d){
					return d.target.y;
				});

		 svg_nodes.attr("cx",function(d){ return d.x; })
				.attr("cy",function(d){ return d.y; });

		 svg_texts.attr("x", function(d){ return d.x; })
			.attr("y", function(d){ return d.y; });
		});
}
