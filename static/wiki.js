$( document ).ready(function() {
  $("td.detail_link").on("click tap", function(event) {
    window.location.href = 'list/' + event.target.attributes.row.value + '/' + event.target.attributes.col.value + '/';
  });
});
