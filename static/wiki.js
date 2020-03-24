$( document ).ready(function() {
  $('td.detail_link').on('click tap', function(event) {
    window.location.href = 'list-' + this.attributes.row.value + '-' + this.attributes.col.value + '/';
  });
  $('#createEntry').on('click tap', function(event) {
    window.location.href = '/create-' + event.target.attributes.row.value + '-' + event.target.attributes.col.value + '/';
  });
  $('#id_title, #id_text, #id_name, #id_email').parents('tr').css('visibility', 'visible');
});
