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
  
            // Group the timetable data by day
            var groupedTimetable = groupTimetableByDay(timetable);
  
            // Sort the timetable entries within each day by start_time
            sortTimetableByTime(groupedTimetable);
  
            // Populate the timetable table with the grouped and sorted data
            $.each(groupedTimetable, function(day, entries) {
              var hasCourse = entries.some(function(entry) {
                return entry.course.name !== 'Break Time';
              });
  
              if (hasCourse) {
                var breakAdded = false;
  
                $.each(entries, function(index, entry) {
                  if (entry.course.name === 'Break Time' && breakAdded) {
                    return; // Skip adding additional break entries
                  }
  
                  if (entry.course.name === 'Break Time') {
                    breakAdded = true;
                  }
  
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
  
                if (!breakAdded) {
                  // Add the break time entry if it hasn't been added yet
                  var breakRow = '<tr class="break-row">' +
                    '<td>' + day + '</td>' +
                    '<td>' + '12:00' + '</td>' +
                    '<td>' + '12:00' + '</td>' +
                    '<td>' + 'Break Time' + '</td>' +
                    '<td>' + '' + '</td>' +
                    '<td>' + '' + '</td>' +
                    '</tr>';
                  $('#timetable-table').append(breakRow);
                }
              } else {
                // Remove the break row if there are no courses for the day
                $('#timetable-table tr:contains("' + day + '")').remove();
              }
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
  
    // Function to group the timetable entries by day
    function groupTimetableByDay(timetable) {
      var groupedTimetable = {};
  
      // Initialize the grouped timetable with empty arrays for each day
      var days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
      $.each(days, function(index, day) {
        groupedTimetable[day] = [];
      });
  
      // Add the timetable entries to the corresponding day in the grouped timetable
      $.each(timetable, function(index, entry) {
        groupedTimetable[entry.day].push(entry);
      });
  
      return groupedTimetable;
    }
  
    // Function to sort the timetable entries within each day by start_time
    function sortTimetableByTime(groupedTimetable) {
      var days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
  
      $.each(days, function(index, day) {
        groupedTimetable[day].sort(function(a, b) {
          var timeA = new Date('1970/01/01 ' + a.start_time);
          var timeB = new Date('1970/01/01 ' + b.start_time);
          return timeA - timeB;
        });
      });
    }
  });
  