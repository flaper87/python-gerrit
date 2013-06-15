python-gerrit
=============

Python library for managing Gerrit through ssh


Getting Started
===============


Queries
-------

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

Reviews
-------

    from gerrit import reviews

    rev = reviews.Review('23424,12', host='review.openstack.org')

    # Set the patch as WIP
    rev.status('workinprogress')
    rev.commit()

    # Set the patch as ready for review
    rev.status('readyforreview')
    rev.commit("Ok, it is ready for review")

    # Code-review -2
    rev.review(-2)
    rev.commit("Erm, I don't like this patch at all")

    # Code-review -2
    rev.review(2)
    rev.verify(1)
    rev.commit("Cool, LGTM, approved")
