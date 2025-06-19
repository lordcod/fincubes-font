import os
import subprocess
import sys


def build_color_font(svg_dir='svg_src', output_dir='build', font_family='FinCubes'):
    # Получаем список файлов с префиксом 'u' и расширением .svg
    svg_files = [
        os.path.join(svg_dir, f)
        for f in os.listdir(svg_dir)
        if f.startswith('u') and f.endswith('.svg')
    ]

    if not svg_files:
        print(f'Нет SVG файлов в папке {svg_dir}')
        sys.exit(1)

    # Формируем команду
    cmd = [
        'nanoemoji',
        '--color_format', 'glyf_colr_1',
        *svg_files
    ]

    print('Запускаем команду:')
    print(' '.join(cmd))

    # Запускаем nanoemoji
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print('Ошибка при запуске nanoemoji:')
        print(result.stderr)
        sys.exit(result.returncode)

    print('Шрифт успешно сгенерирован!')
    print(result.stdout)


if __name__ == '__main__':
    build_color_font()
