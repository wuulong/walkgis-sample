import os
import re
import sqlite3

# Define the coordinates (Latitude, Longitude)
# From Google Maps Batch 1
coords_map = {
    "260101_01": [24.7968636, 120.9983978], # 立晉傳統豆花
    "260101_02": [24.7967452, 120.9990578], # 小洞天
    "260101_03": [24.796453, 120.9988518], # 懷香臭臭鍋
    "260101_04": [24.7980131, 120.9965787], # 清大雙囍餛飩老虎麵
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
