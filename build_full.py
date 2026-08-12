import re

html_path = r"C:\Users\Subodh\.gemini\antigravity\brain\589772f6-c6ea-497a-a812-10774e3a20f1\.user_uploaded\media_1786550188421.html"
out_path = r"c:\Users\Subodh\Desktop\Troopod\sections\purelane-homepage.liquid"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove the V2 light mode CSS from the HTML if it exists, since we did this for purelane.css
html = re.sub(r'(?s)/\*\s*={60}\s*\r?\n\s*VERSION 2 - BRAND COLOURS \(light\).*?$', '', html)

# Extract body
body_start = html.find('<body>') + len('<body>')
body_end = html.find('</body>')
body = html[body_start:body_end].strip()

# Inject Shopify asset tags for images and assets? 
# Wait, the HTML has inline base64 images and SVGs, so there are NO external image dependencies except what's in the CSS.
# The user's HTML is fully self-contained!

content = "{% comment %} EXACT FULL HTML REPLICA {% endcomment %}\n"
content += "{{ 'purelane.css' | asset_url | stylesheet_tag }}\n\n"
content += body + "\n\n"
content += "{% schema %}\n{\n  \"name\": \"Purelane Homepage\",\n  \"settings\": [],\n  \"presets\": [\n    {\n      \"name\": \"Purelane Homepage\"\n    }\n  ]\n}\n{% endschema %}"

with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)
