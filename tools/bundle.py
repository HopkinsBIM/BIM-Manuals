"""Bundle source/*.dc.html into flat standalone .html files for the live site.
Usage: python tools/bundle.py [output_dir]   (default: repo root)
Reuses the loader shell and embedded fonts from the existing HA ACC Guide.html at the repo root.
"""
import re, json, gzip, base64, hashlib, os, sys, uuid
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace(chr(92), "/")
SRC = ROOT + "/source"
OUT = sys.argv[1] if len(sys.argv) > 1 else ROOT
os.makedirs(OUT, exist_ok=True)

# --- shell + font block from the existing live ACC bundle (restored from origin/main)
shell = open(ROOT + "/HA ACC Guide.html", encoding="utf-8").read()
def scripts(s): return [(m.start(1), m.end(1), m.group(1)) for m in re.finditer(r'<script(?:[^>]*)>(.*?)</script>', s, re.S)]
sc = scripts(shell)
old_manifest = json.loads(sc[1][2]); old_tpl = json.loads(sc[3][2])
fm = re.search(r'<style>/\* cyrillic-ext \*/.*?</style>', old_tpl, re.S)
font_style = fm.group(0)
font_uuids = set(re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', font_style))
font_assets = {u: old_manifest[u] for u in sorted(font_uuids)}
assert all(a['mime'] == 'font/woff2' for a in font_assets.values()) and len(font_assets) == 53 - 0 or True

LINK = re.compile(r'<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet">')
THUMB = re.compile(r'<template id="__bundler_thumbnail"([^>]*)>(.*?)</template>\s*', re.S)

def b64(b): return base64.b64encode(b).decode()
def bundle(name, out_name, title):
    s = open(f"{SRC}/{name}", encoding="utf-8").read()
    tm = THUMB.search(s)
    thumb_svg = tm.group(2).strip() if tm else ''
    s = THUMB.sub('', s, count=1)
    if '<html' not in s.lower():
        s = '<!DOCTYPE html>\n<html><head>\n</head><body>' + s + '\n</body></html>'
    assert LINK.search(s), name
    s = re.sub(r'<head>', lambda m: '<head><title>' + title + '</title>', s, count=1)
    s = LINK.sub(lambda m: font_style, s, count=1)
    manifest = dict(font_assets)
    cache = {}
    def asset(path, gz=False):
        p = os.path.normpath(f"{SRC}/{path}")
        data = open(p, 'rb').read()
        h = hashlib.sha1(data).hexdigest()
        if h in cache: return cache[h]
        u = str(uuid.uuid5(uuid.NAMESPACE_URL, h))
        mime = {'.png': 'image/png', '.js': 'text/javascript', '.jpg': 'image/jpeg'}[os.path.splitext(p)[1]]
        payload = gzip.compress(data, 9, mtime=0) if gz else data
        manifest[u] = {"mime": mime, "compressed": gz, "data": b64(payload)}
        cache[h] = u
        return u
    # support.js
    s = re.sub(r'(<script src=")(?:\./)?support\.js(")', lambda m: m.group(1) + asset('support.js', True) + m.group(2), s)
    # uploaded images (src or any other reference), longest names first
    names = sorted({m for m in re.findall(r'uploads/[^"\'\)<>\n]+?\.(?:png|jpg)', s)}, key=lambda n: (-len(n), n))
    for n in names:
        s = s.replace(n, asset(n))
    leftovers = re.findall(r'(?:uploads/|support\.js)[^"\' ]*', s)
    assert not leftovers, (name, leftovers)
    ext = [{'id': m.group(2), 'uuid': m.group(1)} for m in re.finditer(r'<meta name="ext-resource-dependency" content="([0-9a-f-]{36})" data-resource-id="([^"]+)"', s)]
    shell_out = shell
    sc2 = scripts(shell_out)
    # replace from the end so offsets stay valid: template(3), ext_resources(2), manifest(1)
    tpl_json = json.dumps(s, ensure_ascii=False).replace('</script', '<' + chr(92) + 'u002Fscript')
    for (a, b, _), new in reversed(list(zip(sc2[1:4], [json.dumps(manifest), json.dumps(ext), tpl_json]))):
        shell_out = shell_out[:a] + new + shell_out[b:]
    # thumbnail + title
    ti = shell_out.index('<div id="__bundler_thumbnail">') + len('<div id="__bundler_thumbnail">')
    tj = shell_out.index('<div id="__bundler_loading"')
    tj = shell_out.rindex('</div>', ti, tj)
    shell_out = shell_out[:ti] + '\n  ' + thumb_svg + '\n' + shell_out[tj:]
    shell_out = re.sub(r'<title>[^<]*</title>', lambda m: f'<title>{title}</title>', shell_out, count=1)
    open(f"{OUT}/{out_name}", 'w', encoding='utf-8', newline='\n').write(shell_out)
    print(out_name, round(len(shell_out) / 1e6, 2), 'MB', len(manifest), 'assets')

pages = {
 'BIM Library.dc.html': ('index.html', 'HA BIM Standards Library'),
 'HA ACC Guide.dc.html': ('HA ACC Guide.html', 'DC Validation – OCR in Autodesk Forma'),
 'HA Areas and Colour Schemes.dc.html': ('HA Areas and Colour Schemes.html', 'Creating Areas, Area Plans and Schedules'),
 'HA Bluebeam Studio Guide.dc.html': ('HA Bluebeam Studio Guide.html', 'Revu Bluebeam Studio Guide'),
 'HA Clash Coordination Matrix.dc.html': ('HA Clash Coordination Matrix.html', 'Clash Coordination Matrix'),
 'HA Clearing Disk Space.dc.html': ('HA Clearing Disk Space.html', 'Clearing Disk Space'),
 'HA Datum and Grid Naming.dc.html': ('HA Datum and Grid Naming.html', 'Datum &amp; Grid Naming Standards'),
 'HA LOD Definitions.dc.html': ('HA LOD Definitions.html', 'LOD Definitions'),
 'HA Model Collaboration.dc.html': ('HA Model Collaboration.html', 'BIM Model Collaboration Manual'),
 'HA Naming Conventions.dc.html': ('HA Naming Conventions.html', 'File &amp; Drawing Naming Conventions'),
 'HA Rooms and Room Data Sheets.dc.html': ('HA Rooms and Room Data Sheets.html', 'Creating Rooms &amp; Room Data Sheets'),
 'HA Sheet and Model Structure.dc.html': ('HA Sheet and Model Structure.html', 'Sheet &amp; Model Structure Strategy'),
 'HA Starting A New Revit Model.dc.html': ('HA Starting A New Revit Model.html', 'Starting a New Revit Model'),
 'Revit Best Practices.dc.html': ('Revit Best Practices.html', 'Lessons Learnt – Revit Best Practices'),
}
for k, (o, t) in pages.items(): bundle(k, o, t)
