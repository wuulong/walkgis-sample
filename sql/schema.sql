CREATE TABLE layers (
    layer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    layer_type TEXT NOT NULL,                         -- 主分類 (例如：水文與親水層, 生態與景觀層)
    layer_subtype TEXT,                               -- 次分類 (例如：親水點, 河床路徑入口, 合法車泊點)
    qgis_qml TEXT,                                    -- 儲存 QGIS Style (QML 格式的 XML 字串或片段)，用於定義該圖層的視覺呈現
    description TEXT,                                 -- 該圖層的說明 (Markdown 格式)
    meta_data TEXT,                                   -- JSON 格式的備註資訊 (例如：{"source_url": "...", "last_updated": "..."})
    UNIQUE(layer_type, layer_subtype)                 -- 確保 layer_type 和 layer_subtype 的組合是唯一的
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE meta_data_templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    template_name TEXT NOT NULL UNIQUE,       -- 範本名稱 (例如：親水點通用範本, 合法車泊點範本)
    applies_to_layer_type TEXT NOT NULL,      -- 此範本適用的圖層類型
    applies_to_subtype TEXT,                  -- 此範本適用的子類型
    template_json TEXT NOT NULL,              -- 儲存完整的 JSON 範例字串
    description TEXT                          -- 範本的簡要說明或用途 (Markdown 格式)
);
CREATE TABLE walking_map_features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature_id TEXT UNIQUE,                     -- 【新增】唯一識別碼 (例如: 20251212_houli)，對應 features/ 目錄下的 Markdown 檔名
    name TEXT NOT NULL,                         -- 特徵名稱 (例如：后里馬場、大甲溪河流線、緩衝區範圍)
    description TEXT,                           -- 特徵簡要描述 (Markdown 格式)
    layer_id INTEGER NOT NULL,                  -- 外鍵，關聯到 layers.layer_id
    geometry_type TEXT NOT NULL,                -- 幾何類型 (例如：Point, LineString, Polygon) - 用於應用層快速判斷
    geometry_wkt TEXT NOT NULL,                 -- 【核心修改】使用 WKT (Well-Known Text) 純文字儲存幾何資料，AI 可讀
    meta_data TEXT,                             -- JSON 格式的非核心屬性
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 創建時間
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- 最後更新時間
    FOREIGN KEY (layer_id) REFERENCES layers(layer_id)
);
CREATE INDEX idx_features_layer ON walking_map_features(layer_id);
CREATE INDEX idx_features_fid ON walking_map_features(feature_id);
CREATE TABLE walking_maps (
    map_id TEXT PRIMARY KEY,        -- 唯一 ID (e.g., '2025_houfeng_bikeway')
    name TEXT NOT NULL,             -- 名稱 (e.g., '后豐鐵馬道精華遊')
    description TEXT,               -- 描述
    cover_image TEXT,               -- 封面圖路徑 (assets/...)
    region TEXT,                    -- 地區 (e.g., '台中/后里')
    meta_data TEXT,                 -- JSON (含 key: "routes" 存放 Mermaid 語法定義的路徑)
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE walking_map_relations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    map_id TEXT NOT NULL,           -- FK -> walking_maps.map_id
    feature_id TEXT NOT NULL,       -- FK -> walking_map_features.feature_id
    display_order INTEGER,          -- UI 列表顯示順序 (可為 NULL)
    is_highlight BOOLEAN DEFAULT 0, -- 是否為重點標註
    note TEXT,                      -- 自訂註解
    FOREIGN KEY (map_id) REFERENCES walking_maps(map_id),
    FOREIGN KEY (feature_id) REFERENCES walking_map_features(feature_id),
    UNIQUE(map_id, feature_id)      -- 防止重複加入
);
