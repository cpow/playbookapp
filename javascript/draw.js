var posArray=new Array();
var imgIdList=[];

function updatePositions(id, img, position) {
    //alert("Got id" + id + " for image " + img + " and position left " + position.left + " and position top " + position.top);
    var data=new Array(img, position);
    console.log(data);
    posArray[id]=data;
}

function submitPlay() {
    var playname = $("#playname").val();
    var positions = "";
    var pushData=[];
    var imgCnt=0;
   // console.log(playname);
   // console.log(posArray);
   // console.log(imgIdList);
   // for (var i in posArray) {
   //     var localPos=posArray[i];
   //     var img=localPos[0];
   //     var pos=localPos[1];
   //     console.log(img);
   // }
    //playAtoms=getPlayAtoms();
    // Get details for container div so we know images location inside of play field
    playFieldHeight=$('#containment-wrapper').height();
    playFieldWidth=$('#containment-wrapper').width();
    playFieldLeft=$('#containment-wrapper').offset().left;
    playFieldTop=$('#containment-wrapper').offset().top;
    playAtoms=$('.playAtom');
    playAtoms.each(function() {
            testObj=$(this);
            imgSrc=$(this).attr('src');
            console.log("On img " + imgSrc);
            leftVal=$(this).offset().left-playFieldLeft;
            topVal=$(this).offset().top-playFieldTop;
            console.log("left val " + leftVal);
            console.log("top val " + topVal);
            pushData.push([imgSrc, leftVal, topVal]);
            imgCnt++;
    });
    
    response=$.post('submitplay', { playname: playname, 
        fieldHeight : playFieldHeight,
        fieldWidth : playFieldWidth,
        imgCnt: imgCnt, 
        positions: pushData 
        }, function (data){
            console.log(data);        
            $( "#result" ).empty().append(data);
            $.fancybox(data);
    });

}

