
import os
import json

# Configuration
MAP_ID = "260101_tsing_hua_night_market"
MAP_NAME = "清大夜市散步地圖"
MAP_DESC = "2026年清大夜市平價美食散步地圖，收錄經典老店與人氣新秀。"
REGION = "新竹/東區"
LAYER_TYPE = "生活機能"
LAYER_SUBTYPE = "夜市美食"

# Data: Name, Address, Lat, Lng, Description
LOCATIONS = [
    {
        "name": "立晉傳統豆花",
        "lat": 24.797967, "lng": 120.994787,
        "desc": "清夜必吃甜品，招牌是綿密如泡泡冰的糖水冰沙搭配軟嫩豆花。"
    },
    {
        "name": "小洞天",
        "lat": 24.799797, "lng": 120.999500,
        "desc": "在地經典必吃，米腸包香腸配上爽口小黃瓜。"
    },
    {
        "name": "懷香臭臭鍋",
        "lat": 24.797080, "lng": 120.995070,
        "desc": "學生與小資族的最愛，臭豆腐與湯頭口味獨特。"
    },
    {
        "name": "清大雙囍餛飩老虎麵",
        "lat": 24.798000, "lng": 120.997000,
        "desc": "近三十年老店，招牌老虎麵辣勁十足，餛飩飽滿扎實。"
    },
    {
        "name": "吳記蔥蔬餅",
        "lat": 24.798150, "lng": 120.994710,
        "desc": "餅皮加入大量蔬菜與蔥，煎得外酥內軟，份量十足。"
    },
    {
        "name": "蔥大爺餅舖 (阿婆蔥油餅)",
        "lat": 24.799510, "lng": 120.997230,
        "desc": "原阿婆蔥油餅相關，餅皮薄脆，刷上特製辣醬是精華。"
    },
    {
        "name": "大鼓肉夾饃",
        "lat": 24.799014, "lng": 121.000373,
        "desc": "人氣新店，外皮酥脆千層，孜然肉餡香氣濃郁。"
    },
    {
        "name": "車輪餅爺爺",
        "lat": 24.799800, "lng": 121.000500,
        "desc": "脆皮車輪餅，餡料大方，紅豆與奶油是經典。"
    },
    {
        "name": "羅記東山鴨頭",
        "lat": 24.799800, "lng": 121.000500,
        "desc": "入味且外皮微酥，鴨皮與鴨脖子是熱門品項。"
    },
    {
        "name": "郭董脆皮臭豆腐 (老港陳?)",
        "lat": 24.798759, "lng": 120.998248,
        "desc": "清夜內的脆皮臭豆腐選擇，外酥內嫩。"
    },
    {
        "name": "日荃蒸餃",
        "lat": 24.798000, "lng": 120.997000,
        "desc": "高CP值蒸餃，皮薄餡多，搭配酸辣湯是絕配。"
    },
    {
        "name": "紅吱吱牛排館",
        "lat": 24.795499, "lng": 120.998592,
        "desc": "平價牛排首選，提供豐富自助吧，學生最愛。"
    },
    {
        "name": "鳳荷三鮮",
        "lat": 24.793500, "lng": 120.993400,
        "desc": "位於清大校內小吃部，羊肉料理湯頭清甜順口。"
    },
    {
        "name": "飯丸屋 (清大店)",
        "lat": 24.798150, "lng": 120.997320,
        "desc": "沖繩握飯糰專賣，午餐肉與厚蛋組合超受歡迎。"
    },
    {
        "name": "黃記豆花",
        "lat": 24.798089, "lng": 120.997972,
        "desc": "推薦酒釀系列，酒釀蛋與豆花風味獨特。"
    },
    {
        "name": "豆戀迷 Do Re Mi",
        "lat": 24.799778, "lng": 120.996767,
        "desc": "綠豆湯、紅豆湯專賣，推薦加QQ粉角。"
    }
]

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR) # scripts/../
FEATURES_DIR = os.path.join(ROOT_DIR, "features")
MAPS_DIR = os.path.join(ROOT_DIR, "maps")
SQL_DIR = os.path.join(ROOT_DIR, "sql")

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

