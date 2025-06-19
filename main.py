from fontTools.ttLib import TTFont, newTable
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.fontBuilder import FontBuilder
import os
import xml.etree.ElementTree as ET
emojis = {
    'apnea': '🤿',
    'surface': '🌊',
    'bifins': '👟',
    'immersion': '🫧',
}
icons_folder = 'icons'
output_path = 'fonts/fin.ttf'


def svg_to_glyph(svg_path):
    # Простой пример парсинга SVG контуров для глифа
    # Реальный парсинг пути SVG — сложная задача, здесь пример
    # Можно использовать svgpathtools для разбора пути и конвертации в команды
    tree = ET.parse(svg_path)
    root = tree.getroot()

    pen = TTGlyphPen(None)

    # TODO: Реальный парсинг контуров SVG в команды pen
    # Пока что заглушка — пустой глиф
    # Нужно конвертировать <path d="..."> из SVG в pen.moveTo, pen.lineTo и т.д.

    # Для демонстрации создадим квадрат:
    pen.moveTo((100, 100))
    pen.lineTo((500, 100))
    pen.lineTo((500, 500))
    pen.lineTo((100, 500))
    pen.closePath()

    glyph = pen.glyph()
    return glyph


def unicode_to_int(char):
    return ord(char)


def create_notdef_glyph():
    pen = TTGlyphPen(None)
    pen.moveTo((0, 0))
    pen.lineTo((0, 0))
    pen.closePath()
    return pen.glyph()


def create_font(emojis, icons_folder):
    fb = FontBuilder(1024, isTTF=True)
    fb.setupGlyphOrder(['.notdef'] + list(emojis.keys()))
    fb.setupCharacterMap({ord(emojis[k]): k for k in emojis})

    glyphs = {glyphName: svg_to_glyph(os.path.join(
        icons_folder, glyphName + '.svg')) for glyphName in emojis.keys()}
    glyphs['.notdef'] = create_notdef_glyph()
    fb.setupGlyf(glyphs)

    advanceWidths = {glyphName: (600, 50) for glyphName in emojis.keys()}
    advanceWidths['.notdef'] = (600, 50)
    fb.setupHorizontalMetrics(advanceWidths)

    fb.setupHorizontalHeader(ascent=800, descent=200)
    fb.setupNameTable({'familyName': 'MyCustomFont', 'styleName': 'Regular'})
    fb.setupOS2()
    fb.setupPost()

    fb.save(output_path)


if __name__ == '__main__':
    create_font(emojis, icons_folder)
