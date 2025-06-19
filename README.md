# FINCUBES-FONT

Проект для создания кастомного цветного шрифта из SVG-иконок (эмодзи) с помощью [nanoemoji](https://github.com/googlefonts/nanoemoji) (Noto Emoji).

Позволяет конвертировать SVG в цветной OpenType шрифт, генерировать web-форматы и подключать шрифт через CSS, как Google Fonts.

---

## Структура проекта

```
FINCUBES-FONT/
│
├── icons/              # Исходные SVG-иконки для каждого глифа (оригинальные)
├── svg_src/            # Подготовленные SVG с переименованными файлами для nanoemoji
├── fonts/              # Итоговые шрифты в форматах TTF, WOFF, WOFF2
├── build/              # Временные файлы сборки (nanoemoji)
├── example/            # Примеры подключения и использования шрифта через CSS/HTML
├── public/             # Папка для публичных ассетов для CDN
├── .venv/              # Виртуальное окружение Python (опционально)
├── main.py             # Создаёт цветной шрифт из svg_src в build/Font.ttf
├── convertor.py        # Переносит шрифт из build/ в fonts/, конвертирует в WOFF/WOFF2
├── prepare_name.py     # Создаёт папку svg_src из icons, переименовывая SVG для nanoemoji
├── generate_public.py  # Генерирует папку public/ с готовыми к загрузке в CDN файлами и CSS
├── Font.toml           # Конфигурация nanoemoji
├── requirements.txt    # Зависимости Python
└── README.md           # Этот файл
```

---

## Порядок работы со скриптами

1. **prepare_name.py** — создаёт из исходников `icons/` папку `svg_src/` с переименованными SVG, удобными для nanoemoji (имена файлов — Unicode коды эмодзи).

2. **main.py** — собирает цветной шрифт из `svg_src/`, создаёт `build/Font.ttf` с помощью nanoemoji.

3. **convertor.py** — переносит TTF-шрифт из `build/` в `fonts/`, создаёт web-форматы `.woff` и `.woff2`.

4. **generate_public.py** — создаёт папку `public/` с шрифтами и CSS для подключения, готовую к загрузке на CDN.

---

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# или
.venv\Scripts\activate     # Windows

pip install -r requirements.txt

python prepare_name.py
python main.py
python convertor.py
python generate_public.py
```

---

## Использование шрифта в CSS

```css
@font-face {
  font-family: "FincubesFont";
  src: url("../fonts/fin.woff2") format("woff2"), url("../fonts/fin.woff")
      format("woff"), url("../fonts/fin.ttf") format("truetype");
  font-weight: 400;
  font-style: normal;
  font-display: swap;

  unicode-range: U+1F93F, U+1F30A, U+1F45F, U+1FAE7;
}
```

---

## Лицензия

Проект распространяется под лицензией Apache License 2.0.

Вы можете свободно использовать, изменять и распространять этот код при соблюдении условий лицензии.

Подробнее: [https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)
