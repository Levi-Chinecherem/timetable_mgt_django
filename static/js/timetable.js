$(document).ready(function() {
    $('#timetable-form').on('submit', function(event) {
        event.preventDefault();

        var level = $('#level').val();
        var semester = $('#semester').val();

        // Fetch the timetable data based on the selected level and semester
        $.ajax({
            url: '/fetch-timetable/',
            type: 'GET',
            data: {
                'level': level,
                'semester': semester
            },
            dataType: 'json',
            success: function(response) {
                if (response.success) {
                    var timetable = response.timetable;

                    // Clear the existing table rows
                    $('#timetable-table').find('tr:gt(0)').remove();

                    // Populate the timetable table with the fetched data
                    $.each(timetable, function(index, entry) {
                        var row = '<tr>' +
                            '<td>' + entry.day + '</td>' +
                            '<td>' + entry.start_time + '</td>' +
                            '<td>' + entry.end_time + '</td>' +
                            '<td>' + entry.course.name + '</td>' +
                            '<td>' + entry.lecturer.name + '</td>' +
                            '<td>' + entry.semester + '</td>' +
                            '</tr>';
                        $('#timetable-table').append(row);
                    });
                } else {
                    console.log('Error: ' + response.message);
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log('Error:', errorThrown);
            }
        });
    });
});
