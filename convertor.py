from fontTools.ttLib import TTFont


def convert_ttf_to_woff(ttf_path, woff_path):
    font = TTFont(ttf_path)
    font.flavor = 'woff'
    font.save(woff_path)


def convert_ttf_to_woff2(ttf_path, woff2_path):
    font = TTFont(ttf_path)
    font.flavor = 'woff2'
    font.save(woff2_path)


if __name__ == "__main__":
    ttf_file = "fonts/fin.ttf"
    convert_ttf_to_woff(ttf_file, "fonts/fin.woff")
    convert_ttf_to_woff2(ttf_file, "fonts/fin.woff2")
