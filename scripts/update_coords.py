import os
import re
import sqlite3

# Define the coordinates (Latitude, Longitude)
# Approximated based on specific addresses in Hsinchu Tsing Hua Night Market area
coords_map = {
    "260101_01": [24.79805, 120.99750], # 立晉傳統豆花
    "260101_02": [24.79780, 120.99720], # 小洞天
    "260101_03": [24.79782, 120.99722], # 懷香臭臭鍋
    "260101_04": [24.79720, 120.99800], # 清大雙囍餛飩老虎麵
    "260101_05": [24.79800, 120.99745], # 吳記蔥蔬餅
    "260101_06": [24.79700, 120.99850], # 蔥大爺餅舖
    "260101_07": [24.79700, 120.99600], # 大鼓肉夾饃
    "260101_08": [24.79790, 120.99730], # 車輪餅爺爺
    "260101_09": [24.79792, 120.99732], # 羅記東山鴨頭
    "260101_10": [24.79850, 120.99820], # 郭董脆皮臭豆腐
    "260101_11": [24.79722, 120.99802], # 日荃蒸餃
    "260101_12": [24.79710, 120.99580], # 紅吱吱牛排館
    "260101_13": [24.79350, 120.99300], # 鳳荷三鮮
    "260101_14": [24.79750, 120.99750], # 飯丸屋
    "260101_15": [24.79730, 120.99680], # 黃記豆花
    "260101_16": [24.79790, 120.99730], # 豆戀迷
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
            
            # Check if coordinate already exists
            if "coordinate:" not in content:
                # Insert coordinate after tags
                # Pattern: find the tags line (e.g., tags: [...]) and insert new line after
                pattern = r"(tags: \[.*?\])"
                replacement = f"\\1\ncoordinate: [{lat}, {lon}]"
                new_content = re.sub(pattern, replacement, content)
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated {filename}")
                else:
                    print(f"Skipped {filename} (Regex match failed or not needed)")
            else:
                 print(f"Skipped {filename} (coordinate already exists)")

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
