var jobUtils = {};
jobUtils.add_job_list = function(url,element) {
  $.getJSON(url, function( data ) {
    var job_list = [];
    $.each(data, function(i, job){
      job_list.push("<tr><td>" + job['short_name'] + '</td><td>' +
      job['pid']  + '</td><td>' +
      job['status'] + "</td><td>" +
      job['type'] + "</td><td>" +
      String(new Date(job['start_time'])) + "</td><td><a href='/" +
      job['work_folder'] + "'>" + job['work_folder'] + "</a></td><td><button type='button' class='btn btn-danger' onclick='jobUtils.kill_job(" +
      job['pid'] + ")'>Stop</button></td><td><button type='button' class='btn btn-danger' onclick='jobUtils.remove_job_from_list(" +
       job['pid'] + ")'>Remove</button></td></tr>");
    });
    if (job_list.length > 0){
      $(element).replaceWith("<table class='table'><tr><th>Job Name</th><th>Process ID</th><th>Status</th><th>Type</th><th>Start Time</th><th>Work Folder</th><th></th><th></th><th></th></tr>" + job_list.join("") + "</table>");
    }
  });
}

jobUtils.kill_job = function(pid){
  var url = 'cgi-bin/kill_job.cgi?pid=' + pid;
  window.location.replace(url);
}

jobUtils.remove_job_from_list = function(pid){
  var url = 'cgi-bin/remove_job_from_list.cgi?pid=' + pid;
  window.location.replace(url);
}

jobUtils.add_existing_image_folder_list = function(url, element){
  $.getJSON(url, function( data ){
    console.log(data);
    var image_folder_list = [];
    $.each(data, function(i, image_folder){
      var analysis_exists = 'No';
      var analysis_button = '';
      if (image_folder['analysis_exists']){
        analysis_exists = 'Yes';
      }
      else{
        analysis_button = "</td><td><div class='dropdown'>  <button type='button' class='btn btn-primary dropdown-toggle' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'> Select Analysis Method <span class='caret'></span> </button><ul class='dropdown-menu'> <li><a href='select_regions.html?path=" +
        image_folder['path'] +
         "'>NDVI</a></li> <li><a href='#'>Method 2</a></li><li><a href='#'>Method 3</a></li></ul></div></td><td>";
      }
      image_folder_list.push("<tr><td>" + image_folder['short_name'] + "</td><td>" +
      "<a href='/" +
      image_folder['path'] + "'>" + image_folder['path'] + "</a>" + '</td><td>' +
      image_folder['status'] + '</td><td>' +
      String(new Date(image_folder['collection_datetime'])) + '</td><td>' +
      analysis_exists + '</td><td>' +
      analysis_button + '</td><td>' +
      '</tr>'
      );
    });
    if (image_folder_list.length > 0){
      console.log(image_folder_list.length)
      $(element).replaceWith("<table class='table'><tr><th>Job Name</th><th>Image Folder</th><th>Folder Status</th><th>Collection Date Time</th><th>Existing Analysis</th><th></th><th></th></tr>" + image_folder_list.join("") + "</table>");
    }
  });
}
