function add_job_list(url,element) {
  $.getJSON(url, function( data ) {
    var job_list = [];
    $.each(data, function(i, job){
      job_list.push("<tr><td>" + job['short_name'] + '</td><td>' +
      job['pid']  + '</td><td>' +
      job['status'] + "</td><td>" +
      job['type'] + "</td><td>" +
      String(new Date(job['start_time'])) + "</td><td><a href='/" +
      job['work_folder'] + "'>" + job['work_folder'] + "</a></td><td><button type='button' class='btn btn-danger' onclick='kill_job(" +
      job['pid'] + ")'>Stop</button></td><td><button type='button' class='btn btn-danger' onclick='remove_job_from_list(" +
       job['pid'] + ")'>Remove</button></td></tr>");
    });
    if (job_list.length > 0){
      $(element).replaceWith("<table class='table'><tr><th>Job Name</th><th>Process ID</th><th>Status</th><th>Type</th><th>Start Time</th><th>Work Folder</th><th></th><th></th><th></th></tr>" + job_list.join("") + "</table>");
    }
  });
}

function kill_job(pid){
  var url = 'cgi-bin/kill_job.cgi?pid=' + pid;
  window.location.replace(url);
}

function remove_job_from_list(pid){
  var url = 'cgi-bin/remove_job_from_list.cgi?pid=' + pid;
  window.location.replace(url);
}
