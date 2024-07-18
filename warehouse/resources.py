import chardet
from import_export import resources
from import_export.results import Result
from import_export.formats.base_formats import CSV
from .models import Stock

class StockResource(resources.ModelResource):
    class Meta:
        model = Stock

    def import_data(self, dataset, dry_run=False, raise_errors=False, file_name=None, user=None, **kwargs):
        result = Result()
        if isinstance(dataset, CSV):
            encoding = self.detect_encoding(dataset)
            try:
                dataset.load(dataset, format='csv', encoding=encoding)
            except UnicodeDecodeError as e:
                result.import_type = result.IMPORT_TYPE_ERROR
                result.base_errors.append(f"UnicodeDecodeError: {str(e)}. Ensure you have chosen the correct format for the file.")
        return super().import_data(dataset, dry_run, raise_errors, file_name, user, **kwargs)

    @staticmethod
    def detect_encoding(data):
        if isinstance(data, bytes):
            result = chardet.detect(data)
            return result['encoding']
        return 'utf-8'
