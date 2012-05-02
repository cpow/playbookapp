var posArray=new Array();
var imgCounter=0;


function updatePositions(id, img, position) {
    //alert("Got id" + id + " for image " + img + " and position left " + position.left + " and position top " + position.top);
    var data=new Array(img, position);
    console.log(data);
    posArray[id]=data;
}

function returnPositions() {
    // Iterate through each image/position combo in the position array
    // Need to come up with some format for posting this to another page to draw image.
    for (var i in posArray) {
        var localPos=posArray[i];
        var img=localPos[0];
        var pos=localPos[1];
        alert("Img " + img + " and location " + pos.left + " " + pos.top);
    }

}

function addImg(imgSrc, dstDiv) {
    imgCounter++;
    $('#'+dstDiv).prepend('<img id="' + imgSrc + imgCounter + '" src="' + imgSrc + '" class="dragimg" />')
    $(function() {            
        $( ".dragimg" ).draggable({
            containment: "#" + dstDiv,
            //containment: "#$dstDiv",
            create: function(event, ui) {console.log(ui.position)},
            stop:   function(event, ui) {updatePositions(ui.helper.attr("id"), ui.helper.attr("src"), ui.position), console.log(posArray)}
		});
	});

}
function getPos(el) {
    // yay readability
    for (var lx=0, ly=0;
         el != null;
         lx += el.offsetLeft, ly += el.offsetTop, el = el.offsetParent);
    return {x: lx,y: ly};
}

function submitPlay() {
    var playname = $("#playname").val();
    var positions = "";
    console.log(playname);
    console.log(posArray);
    for (var i in posArray) {
        var localPos=posArray[i];
        var img=localPos[0];
        var pos=localPos[1];
        console.log(img);
    }

//    returnPositions();
    $.post('submitplay', { playname: playname , positions: posArray });
}