def generate_id(prefix, name):
    # Simple transliteration or hash could be used, but for now we use safe ASCII check or just id
    # Using a simple counter or hash might be better to avoid Chinese characters in filenames if system doesn't like it.
    # However, user example used `20251212_houli`.
    # Let's use `260101_idx` for simplicity or mapped english names if I had them.
    # I'll use index for stability: `260101_01`, `260101_02`...
    # Actually, let's use a hash of the name to be deterministic but safe? 
    # Or just `260101_{index}`.
    return f"{prefix}_{locations.index(item) + 1:02d}"

locations = LOCATIONS # alias

def main():
    ensure_dir(FEATURES_DIR)
    ensure_dir(MAPS_DIR)
    ensure_dir(SQL_DIR)

    sql_statements = []
    
    # 1. SQL: Insert Layer
    sql_statements.append("-- 1. Insert Layer")
    sql_statements.append(f"""
INSERT OR IGNORE INTO layers (layer_type, layer_subtype, description, meta_data)
VALUES ('{LAYER_TYPE}', '{LAYER_SUBTYPE}', '清大夜市美食商家', '{{}}');
    """)

    # 2. Features
    feature_ids = []
    sql_statements.append("-- 2. Insert Features")
    
    for idx, loc in enumerate(locations):
        fid = f"260101_{idx+1:02d}"
        fname = f"{fid}.md"
        fpath = os.path.join(FEATURES_DIR, fname)
        feature_ids.append(fid)
        
        # Write MD
        md_content = f"""---
id: {fid}
tags: [{LAYER_SUBTYPE}, {LAYER_TYPE}]
---
# {loc['name']}

{loc['desc']}
"""
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        # SQL
        wkt = f"POINT({loc['lng']} {loc['lat']})"
        sql_statements.append(f"""
INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '{fid}', 
    '{loc['name']}', 
    '{loc['desc']}', 
    (SELECT layer_id FROM layers WHERE layer_type='{LAYER_TYPE}' AND layer_subtype='{LAYER_SUBTYPE}' LIMIT 1),
    'POINT', 
    '{wkt}', 
    '{{}}'
);
        """)

    # 3. Map
    map_fname = f"{MAP_ID}.md"
    map_fpath = os.path.join(MAPS_DIR, map_fname)
    
    # Mermaid Graph (Simple Linear or just list?)
    # "散步地圖" implies a route. I'll just connect them 1->2->3... for fun, or just list.
    # Example used `graph TD`.
    mermaid = "graph TD;\n"
    # Let's make a simple route: Start -> End. Or just a cluster.
    # Connecting all 16 linearly might be too long.
    # Let's just connect them in order.
    for i in range(len(locations) - 1):
        mermaid += f"    N{i}[{locations[i]['name']}] --> N{i+1}[{locations[i+1]['name']}];\n"
    mermaid += f"    N{len(locations)-1}[{locations[-1]['name']}];\n"

    # Links
    links = ""
    for idx, loc in enumerate(locations):
        links += f"*   [{loc['name']}](../features/{feature_ids[idx]}.md)\n"

    map_md = f"""---
title: {MAP_NAME}
date: 2026-01-01
---
{mermaid}

{MAP_DESC}

## 景點列表
{links}
"""
    with open(map_fpath, "w", encoding="utf-8") as f:
        f.write(map_md)
        
    # SQL for Map
    sql_statements.append("-- 3. Insert Map")
    # Prepare JSON for meta_data containing routes
    # Actually the example schema says `meta_data TEXT -- JSON (含 key: "routes" 存放 Mermaid 語法定義的路徑)`
    # The 'routes' in DB is often used for rendering.
    meta_json = json.dumps({"routes": mermaid}, ensure_ascii=False)
    
    sql_statements.append(f"""
INSERT INTO walking_maps (map_id, name, description, region, meta_data)
VALUES ('{MAP_ID}', '{MAP_NAME}', '{MAP_DESC}', '{REGION}', '{meta_json}');
    """)

    # 4. Relations
    sql_statements.append("-- 4. Insert Relations")
    for idx, fid in enumerate(feature_ids):
        order = idx + 1
        sql_statements.append(f"""
INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('{MAP_ID}', '{fid}', {order}, 1);
        """)

    # Write SQL file
    sql_out_path = os.path.join(SQL_DIR, f"create_{MAP_ID}.sql")
    with open(sql_out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sql_statements))

    print(f"Successfully generated files for Map: {MAP_NAME}")
    print(f"Features: {len(locations)}")
    print(f"Python script location: {__file__}")
    print(f"SQL script location: {sql_out_path}")

if __name__ == "__main__":
    main()
