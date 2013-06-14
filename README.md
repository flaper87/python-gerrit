python-gerrit
=============

Python library for managing Gerrit through ssh


Getting Started
===============

    from gerrit import filters
    from gerrit import reviews

    project = filters.OrFilter()
    project.add_items('project', ['openstack/glance', 'openstack/python-glanceclient'])

    other = filters.Items()
    other.add_items('is', 'open')
    other.add_items('limit', 100)

    query = reviews.Query('review.openstack.org')
    for review in query.filter(project, other):
        # do something with the review
