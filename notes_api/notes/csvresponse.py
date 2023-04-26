import csv
import io
from django.http import HttpResponse

class CSVResponse(HttpResponse):
    def __init__(self, data, filename=None):
        if not filename:
            filename = 'data.csv'
        content = self.to_csv(data)
        super().__init__(content, content_type='text/csv')
        self['Content-Disposition'] = f'attachment; filename="{filename}"'

    def to_csv(self, data):
        header = data[0].keys()
        rows = [row.values() for row in data]
        string = io.StringIO()
        writer = csv.writer(string)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
        return string.getvalue()
