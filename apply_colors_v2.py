import re

css_path = 'css/style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace primary color (#6366f1 to #e5b161)
css = css.replace('#6366f1', '#e5b161')
css = css.replace('#6366F1', '#e5b161')

# Replace hover state of primary (#4f46e5 to #c89a54 - darker gold)
css = css.replace('#4f46e5', '#c89a54')

# Replace rgba tint used in service-item icons & shadow
css = css.replace('rgba(99, 102, 241,', 'rgba(229, 177, 97,')

# Use secondary color (#f4dbc2) for the page background to create the dual-tone warm aesthetic
css = css.replace('background-color: #f8fafc;', 'background-color: #f4dbc2;')

# Optionally, override secondary variable
css = css.replace('--secondary: #6c757d;', '--secondary: #f4dbc2;')

# Make the dark sidebar have a slight warm tint instead of a cool blue tint
css = css.replace('linear-gradient(135deg, #1e1e2f, #0f172a)', 'linear-gradient(135deg, #2a221b, #17110c)')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Colors applied successfully.")
