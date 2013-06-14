
import json
from gerrit import ssh
from gerrit import filters


class Query(ssh.Client):

    def __init__(self, *args, **kwargs):
        super(Query, self).__init__(*args, **kwargs)

        self._filters = filters.Items()

    def __iter__(self):
        return iter(self._execute())

    def _execute(self):
        """Executes the query and yields items."""

        query = [
            'gerrit', 'query',
            str(self._filters),
            '--current-patch-set',
            '--comments',
            '--format=JSON']

        results = self.client.exec_command(' '.join(query))
        stdin, stdout, stderr = results

        for line in stdout:
            normalized = json.loads(line)

            if "rowCount" in normalized:
                raise StopIteration

            yield normalized

    def filter(self, *filters):
        """Adds generic filters to use in the query

        For example:

            - is:open
            - is:
        :param filters: List or tuple of projects
        to add to the filters.
        """
        self._filters.extend(filters)
        return self

    def limit(self, limit):
        assert isinstance(limit, int)
        self._limit = limit
