#!/bin/bash

# Script Name: gen_notebooklm_context.sh
# Description: Generates a "Mega Context" Markdown file for NotebookLM by intelligently querying the WalkGIS database.
#              It combines the Map's main markdown file and ONLY its linked Feature files.
# Usage: ./gen_notebooklm_context.sh <MAP_ID>

# 1. 檢查參數
MAP_ID="$1"
if [ -z "$MAP_ID" ]; then
    echo "Usage: $0 <MAP_ID>"
    echo "Example: $0 2025_houfeng_dongfeng_loop"
    exit 1
fi

# 2. 設定路徑與變數
# 取得腳本所在目錄，並推算專案根目錄
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
MAPS_DIR="$PROJECT_ROOT/maps"
FEATURES_DIR="$PROJECT_ROOT/features"
DB_FILE="$PROJECT_ROOT/walkgis.db"
OUTPUT_FILE="$PROJECT_ROOT/walkgis_${MAP_ID}_notebooklm.md"

echo "--- WalkGIS Smart Context Generator ---"
echo "Target Map ID: $MAP_ID"
echo "Database: $DB_FILE"

# 3. 檢查 Map 檔案是否存在
MAP_FILE="$MAPS_DIR/$MAP_ID.md"
if [ ! -f "$MAP_FILE" ]; then
    echo "Error: Map file not found at $MAP_FILE"
    echo "Please ensure the MAP_ID matches the filename in maps/"
    exit 1
fi

echo "Found Map File: $MAP_FILE"
echo "Generating Output: $OUTPUT_FILE"

# 4. 產生 Prompt Header
cat <<EOF > "$OUTPUT_FILE"
# AI INSTRUCTION HEADER
Role: You are an enthusiastic, cartoon-style Travel Guide for the "WalkGIS Adventure".
Tone: Fun, Energetic, Child-friendly, Vibrant, and Imaginative.

## Your Task
Transform this structured GIS data (Map Topology + Feature Details) into a lively "Cartoon Adventure Guide".

## Output Requirements (When asked)
1. **Visual Map Description**: Describe a hand-drawn, Ghibli-style map connecting these specific locations.
2. **Slide Deck Outline**: Create a 10-15 slide presentation structure.
3. **Adventure Story**: Weave a route-based story using the connected features.

---
# DATA: MAP TOPOLOGY
EOF

# 5. 寫入地圖內容
cat "$MAP_FILE" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "# DATA: FEATURES DETAIL" >> "$OUTPUT_FILE"

# 6. 從資料庫查詢關聯的 Feature IDs
# 使用 sqlite3 查詢 walking_map_relations 表
FEATURE_IDS=$(sqlite3 "$DB_FILE" "SELECT feature_id FROM walking_map_relations WHERE map_id = '$MAP_ID' ORDER BY display_order ASC, feature_id ASC;")

if [ -z "$FEATURE_IDS" ]; then
    echo "Warning: No linked features found in database for map '$MAP_ID'."
else
    echo "Found linked features in DB. Processing..."
fi

# 7. 遍歷 Feature IDs 並抓取檔案
COUNT=0
for fid in $FEATURE_IDS; do
    # 嘗試幾種可能的副檔名或命名慣例
    FEATURE_FILE="$FEATURES_DIR/$fid.md"
    
    if [ -f "$FEATURE_FILE" ]; then
        echo "Adding Feature: $fid"
        echo "" >> "$OUTPUT_FILE"
        cat "$FEATURE_FILE" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
        echo "---" >> "$OUTPUT_FILE"
        ((COUNT++))
    else
        echo "Skipping: $fid (File not found: $FEATURE_FILE)"
    fi
done

echo "Done! Added $COUNT features to context file."
echo "File ready: $OUTPUT_FILE"
