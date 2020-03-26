$( document ).ready(function() {
  $('td.detail_link').on('click tap', function() {
    window.location.href = 'list-' + this.attributes.row.value + '-' + this.attributes.col.value + '/';
  });
  $('#createInfo1, #createInfo2').on('click tap', function() {
    window.location.href = '/create-' + this.attributes.row.value + '-' + this.attributes.col.value + '/';
  });
  $('.card .btn-link').on('click tap', function() {
    $(this).find('i.icon').toggleClass('fa-angle-down fa-angle-up');
  });
  $('#id_text').attr('rows', 5);
});
