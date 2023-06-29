$(document).ready(function() {
    $('#lecturer-form').on('submit', function(event) {
        event.preventDefault();

        var level = $('#level').val();
        var semester = $('#semester').val();

        $.ajax({
            url: '/fetch-lecturers/',
            type: 'GET',
            data: {
                level: level,
                semester: semester
            },
            success: function(response) {
                var lecturers = response.lecturers;
                var lecturerList = $('#lecturer-list');
                var paginationContainer = $('#pagination-container');
                
                // Clear previous data
                lecturerList.empty();
                paginationContainer.empty();

                // Calculate number of pages
                var numPages = Math.ceil(lecturers.length / 10);

                // Display lecturers for the current page
                var currentPage = 1;
                displayLecturersForPage(currentPage);

                // Create pagination links
                for (var i = 1; i <= numPages; i++) {
                    var link = $('<a>', {
                        href: '#',
                        text: i,
                        click: function() {
                            currentPage = $(this).text();
                            displayLecturersForPage(currentPage);
                        }
                    });
                    paginationContainer.append(link);
                }

                // Update the total number of lecturers
                $('#total-lecturers').text(lecturers.length);

                // Function to display lecturers for the specified page
                function displayLecturersForPage(page) {
                    lecturerList.empty();
                    var startIndex = (page - 1) * 10;
                    var endIndex = startIndex + 10;

                    for (var i = startIndex; i < endIndex; i++) {
                        if (i >= lecturers.length) {
                            break;
                        }

                        var lecturerName = lecturers[i];
                        lecturerList.append('<li>' + (i+1) + '. ' + lecturerName + '</li>');
                    }

                    // Highlight the current page link
                    paginationContainer.find('a').removeClass('active');
                    paginationContainer.find('a:nth-child(' + page + ')').addClass('active');
                }
            },
            error: function(xhr) {
                console.log(xhr.responseText);
            }
        });
    });
});