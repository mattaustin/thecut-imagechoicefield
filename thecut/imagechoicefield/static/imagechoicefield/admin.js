django.jQuery(document).ready(function ($) {

    var selectedClass = 'selected';

    $('.imagechoicefield').addClass('js-enabled');

    $('.imagechoicefield input[type="radio"]').change(function () {
        var $radio = $(this);
        var $label = $radio.closest('label');
        if ($radio.is(':checked')) {
            $radio.closest('ul').find('label').removeClass(selectedClass);
            $label.addClass(selectedClass);
        } else {
            $label.removeClass(selectedClass);
        }
    }).change();

});
