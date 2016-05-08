from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Common(object):

    @staticmethod
    def contains(characters, verbose=None):
        return RegexValidator(
            r'^[' + characters + ']*$',
            'Only ' + (verbose or characters) + ' characters are allowed.'
        )

    @staticmethod
    def alphanumeric():
        return Common.contains('0-9a-zA-Z', 'alphanumeric')

    @staticmethod
    def starts_with(val):
        val = str(val)
        return RegexValidator(
            '^[' + val + ']',
            'Must start with a ' + val + '.'
        )

    @staticmethod
    def starts_with_letter():
        return RegexValidator(
            '^[a-zA-Z]',
            'Must start with a letter.'
        )

    @staticmethod
    def min_length(val):
        val = str(val)
        return RegexValidator(
            '^(.){' + val + ',}$',
            'A minimum of ' + val + ' characters are required.'
        )


class File(object):

    @staticmethod
    def max_size(size):
        """
        Sets the maximum size of a FieldFile.
        :param size: maximum file size in bytes
        """
        def _max_size(obj):
            obj_size = obj.file.size
            if obj_size > size:
                size_mb = File._bytes_to_megabytes(size)
                raise ValidationError('Maximum file size is {0}MB'
                                      .format(size_mb))
        return _max_size

    @staticmethod
    def _bytes_to_megabytes(val, decimals=2):
        return round(val / 1024 / 1024, decimals)
