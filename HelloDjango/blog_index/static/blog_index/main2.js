var heighttags = document.getElementById('tags').clientHeight
//var heightlist = document.getElementById('list').clientHeight
//var heightbody = heightlist + heighttags
let canvas = document.getElementById("canvas");
let canv = document.getElementById("bg-canvas");
let heibody = heighttags+500+'px!important'
//canvas.style.height = heightbody + 100;
//canv.style.height = heightbody + 100;
//console.log(heightbody + 200)
//console.log(heighttags)
//console.log(heightlist)
//console.log(heightbody)
console.log(heibody)

$(window).on('load', function () {
	$('#bg-canvas #canvas').css({'height': heibody});
//	$('#canvas').css({'height': heibody});
	console.log('22')
	console.log('height')
	console.log(heighttags)
});