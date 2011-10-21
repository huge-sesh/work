import sheet

resource = {}
def get(idx): return resource[idx]
def set(idx, val): resource[idx] = val

resource['characters'] = sheet.Sheet('image/lofi_char.png', 16, 31, 8, 8)
resource['blocks'] = sheet.Sheet('image/bugtilesgreentest.png', 29, 32, 16, 16)
