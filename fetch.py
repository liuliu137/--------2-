# -*- coding: utf-8 -*-
import urllib.request, os, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
assets = r"C:\Users\admin\Doubao\chats\2026-10-17\new-chat\养老服务信息平台\assets"
os.makedirs(assets, exist_ok=True)
candidates = {
    "three.min.js": [
        "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js",
        "https://unpkg.com/three@0.128.0/build/three.min.js",
    ],
    "OrbitControls.js": [
        "https://unpkg.com/three@0.128.0/examples/js/controls/OrbitControls.js",
        "https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js",
    ],
    "echarts.min.js": [
        "https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.3/echarts.min.js",
        "https://unpkg.com/echarts@5.4.3/dist/echarts.min.js",
    ],
    "earth.jpg": [
        "https://unpkg.com/three-globe@2.31.0/example/img/earth-blue-marble.jpg",
        "https://cdn.jsdelivr.net/npm/three-globe@2.31.0/example/img/earth-blue-marble.jpg",
    ],
}
for name, urls in candidates.items():
    ok = False
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=40) as r:
                data = r.read()
            if len(data) < 20000:
                print("TOOSMALL", name, len(data)); continue
            with open(os.path.join(assets, name), "wb") as f:
                f.write(data)
            print("OK", name, len(data))
            ok = True
            break
        except Exception as e:
            print("FAIL", name, url, repr(e))
    if not ok:
        print("ALLFAIL", name)
