import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Asegurar la existencia del directorio de salida
os.makedirs('generated', exist_ok=True)
pdf_path = 'generated/certificado_fin_estudios.pdf'

# Configurar el documento (Letter horizontal: 792 x 612 puntos)
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=landscape(letter),
    leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40,
    title="Certificado de Fin de Estudios"
)

styles = getSampleStyleSheet()

# Estilos tipográficos institucionales
style_institucion = ParagraphStyle(
    'Inst', fontName='Helvetica-Bold', fontSize=22, leading=26, alignment=1, textColor=colors.HexColor('#1A365D')
)
style_subtitulo = ParagraphStyle(
    'Sub', fontName='Helvetica', fontSize=11, leading=15, alignment=1, textColor=colors.HexColor('#4A5568')
)
style_titulo = ParagraphStyle(
    'Tit', fontName='Helvetica-Bold', fontSize=34, leading=40, alignment=1, textColor=colors.HexColor('#2C3E50')
)
style_texto = ParagraphStyle(
    'Tex', fontName='Helvetica', fontSize=14, leading=22, alignment=1, textColor=colors.HexColor('#2D3748')
)
style_nombre = ParagraphStyle(
    'Nom', fontName='Helvetica-Bold', fontSize=24, leading=28, alignment=1, textColor=colors.HexColor('#2B6CB0')
)
style_firma = ParagraphStyle(
    'Fir', fontName='Helvetica', fontSize=10, leading=14, alignment=1, textColor=colors.HexColor('#4A5568')
)

story = []

# Distribución del contenido vertical
story.append(Spacer(1, 40))
story.append(Paragraph("INSTITUTO DE EDUCACIÓN SUPERIOR", style_institucion))
story.append(Paragraph("Reconocimiento Oficial del Ministerio de Educación", style_subtitulo))
story.append(Spacer(1, 35))

story.append(Paragraph("CERTIFICADO DE FIN DE ESTUDIOS", style_titulo))
story.append(Spacer(1, 30))

story.append(Paragraph("Se otorga el presente documento a:", style_texto))
story.append(Spacer(1, 10))
story.append(Paragraph("ALEJANDRO MARTÍNEZ GÓMEZ", style_nombre))
story.append(Spacer(1, 10))
story.append(Paragraph("D.N.I. / Documento de Identidad: 12.345.678X", style_texto))
story.append(Spacer(1, 25))

texto_cuerpo = (
    "Por haber cursado y aprobado satisfactoriamente la totalidad del plan de estudios correspondiente "
    "a la carrera de <b>Tecnicatura Superior en Desarrollo de Software</b>, cumpliendo con todos los "
    "requisitos académicos y legales exigidos por esta institución."
)
story.append(Paragraph(texto_cuerpo, style_texto))
story.append(Spacer(1, 25))

story.append(Paragraph("Dado en la ciudad de Buenos Aires, a los 16 días del mes de agosto de 2026.", style_texto))
story.append(Spacer(1, 70))

# Bloque inferior para firmas de autoridades
data_firmas = [
    ["", ""], 
    [Paragraph("<b>Dr. Carlos Mendoza</b><br/>Director General", style_firma),
     Paragraph("<b>Dra. Elena Rostova</b><br/>Secretaria Académica", style_firma)]
]
t_firmas = Table(data_firmas, colWidths=[220, 220])
t_firmas.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LINEABOVE', (0,1), (0,1), 1, colors.HexColor('#4A5568')), 
    ('LINEABOVE', (1,1), (1,1), 1, colors.HexColor('#4A5568')), 
]))

# Centrar el bloque de firmas en el flujo de la página
t_contenedor = Table([[t_firmas]], colWidths=[712])
t_contenedor.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER')]))
story.append(t_contenedor)

# Función callback para dibujar el marco decorativo directamente sobre el lienzo
def dibujar_marco(canvas, doc):
    canvas.saveState()
    # Borde azul exterior grueso
    canvas.setStrokeColor(colors.HexColor('#1A365D'))
    canvas.setLineWidth(4)
    canvas.rect(20, 20, 752, 572)
    
    # Borde dorado interior fino
    canvas.setStrokeColor(colors.HexColor('#D69E2E'))
    canvas.setLineWidth(1.5)
    canvas.rect(26, 26, 740, 560)
    canvas.restoreState()

# Ejecutar compilación del PDF asignando el dibujo del marco a la primera página
doc.build(story, onFirstPage=dibujar_marco)
