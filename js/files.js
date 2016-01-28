var fileUtils = {};

fileUtils.get_parsed_static_JSON = function(path, file){
  var url = path + '/' + file;
  return $.get(url).responseJSON;
}

fileUtils.getParameterByName = function(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

fileUtils.sort_nums = function(a,b){
  return a - b;
}

fileUtils.get_image_list = function(path){
  var image_list = [];
  var path = fileUtils.getParameterByName('path');
  var layout = fileUtils.get_parsed_static_JSON(path, 'layout.json');
  var racks = Object.keys(layout).sort(fileUtils.ort_nums);
  for ( var r = 1; r <= racks.length; r++){
    var plots = Object.keys(layout[r]).sort(fileUtils.sort_nums);
    for (var p = 1; p<= plots.length; p++){
      image_list.push(layout[r][p]);
    }
  }
  return image_list;
}

fileUtils.send_download_json = function(obj, fname){
  var blob = new Blob([JSON.stringify(obj)], {type: "application/json;charset=utf-8"});
  saveAs(blob, fname);
}
