import os
import shutil

# Исходный словарь: путь к SVG -> emoji символ
emojis = {
    'icons/apnea.svg': '🤿',
    'icons/surface.svg': '🌊',
    'icons/bifins.svg': '👟',
    'icons/immersion.svg': '🫧',
}

svg_src_dir = 'svg_src'


def emoji_to_filename(emoji_char):
    codepoints = [f'{ord(c):x}' for c in emoji_char]
    filename = 'u' + '_'.join(codepoints) + '.svg'
    return filename


def prepare_svg_src():
    os.makedirs(svg_src_dir, exist_ok=True)

    for src_path, emoji_char in emojis.items():
        if not os.path.isfile(src_path):
            print(f"Файл не найден: {src_path}")
            continue
        filename = emoji_to_filename(emoji_char)
        dst_path = os.path.join(svg_src_dir, filename)
        print(f'Копируем {src_path} -> {dst_path}')
        shutil.copy(src_path, dst_path)


if __name__ == '__main__':
    prepare_svg_src()
