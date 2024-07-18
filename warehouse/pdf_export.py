# pdf_export.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from import_export.formats import base_formats

class CustomPDF(base_formats.BaseFormat):
    def export_data(self, dataset, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="export.pdf"'

        # Create PDF content using ReportLab
        p = canvas.Canvas(response, pagesize=letter)
        p.drawString(100, 750, "PDF Export Example")
        p.showPage()
        p.save()

        return response
