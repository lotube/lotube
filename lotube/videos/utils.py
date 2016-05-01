from constants import MIN_TAGS, MAX_TAGS


class Utils:

    @staticmethod
    def get_tags(title):
        """Gets all tags from title."""
        tags = filter(lambda x: len(x) > 2, title.split())
        if not tags:
            return title.split()[:MIN_TAGS]  # Minimum of tags
        return tags[:MAX_TAGS]
