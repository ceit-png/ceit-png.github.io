import re
from pathlib import Path
root = Path('d:/ceit-png.github.io/_drafts')
files = list(root.rglob('*.html'))

badge_map = {
    '#c9b037': 'badge-gold',
    '#ad8a56': 'badge-olive',
    '#d7d7d7': 'badge-silver',
    '#af9500': 'badge-bronze',
    '#339fff': 'badge-blue',
    '#ff3f33': 'badge-red',
    '#ffc733': 'badge-yellow',
}
prop_map = {
    ('cursor', 'pointer'): 'cursor-pointer',
    ('color', 'white'): 'text-white',
    ('font-size', '12px'): 'text-xs',
    ('padding-top', '15px'): 'pt-15',
    ('padding-top', '0px'): 'pt-0',
    ('padding-left', '76px'): 'pl-76',
    ('padding-left', '20px'): 'pl-20',
    ('width', '100%'): 'full-width',
    ('position', 'absolute'): 'position-absolute',
}
strip_props = {('text-align', 'none')}

TAG_RE = re.compile(r'<(?P<tag>[a-zA-Z][^<>]*?)>', re.S)
ATTR_RE = re.compile(r'(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*(?P<quote>["\'])(?P<value>.*?)(?P=quote)', re.S)
STYLE_RE = re.compile(r'([\w-]+)\s*:\s*([^;]+)\s*(?:;|$)')

changed_files = []
for path in files:
    text = path.read_text(encoding='utf-8')
    original = text
    def process_tag(match):
        tag = match.group(0)
        if 'style=' not in tag.lower():
            return tag
        attrs = list(ATTR_RE.finditer(tag))
        style_match = next((m for m in attrs if m.group('name').lower() == 'style'), None)
        if not style_match:
            return tag
        class_match = next((m for m in attrs if m.group('name').lower() == 'class'), None)
        style_value = style_match.group('value')
        classes_to_add = []
        new_styles = []
        has_table_layout = False
        has_width_100 = False
        for prop, val in STYLE_RE.findall(style_value):
            key = (prop.strip().lower(), val.strip().lower())
            if key[0] == 'background-color' and key[1] in badge_map:
                classes_to_add.append(badge_map[key[1]])
                continue
            if key in prop_map:
                classes_to_add.append(prop_map[key])
                if key == ('table-layout', 'fixed'):
                    has_table_layout = True
                if key == ('width', '100%'):
                    has_width_100 = True
                continue
            if key == ('table-layout', 'fixed'):
                has_table_layout = True
                continue
            if key == ('width', '100%'):
                has_width_100 = True
                continue
            if key in strip_props:
                continue
            new_styles.append(f'{prop.strip()}: {val.strip()}')
        if has_table_layout and has_width_100 and 'table-fixed' not in classes_to_add:
            classes_to_add.append('table-fixed')
        if not classes_to_add and len(new_styles) == len(STYLE_RE.findall(style_value)):
            return tag
        # update class attr
        new_tag = tag
        if class_match:
            old_classes = class_match.group('value').strip()
            combined = ' '.join([old_classes] + classes_to_add).strip()
            new_tag = new_tag[:class_match.start('value')] + combined + new_tag[class_match.end('value'):]
        elif classes_to_add:
            insert_pos = new_tag.rfind('>')
            if insert_pos == -1:
                insert_pos = len(new_tag)
            if new_tag[insert_pos-1] == '/':
                insert_pos -= 1
            new_tag = new_tag[:insert_pos] + ' class="' + ' '.join(classes_to_add) + '"' + new_tag[insert_pos:]
        # update style attr
        if new_styles:
            new_style_value = '; '.join(new_styles) + ';'
            new_tag = re.sub(r'style\s*=\s*(?:"[^"]*"|\'[^\']*\')', f'style="{new_style_value}"', new_tag, count=1)
        else:
            new_tag = re.sub(r'\s*style\s*=\s*(?:"[^"]*"|\'[^\']*\')', '', new_tag, count=1)
        return new_tag
    text = TAG_RE.sub(process_tag, text)
    if text != original:
        path.write_text(text, encoding='utf-8')
        changed_files.append(str(path.relative_to(root.parent)))
print('changed', len(changed_files), 'files')
for f in changed_files:
    print(f)
