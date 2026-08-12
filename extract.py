import re

html_path = r'C:\Users\Subodh\.gemini\antigravity\brain\589772f6-c6ea-497a-a812-10774e3a20f1\.user_uploaded\media_1786550188421.html'
out_path = r'c:\Users\Subodh\Desktop\Troopod\snippets\purelane-parallax-bg.liquid'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

bg_start = html.find('<div class="scenes"')
bg_end = html.find('<div class="vig"></div>\n</div>') + len('<div class="vig"></div>\n</div>')
bg = html[bg_start:bg_end]

script_start = html.find('  /* ---------- scene crossfade (scroll driven, deterministic) ---------- */')
script_end = html.find('  /* ---------- ambient drift on the hero product ---------- */')
script = html[script_start:script_end]

out = "{% comment %} PURELANE PARALLAX BACKGROUND (1:1 V1 DARK) {% endcomment %}\n" + bg + "\n<script>\n(function () {\n  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n" + script + "\n  /* ---------- parallax + header ---------- */\n  var hdr = document.getElementById('shopify-section-purelane-header');\n  var raf = null, mx = 0, my = 0;\n\n  function frame() {\n    raf = null;\n    var y = window.scrollY || window.pageYOffset;\n    if (hdr) hdr.classList.toggle('up', y > 90);\n    if (!reduce) {\n      var wl = document.querySelectorAll('#water .wl');\n      for (var i = 0; i < wl.length; i++) {\n        var d = [0.05, 0.09, 0.03, 0.02][i] || 0.05;\n        wl[i].style.setProperty('--px', (mx * d * 130).toFixed(1) + 'px');\n        wl[i].style.setProperty('--py', (-y * d + my * d * 90).toFixed(1) + 'px');\n      }\n    }\n    pickScene();\n  }\n  function onScroll() { if (!raf) raf = requestAnimationFrame(frame); }\n  window.addEventListener('scroll', onScroll, { passive: true });\n  window.addEventListener('resize', onScroll);\n\n  if (!reduce && window.matchMedia('(min-width: 1024px)').matches) {\n    window.addEventListener('mousemove', function (e) {\n      mx = (e.clientX / window.innerWidth - 0.5) * 2;\n      my = (e.clientY / window.innerHeight - 0.5) * 2;\n      onScroll();\n    }, { passive: true });\n  }\n})();\n</script>"

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(out)
