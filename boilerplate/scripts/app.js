jQuery(document).ready(function($) {
    /**
     * Activate semantic-ui features
     */
    // $('.ui.sidebar')
    //     .sidebar('attach events', '.toc.item')
    // ;

    $('.ui.dropdown')
        .dropdown()
    ;

    $('.special.card .image').dimmer({
        on: 'hover'
    });


    /**
     * Custom app code
     */
    $('#change-profile-image').on('click', function() {
        $('#profile-image-input').click();
    });

    $('.ui.modal')
        .modal({
            blurring: true
        })
        .modal('show')
    ;
});