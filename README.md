# 🧱 FinCubes Font Builder

Генератор цветного шрифта на основе SVG-эмодзи, с использованием [nanoemoji](https://github.com/googlefonts/nanoemoji) и [fontTools](https://github.com/fonttools/fonttools).

---

## 📦 Возможности

- ✅ Поддержка цветных эмодзи через формат `glyf_colr_1`
- 🔀 Преобразование SVG-файлов в шрифтовые глифы
- 📤 Экспорт в `.ttf`, `.woff`, `.woff2`
- 🌐 Готовность к использованию через веб (CDN)
- 🧪 Простая система проверки/предпросмотра

---

## ⚙️ Установка

1. Установи зависимости Python:

```bash
pip install -r requirements.txt
```

---

## 🚀 Использование

1. Помести SVG-иконки в папку `icons/`

2. В `main.py` обнови словарь `emojis`:

```python
emojis = {
    'icons/apnea.svg': '🤿',
    'icons/surface.svg': '🌊',
    ...
}
```

3. Запусти скрипт:

```bash
python main.py
```

После выполнения ты получишь:

- Готовые шрифты в `build/fonts/`
- Переименованные финальные версии в `dist/`, готовые к публикации через CDN

---

## 🌍 Подключение на сайте

В директории `dist` создаются все нужные файлы. Ниже пример подключения в HTML:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <style>
      @import url("https://cdn.fincubes.ru/fonts/fincubesfont.css");
      body {
        font-family: "FinCubes", sans-serif;
        font-size: 64px;
      }
    </style>
  </head>
  <body>
    <div class="emoji">🤿 🌊 👟 🫧</div>
  </body>
</html>
```

---

## 🧠 FAQ

### Как работает `emoji_to_filename`?

Переименование происходит в формат `uXXXX.svg`, который ожидает `nanoemoji`.

---

## 📜 Лицензия

Apache License 2.0 — используйте свободно.

---

## ✨ Авторы

- 👤 @lordcod
