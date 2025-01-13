# -*- coding: utf-8 -*-
"""
PDF EXTRACTION
@author: omar.khan
"""

import pypdf
import pandas as pd

def style_codes(x):
    styles = []
    for pos, char in enumerate(x):
        if char in 'TOTAL':
            styles.append(pos + 1)

    pos = 0
    new_styles = []
    for i in styles:
        if '-' in x[styles[pos]] and x[styles[pos]].count('-') == 1 and '.' in x[styles[pos]]:
            new_styles.append(x[styles[pos]])
            pos += 1
        else:
            pos += 1

    return new_styles

def color(x): 
    colors = []

    for pos, char in enumerate(x):
        if 'M.ID' in char :
            colors.append(char)

    return colors 

def customs(x):
    cust = []

    for pos, char in enumerate(x):
        if 'M.ID' in char :
            a = pos + 3
            try:  
                int(x[a][-1])
                if '/' not in x[a] and '.' not in x[a] and len(x[a]) >= 4:
                    cust.append(a)
            except:
                pass

            a = pos + 4 
            try: 
                int(x[a][-1])
                if '/' not in x[a] and '.' not in x[a] and len(x[a]) >= 4:
                    cust.append(a)
            except:
                pass

            a = pos + 5
            try: 
                int(x[a][-1])
                if '/' not in x[a] and '.' not in x[a] and len(x[a]) >= 4:
                    cust.append(a)
            except:
                pass

            a = pos + 6
            try: 
                int(x[a][-1])
                if '/' not in x[a] and '.' not in x[a] and len(x[a]) >= 4:
                    cust.append(a)
            except:
                pass

            a = pos + 7
            try: 
                int(x[a][-1])
                if '/' not in x[a] and '.' not in x[a] and len(x[a]) >= 4:
                    cust.append(a)
            except:
                pass
  
        # try except blocks for the diff cases
    pos = 0
    new_cust = []
    for i in cust:
        new_cust.append(x[cust[pos]])
        pos += 1

    return new_cust


def qty(x):
    qt = []
    for pos, char in enumerate(x):
        if char == 'QTY:':
            qt.append(pos + 1)

    pos = 0
    new_qty = []
    for i in qt:
        new_qty.append(x[qt[pos]])
        pos += 1
    return new_qty

def grossamt(x):
    ga = []
    for pos, char in enumerate(x):
        if char == 'QTY:':
            fchar = pos + 4
            schar = pos + 5
            conc = x[fchar] + ' ' + x[schar]
            ga.append(conc)
    return ga

#CHANGE THE FILE PATH 
pdf_path = "/Users/omarkhan/Desktop/JACQUEMUS.pdf"

all_style_codes = []
all_color = []
all_customs = []
all_qty = []
all_gmt = []


reader = pypdf.PdfReader(pdf_path)
num_pages = len(reader.pages)


for pageno in range(num_pages):
    page = reader.pages[pageno]
    text = page.extract_text(extraction_mode="layout")
    x = text.split()

    styles_on_page = style_codes(x)
    all_style_codes.extend(styles_on_page)

    all_color_on_page = color(x)
    all_color.extend(all_color_on_page) 

    customs_on_page = customs(x)
    all_customs.extend(customs_on_page)

    qty_on_page = qty(x)
    all_qty.extend(qty_on_page) 

    gmt_on_page = grossamt(x)
    all_gmt.extend(gmt_on_page)


all_styles_final = [i[0:13] for i in all_style_codes]

df = pd.DataFrame({
    'Style': all_styles_final,
    'ID': all_color, 
    'Code_No': all_customs, 
    'Total_Qty': all_qty,
    'Amount': all_gmt
})

print(df)

# df.to_csv('')
