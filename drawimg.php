<!DOCTYPE HTML>
<html>
    <head>
	<script>
function loadImages(sources, callback){
    var images = {};
    var loadedImages = 0;
    var numImages = 0;
    // get num of sources
    for (var src in sources) {
        numImages++;
    }
    for (var src in sources) {
        images[src] = new Image();
        images[src].onload = function(){
            if (++loadedImages >= numImages) {
                callback(images);
            }
        };
        images[src].src = sources[src];
    }
}
 
            window.onload = function(){
    		var canvas = document.getElementById("myCanvas");
		var context = canvas.getContext("2d");
 
		var sources = {
	        	testimg: "../images/testImg.jpg",
		        testimg2: "../images/testImg.jpg"
		};
		loadImages(sources, function(images){

<?php
$imgMap = array(1=> array("img"=>"testimg", "x"=>"500", "y"=>"200"),
	      2=> array("img"=>"testimg2", "x"=>"0", "y"=>"141"));

foreach ($imgMap as $img) {
	echo "context.drawImage(images.$img[img], $img[x], $img[y]);\n";
}

?>
		});
		};
        </script>
    </head>
    <body>
        <canvas id="myCanvas" width="600" height="600">
        </canvas>
    </body>
</html>
