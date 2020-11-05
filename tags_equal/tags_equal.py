
def parse_tag(html_tag):
    """Return tuple of tag name and sorted attributes."""
    tag_name, *attr_strings = html_tag[1:-1].lower().split()
    attributes = {}
    for attribute in attr_strings:
        try:
            key, value = attribute.split('=')
        except ValueError:
            key, value = attribute, None
        attributes.setdefault(key, value)
    return tag_name, attributes


def tags_equal(tag1, tag2):
    """Return True if the given HTML open tags represent the same thing."""
    return parse_tag(tag1) == parse_tag(tag2)
