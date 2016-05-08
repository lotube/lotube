PROJECT_NAME = 'lotube'
PAGINATE_BY = 10  # X items per page


def app_constants(request):
    return {
        'PROJECT_NAME': PROJECT_NAME,
    }
