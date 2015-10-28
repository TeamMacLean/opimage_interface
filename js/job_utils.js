function add_job_list(url,element) {
  console.log('spawned');
  console.log(url);
  $.getJSON(url, function( data ) {
    console.log(data);
    var job_list = [];
    $.each(data, function(i, job){
      job_list.push("<li>" + job['pid'] + "</li>");
    });
    if (job_list.length > 0){
      $(element).replaceWith("<ul>" + job_list.join("") + "</ul>");
    }
  });
}
