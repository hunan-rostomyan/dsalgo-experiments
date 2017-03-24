def links_from_list(Link, lst):
    """Convert a list into a linked list."""
    ll = Link()
    for item in lst:
        ll.insert(Link(item))
    return ll

