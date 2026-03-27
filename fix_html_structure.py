import re

html_path = 'index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the extra </div> closing tags before <!-- Education End -->
# The correct sequence should just close col-12, row, and container.
# new_exp ended with </div> (closes timeline-box)
# Then we need </div> (closes col-12)
# Then </div> (closes row)
# Then </div> (closes container)
# Let's cleanly replace the block of closing tags before Education End

bad_block_regex = re.compile(r'</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*<!-- Education End -->', re.DOTALL)

# How many </div> should there be? 
# "Graphic Design" position relative is closed by the last </div> in new_exp string? No, new_exp ends with:
# </ul>
# </div> (closes position-relative)
# </div> (closes timeline-box)
#
# Then we need:
# </div> (closes col-12)
# </div> (closes px-3 row)
# </div> (closes container)
# Let's replace any cluster of </div> prior to <!-- Education End --> with exactly 3 `</div>` tags.
html = re.sub(r'(</div>\s*){4,}<!-- Education End -->', '</div>\\n                        </div>\\n                    </div>\\n                </div>\\n                <!-- Education End -->', html)

# Also fix the literal '\\n' inserted in implement_sections.py
html = html.replace('\\n', '\n')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed HTML structure successfully.")
