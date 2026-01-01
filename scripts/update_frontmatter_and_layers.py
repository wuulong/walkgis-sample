import sqlite3
import os
import re

db_path = "/Users/wuulong/github/walkgis-sample/walkgis.db"
features_dir = "/Users/wuulong/github/walkgis-sample/features"

# Feature configuration
features_config = {
    "260101_01": {"name": "立晉傳統豆花", "subtype": "甜品冰品"},
    "260101_02": {"name": "小洞天", "subtype": "在地小吃"},
    "260101_03": {"name": "懷香臭臭鍋", "subtype": "火鍋"},
    "260101_04": {"name": "清大雙囍餛飩老虎麵", "subtype": "麵食水餃"},
    "260101_05": {"name": "吳記蔥蔬餅", "subtype": "在地小吃"},
    "260101_06": {"name": "蔥大爺餅舖", "subtype": "在地小吃"},
    "260101_07": {"name": "大鼓肉夾饃", "subtype": "異國料理"},
    "260101_08": {"name": "車輪餅爺爺", "subtype": "甜品冰品"},
    "260101_09": {"name": "羅記東山鴨頭", "subtype": "在地小吃"},
    "260101_10": {"name": "郭董脆皮臭豆腐", "subtype": "在地小吃"},
    "260101_11": {"name": "日荃蒸餃", "subtype": "麵食水餃"},
    "260101_12": {"name": "紅吱吱牛排館", "subtype": "排餐"},
    "260101_13": {"name": "鳳荷三鮮", "subtype": "麵食水餃"},
    "260101_14": {"name": "飯丸屋", "subtype": "異國料理"},
    "260101_15": {"name": "黃記豆花", "subtype": "甜品冰品"},
    "260101_16": {"name": "豆戀迷", "subtype": "甜品冰品"},
}

primary_type = "商圈美食"
date_str = "2026-01-01"
# Tags from user request example logic: map name
tags_list = '["清大夜市散步地圖"]'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Setup Layers
print("Setting up layers...")
subtypes = set(f["subtype"] for f in features_config.values())
layer_map = {} # (type, subtype) -> layer_id

for subtype in subtypes:
    # Check if exists
    cursor.execute("SELECT layer_id FROM layers WHERE layer_type = ? AND layer_subtype = ?", (primary_type, subtype))
    row = cursor.fetchone()
    if row:
        layer_id = row[0]
    else:
        cursor.execute("INSERT INTO layers (layer_type, layer_subtype, description) VALUES (?, ?, ?)", 
                       (primary_type, subtype, f"{primary_type} - {subtype}"))
        layer_id = cursor.lastrowid
        print(f"Created new layer: {primary_type}/{subtype} (ID: {layer_id})")
    layer_map[(primary_type, subtype)] = layer_id

conn.commit()

# 2. Update Features (DB & Markdown)
print("Updating features...")

for feature_id, config in features_config.items():
    name = config["name"]
    subtype = config["subtype"]
    layer_id = layer_map[(primary_type, subtype)]
    
    # Update DB
    cursor.execute("UPDATE walking_map_features SET layer_id = ? WHERE feature_id = ?", (layer_id, feature_id))
    
    # Read Markdown to get coordinate if it exists (it should from previous step)
    file_path = os.path.join(features_dir, f"{feature_id}.md")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract coordinate
    coord_match = re.search(r"coordinate: (\[.*?\])", content)
    coordinate_str = coord_match.group(1) if coord_match else "[0.0, 0.0]"
    
    # Build new Frontmatter
    new_frontmatter = f"""---
id: {feature_id}
name: {name}
type: {primary_type}
subtype: {subtype}
date: {date_str}
coordinate: {coordinate_str}
tags: {tags_list}
---
"""
    
    # Replace old frontmatter
    # Split by the second '---'
    parts = re.split(r"^---\s*$", content, maxsplit=2, flags=re.MULTILINE)
    
    if len(parts) >= 3:
        # parts[0] is empty (before first ---)
        # parts[1] is old frontmatter
        # parts[2] is body
        markdown_body = parts[2]
        # Remove the Title line if it looks like "# Name" because we moved Name to frontmatter?
        # User didn't say to remove the title from body, but usually if name is in frontmatter, 
        # the body might still keep it or not. The user example didn't show the body. 
        # I'll keep the body as is for now to avoid losing info.
        
        new_content = new_frontmatter + markdown_body
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {feature_id}.md")
    else:
        print(f"Could not parse frontmatter for {feature_id}")

conn.commit()
conn.close()
print("Done.")
