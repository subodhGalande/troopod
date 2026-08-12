import re

html_path = r'C:\Users\Subodh\.gemini\antigravity\brain\589772f6-c6ea-497a-a812-10774e3a20f1\.user_uploaded\media_1786550188421.html'
out_path = r'c:\Users\Subodh\Desktop\Troopod\snippets\purelane-parallax-bg.liquid'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Get the scenes div
bg_start = html.find('<div class="scenes"')
bg_end = html.find('<div class="vig"></div>\n</div>') + len('<div class="vig"></div>\n</div>')
bg = html[bg_start:bg_end]

# Get the entire script tag at the bottom
script_start = html.rfind('<script>')
script_end = html.rfind('</script>') + len('</script>')
script = html[script_start:script_end]

# We should fix the header ID in the script since our header section is different.
# Or better yet, we can leave it as is if we fix the header ID in the header liquid.
# In the original, header is id="hdr". We will just use 'hdr'.
script = script.replace("document.getElementById('hdr')", "document.getElementById('shopify-section-purelane-header')")

out = "{% comment %} PURELANE PARALLAX BACKGROUND AND GLOBAL SCRIPTS {% endcomment %}\n" + bg + "\n" + script

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(out)
