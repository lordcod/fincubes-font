from pathlib import Path
from fontTools.ttLib import TTFont
import os
import subprocess
import sys
import shutil

# === Настройки ===

emojis = {
    'icons/apnea.svg': '🤿',
    'icons/surface.svg': '🌊',
    'icons/bifins.svg': '👟',
    'icons/immersion.svg': '🫧',
}

BUILD_DIR = Path('build')
BUILD_DIR.mkdir(exist_ok=True)

SVG_SRC_DIR = Path('build/svg_src')
BUILD_TTF_FILE = Path('build/Font.ttf')
FONTS_FOLDER = Path('build/fonts')
PUBLIC_FOLDER = Path('dist')
PREFIX_FILENAME_PUBLIC = 'fincubesfont'


# === Утилиты ===

def emoji_to_filename(emoji_char: str) -> str:
    codepoints = [f'{ord(c):x}' for c in emoji_char]
    return 'u' + '_'.join(codepoints) + '.svg'


def check_nanoemoji_installed():
    if shutil.which('nanoemoji') is None:
        print("❌ nanoemoji не найден. Установи его: pip install nanoemoji")
        sys.exit(1)


# === Этапы пайплайна ===

def prepare_svg_src():
    SVG_SRC_DIR.mkdir(exist_ok=True)
    for src_path, emoji_char in emojis.items():
        src = Path(src_path)
        if not src.exists():
            print(f"⚠️ Файл не найден: {src}")
            continue
        dst = SVG_SRC_DIR / emoji_to_filename(emoji_char)
        print(f'📥 Копируем {src} → {dst}')
        shutil.copy(src, dst)


def build_color_font():
    check_nanoemoji_installed()

    svg_files = sorted(SVG_SRC_DIR.glob("u*.svg"))
    if not svg_files:
        print(f'❌ Нет SVG-файлов в {SVG_SRC_DIR}')
        sys.exit(1)

    cmd = [
        'nanoemoji',
        '--color_format', 'glyf_colr_1',
        *map(str, svg_files)
    ]

    print('🚀 Запускаем nanoemoji:')
    print(' '.join(cmd))

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print('❌ Ошибка nanoemoji:')
        print(result.stderr)
        sys.exit(result.returncode)

    print('✅ Шрифт успешно сгенерирован!')


def convert_ttf_to_style(ttf_path: Path, out_path: Path, style: str):
    font = TTFont(str(ttf_path))
    font.flavor = style
    font.save(str(out_path))


def convert_fonts():
    FONTS_FOLDER.mkdir(exist_ok=True)
    shutil.copy(BUILD_TTF_FILE, FONTS_FOLDER / 'font.ttf')
    convert_ttf_to_style(BUILD_TTF_FILE, FONTS_FOLDER / "font.woff", 'woff')
    convert_ttf_to_style(BUILD_TTF_FILE, FONTS_FOLDER / "font.woff2", 'woff2')
    print('🎉 Конвертированы шрифты: TTF, WOFF, WOFF2')


def generate_public():
    PUBLIC_FOLDER.mkdir(exist_ok=True)
    for file in FONTS_FOLDER.iterdir():
        ext = file.suffix
        new_name = f"{PREFIX_FILENAME_PUBLIC}{ext}"
        shutil.copy(file, PUBLIC_FOLDER / new_name)
    print('🌐 Готово к использованию через CDN!')


# === Запуск ===

if __name__ == '__main__':
    prepare_svg_src()
    build_color_font()
    convert_fonts()
    generate_public()
