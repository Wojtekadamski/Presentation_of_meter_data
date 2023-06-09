// Script for the interactive graph
$(function () {
    $('#datetimepicker1').datetimepicker();
});

$(function () {
    $('#datetimepicker2').datetimepicker();
});

// Script for the dropdown menu
$('.dropdown-toggle').dropdown()

// Script for the modal
$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})

// Script for the tooltip
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

// Script for the popover
$(function () {
    $('[data-toggle="popover"]').popover()
})
