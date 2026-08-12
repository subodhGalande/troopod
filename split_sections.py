import re
import os

html_path = r"C:\Users\Subodh\.gemini\antigravity\brain\589772f6-c6ea-497a-a812-10774e3a20f1\.user_uploaded\media_1786550188421.html"
out_dir = r"c:\Users\Subodh\Desktop\Troopod\sections"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove the V2 light mode CSS so the background stays dark green, since the user explicitly pointed to the V1 dark mode green background.
html = re.sub(r'(?s)/\*\s*={60}\s*\r?\n\s*VERSION 2 - BRAND COLOURS \(light\).*?$', '', html)

def write_section(name, marker, schema_name):
    # Find start of section
    start_str = f"<!-- ================= {marker} ================= -->"
    start_idx = html.find(start_str)
    if start_idx == -1: return
    
    # Find next section or </main> or </body>
    next_idx = html.find("<!-- ================= ", start_idx + len(start_str))
    if next_idx == -1: next_idx = html.find("</body>", start_idx)
    
    chunk = html[start_idx:next_idx].strip()
    # If the chunk contains </main>, trim it
    chunk = chunk.replace("</main>", "").strip()
    
    file_path = os.path.join(out_dir, f"{name}.liquid")
    
    content = f"{{% comment %}} EXACT HTML REPLICA {{% endcomment %}}\n\n"
    if name == "purelane-hero":
        content += "{{ 'purelane.css' | asset_url | stylesheet_tag }}\n"
    
    content += chunk + "\n\n"
    content += f"{{% schema %}}\n{{\n  \"name\": \"{schema_name}\",\n  \"settings\": [],\n  \"presets\": [\n    {{\n      \"name\": \"{schema_name}\"\n    }}\n  ]\n}}\n{{% endschema %}}"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

write_section("purelane-ticker", "TICKER", "Purelane Ticker")
write_section("purelane-header", "NAV", "Purelane Header")
write_section("purelane-hero", "HERO", "Purelane Hero")
write_section("purelane-reviews", "CUSTOMER REVIEWS (auto marquee)", "Purelane Reviews")
write_section("purelane-ingredients", "INGREDIENTS", "Purelane Ingredients")
write_section("purelane-pillars", "PILLARS", "Purelane Pillars")
write_section("purelane-proof", "PROOF", "Purelane Proof")
write_section("purelane-combos", "BEST SELLING COMBOS", "Purelane Combos")
write_section("purelane-bundles", "BUNDLES", "Purelane Bundles")
write_section("purelane-shop", "SHOP", "Purelane Shop")
write_section("purelane-range", "FULL RANGE", "Purelane Range")
write_section("purelane-why-bundles", "WHY BUNDLES BEAT BUYING SINGLE", "Purelane Why Bundles")
write_section("purelane-categories", "FIND THE RIGHT BUNDLE", "Purelane Categories")
write_section("purelane-trust-signup", "TRUST BAR", "Purelane Trust")

# Signup is combined with Trust Bar in the original layout if it's right after it? 
# Wait, Signup has its own marker
write_section("purelane-signup", "SIGNUP", "Purelane Signup")
write_section("purelane-footer", "FOOTER", "Purelane Footer")
write_section("purelane-sticky-cta", "STICKY CTA", "Purelane Sticky CTA")

