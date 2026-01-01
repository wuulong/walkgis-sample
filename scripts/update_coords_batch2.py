import os
import re
import sqlite3

# Define the coordinates (Latitude, Longitude)
# From Google Maps Batch 2
coords_map = {
    "260101_05": [24.7965548, 120.9982133], # 吳記蔥蔬餅
    "260101_06": [24.798642, 120.9974454], # 蔥大爺餅舖
    "260101_07": [24.797161, 120.9967356], # 大鼓肉夾饃
    "260101_08": [24.7983329, 120.996726], # 車輪餅爺爺 (Approx. via 日荃蒸餃)
}

features_dir = "/Users/wuulong/github/walkgis-sample/features"
db_path = "/Users/wuulong/github/walkgis-sample/walkgis.db"

# 1. Update Markdown Files
print("Updating Markdown files...")
for filename in os.listdir(features_dir):
    if filename.endswith(".md"):
        feature_id = os.path.splitext(filename)[0]
        if feature_id in coords_map:
            lat, lon = coords_map[feature_id]
            file_path = os.path.join(features_dir, filename)
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace existing coordinate line
            # coordinate: [24.79805, 120.9975]
            pattern = r"coordinate: \[.*?\]"
            replacement = f"coordinate: [{lat}, {lon}]"
            new_content = re.sub(pattern, replacement, content)
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                 print(f"Skipped {filename} (No change or not found)")

# 2. Update SQLite Database
print("Updating Database...")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

for feature_id, (lat, lon) in coords_map.items():
    # WKT format: POINT(lon lat)
    wkt = f"POINT({lon} {lat})"
    cursor.execute(
        "UPDATE walking_map_features SET geometry_wkt = ? WHERE feature_id = ?",
        (wkt, feature_id)
    )
    if cursor.rowcount > 0:
        print(f"DB Updated {feature_id}: {wkt}")
    else:
        print(f"DB Record not found for {feature_id}")

conn.commit()
conn.close()
print("Done.")
