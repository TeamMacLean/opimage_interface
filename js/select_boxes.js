$(function() {
    var $preview_pane = $('#preview_pane');
    var $selection = $('<div>').addClass('selection-box');
    var $image = $('#image');
    var $pos = $preview_pane.position();
    var _edit = false;

  $("#delete, #draw").on("change", function () {
    _edit = !_edit;
  });

    $preview_pane.on("click", ".final", function () {
        if (_edit) {
          $(this).remove();
          update();
        }
      }).on('mousedown', function(e) {
      if (_edit === true) return;
        var click_y = e.pageY - $pos.top, click_x = e.pageX - $pos.left;

        $selection.css({
          'top':    click_y,
          'left':   click_x,
          'width':  0,
          'height': 0
        });
        $selection.appendTo($preview_pane);

        $preview_pane.on('mousemove', function(e) {
                var move_x = e.pageX - $pos.left,
                    move_y = e.pageY - $pos.top,
                    width  = Math.abs(move_x - click_x),
                    height = Math.abs(move_y - click_y);

                $selection.css({
                    'width':  width,
                    'height': height
                });
                if (move_x < click_x) { //mouse moving left instead of right
                    $selection.css({
                        'left': click_x - width
                    });
                }
                if (move_y < click_y) { //mouse moving up instead of down
                    $selection.css({
                        'top': click_y - height
                    });
                }
        }).on('mouseup', function(e) {
            $preview_pane.off('mousemove');
            // $selection.remove();
        });
    });

  $("#add").on('click', function (e) {
      var $text = $("#title").val().replace(/^s+|s+$/,'');
      if ($text.length && $($selection,$preview_pane).length) {
        clonerect($selection, $text);
        $selection.remove();
        update();
        $("#title").val("");
      }
    });

  //$("#set").on('click', function () {
  //  var cache = new Image();
  //  cache.onload = function () {
  //    $image.attr("src", cache.src);
  //    $preview_pane.css({
  //      width: $image.width(),
  //      height: $image.height()
  //    });
  //  };
  //  cache.src = $("#src").val();
 //
//  });
});

function show_next_image(path, fname){
  var img_url = path + '/' + fname;
  var $preview_pane = $('#preview_pane');
  var $image = $('#image');
  var cache = new Image();
  cache.onload = function () {
    $image.attr("src", cache.src);
    $preview_pane.css({
      width: $image.width(),
      height: $image.height()
    });
  };
  cache.src = img_url;
  $(".final").remove();
  $('#curr_image').empty().append("<p> Current Image: " + fname + "</p>");
}

function clonerect($obj, $val) {
  var name = "<h2>" + $val + "</h2>";
  $("<div>")
    .addClass("final")
    .attr("title",$val)
    .css({
      top: $obj.position().top,
      left: $obj.position().left,
      width: $obj.width(),
      height: $obj.height()
    })
    .append(name)
    .appendTo("#preview_pane");
}

function update(){
  var fname = $("#image")[0].currentSrc.split("/").pop();
  var curr_id = fname.split('.')[0];
  var list = undefined;
  console.log(curr_id);
  if ( $('#' + curr_id).length == 0){
    var new_list = "<ol id='" + curr_id + "'></ol>";
    console.log(new_list);
    $("#output").append(new_list);
  }
  var result = "";
  $(".final").each(function(i, el){

    var coords =  parseInt($(el).position().left,10) +
           "," +
           parseInt($(el).position().top,10) +
           "," +
           parseInt(($(el).position().left + $(el).width()),10) +
           "," +
           parseInt(($(el).position().top + $(el).height()),10);
    result = result + "<li>" + fname + " " + $(el).attr("title") + " " + coords + "</li>";
    console.log(result);
  });
  $('#' + curr_id).empty().append(result);
}

// //function update() {
// //  var j = {};
// //  var o = [];
// //  o[0] = "<img usemap='#mymap' src='" + $("#src").val() + "' />";
//   o[1] = "<map id='_mymap' name='mymap'>";
//   $(".final").each(function(index,el) {
//     o[index+2] = "  <area shape='rect' title='" +
//       $(el).attr("title") +
//       "' coords='" +
//       parseInt($(el).position().left,10) +
//       "," +
//       parseInt($(el).position().top,10) +
//       "," +
//       parseInt(($(el).position().left + $(el).width()),10) +
//       "," +
//       parseInt(($(el).position().top + $(el).height()),10) +
//       "' />";
//   });
//   o[o.length] = "</map>";
//   $("#output").val(o.join("\n"));
// }
