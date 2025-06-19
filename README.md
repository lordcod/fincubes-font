# FINCUBES-FONT

Проект для создания кастомного шрифта из SVG-иконок (эмодзи), конвертации в разные форматы шрифтов и подключения их через CSS, как в Google Fonts.

---

## Структура проекта

```
FINCUBES-FONT/
│
├── icons/              # Исходные SVG-иконки для каждого глифа
│   ├── apnea.svg
│   ├── bifins.svg
│   ├── immersion.svg
│   └── surface.svg
│
├── fonts/              # Скомпилированные шрифты в разных форматах
│   ├── fin.ttf
│   ├── fin.woff
│   └── fin.woff2
│
├── example/            # Примеры подключения шрифта через CSS
│   ├── font.css        # CSS с @font-face для подключения шрифта
│   └── usage.css       # Пример использования шрифта в стилях
│
├── convertor.py        # Скрипт конвертации TTF -> WOFF/WOFF2
├── main.py             # Основной скрипт для генерации шрифта из SVG
├── requirements.txt    # Зависимости проекта
└── .venv/              # Виртуальное окружение Python (опционально)
```

---

## Как использовать

1. Клонируйте репозиторий и создайте виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Поместите ваши SVG-иконки в папку `icons/` с именами:

- `apnea.svg`
- `surface.svg`
- `bifins.svg`
- `immersion.svg`

4. Запустите скрипт генерации шрифта:

```bash
python main.py
```

Шрифт будет сгенерирован и сохранён в `fonts/fin.ttf`.

5. Запустите конвертер для создания web-форматов шрифта:

```bash
python convertor.py
```

Это создаст файлы `fin.woff` и `fin.woff2` в папке `fonts/`.

6. Подключите шрифт через CSS (пример в `example/font.css`):

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

7. Используйте шрифт в CSS:

```css
body {
  font-family: "FincubesFont", sans-serif;
}
```

---

## Настройки и доработка

- В `main.py` находится функция конвертации SVG в глифы. Сейчас это заглушка — для продвинутой работы нужно реализовать парсинг SVG путей.
- Можно добавлять новые иконки в `icons/` и обновлять объект эмодзи в `main.py`.
- Можно менять название шрифта и параметры в CSS.

---

## Зависимости

- fonttools
- brotli (для woff2)

Установить:

```bash
pip install -r requirements.txt
```

---

## Лицензия

Этот проект открыт для свободного использования и модификации.
