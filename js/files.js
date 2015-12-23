function get_parsed_static_JSON(path, file){
  var url = path + '/' + file;
  return $.get(url).responseJSON;
}

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function sort_nums(a,b){
  return a - b;
}

function get_image_list(path){
  var image_list = [];
  var path = getParameterByName('path');
  var layout = get_parsed_static_JSON(path, 'layout.json');
  var racks = Object.keys(layout).sort(sort_nums);
  for ( var r = 1; r <= racks.length; r++){
    var plots = Object.keys(layout[r]).sort(sort_nums);
    for (var p = 1; p<= plots.length; p++){
      image_list.push(layout[r][p]);
    }
  }
  return image_list;
}
