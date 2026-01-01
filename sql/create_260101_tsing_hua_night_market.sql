-- 1. Insert Layer

INSERT OR IGNORE INTO layers (layer_type, layer_subtype, description, meta_data)
VALUES ('生活機能', '夜市美食', '清大夜市美食商家', '{}');
    
-- 2. Insert Features

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_01', 
    '立晉傳統豆花', 
    '清夜必吃甜品，招牌是綿密如泡泡冰的糖水冰沙搭配軟嫩豆花。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.994787 24.797967)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_02', 
    '小洞天', 
    '在地經典必吃，米腸包香腸配上爽口小黃瓜。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.9995 24.799797)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_03', 
    '懷香臭臭鍋', 
    '學生與小資族的最愛，臭豆腐與湯頭口味獨特。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.99507 24.79708)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_04', 
    '清大雙囍餛飩老虎麵', 
    '近三十年老店，招牌老虎麵辣勁十足，餛飩飽滿扎實。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.997 24.798)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_05', 
    '吳記蔥蔬餅', 
    '餅皮加入大量蔬菜與蔥，煎得外酥內軟，份量十足。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.99471 24.79815)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_06', 
    '蔥大爺餅舖 (阿婆蔥油餅)', 
    '原阿婆蔥油餅相關，餅皮薄脆，刷上特製辣醬是精華。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.99723 24.79951)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_07', 
    '大鼓肉夾饃', 
    '人氣新店，外皮酥脆千層，孜然肉餡香氣濃郁。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(121.000373 24.799014)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_08', 
    '車輪餅爺爺', 
    '脆皮車輪餅，餡料大方，紅豆與奶油是經典。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(121.0005 24.7998)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_09', 
    '羅記東山鴨頭', 
    '入味且外皮微酥，鴨皮與鴨脖子是熱門品項。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(121.0005 24.7998)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_10', 
    '郭董脆皮臭豆腐 (老港陳?)', 
    '清夜內的脆皮臭豆腐選擇，外酥內嫩。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.998248 24.798759)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_11', 
    '日荃蒸餃', 
    '高CP值蒸餃，皮薄餡多，搭配酸辣湯是絕配。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.997 24.798)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_12', 
    '紅吱吱牛排館', 
    '平價牛排首選，提供豐富自助吧，學生最愛。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.998592 24.795499)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_13', 
    '鳳荷三鮮', 
    '位於清大校內小吃部，羊肉料理湯頭清甜順口。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.9934 24.7935)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_14', 
    '飯丸屋 (清大店)', 
    '沖繩握飯糰專賣，午餐肉與厚蛋組合超受歡迎。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.99732 24.79815)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_15', 
    '黃記豆花', 
    '推薦酒釀系列，酒釀蛋與豆花風味獨特。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.997972 24.798089)', 
    '{}'
);
        

INSERT INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt, meta_data)
VALUES (
    '260101_16', 
    '豆戀迷 Do Re Mi', 
    '綠豆湯、紅豆湯專賣，推薦加QQ粉角。', 
    (SELECT layer_id FROM layers WHERE layer_type='生活機能' AND layer_subtype='夜市美食' LIMIT 1),
    'POINT', 
    'POINT(120.996767 24.799778)', 
    '{}'
);
        
-- 3. Insert Map

INSERT INTO walking_maps (map_id, name, description, region, meta_data)
VALUES ('260101_tsing_hua_night_market', '清大夜市散步地圖', '2026年清大夜市平價美食散步地圖，收錄經典老店與人氣新秀。', '新竹/東區', '{"routes": "graph TD;\n    N0[立晉傳統豆花] --> N1[小洞天];\n    N1[小洞天] --> N2[懷香臭臭鍋];\n    N2[懷香臭臭鍋] --> N3[清大雙囍餛飩老虎麵];\n    N3[清大雙囍餛飩老虎麵] --> N4[吳記蔥蔬餅];\n    N4[吳記蔥蔬餅] --> N5[蔥大爺餅舖 (阿婆蔥油餅)];\n    N5[蔥大爺餅舖 (阿婆蔥油餅)] --> N6[大鼓肉夾饃];\n    N6[大鼓肉夾饃] --> N7[車輪餅爺爺];\n    N7[車輪餅爺爺] --> N8[羅記東山鴨頭];\n    N8[羅記東山鴨頭] --> N9[郭董脆皮臭豆腐 (老港陳?)];\n    N9[郭董脆皮臭豆腐 (老港陳?)] --> N10[日荃蒸餃];\n    N10[日荃蒸餃] --> N11[紅吱吱牛排館];\n    N11[紅吱吱牛排館] --> N12[鳳荷三鮮];\n    N12[鳳荷三鮮] --> N13[飯丸屋 (清大店)];\n    N13[飯丸屋 (清大店)] --> N14[黃記豆花];\n    N14[黃記豆花] --> N15[豆戀迷 Do Re Mi];\n    N15[豆戀迷 Do Re Mi];\n"}');
    
-- 4. Insert Relations

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_01', 1, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_02', 2, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_03', 3, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_04', 4, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_05', 5, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_06', 6, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_07', 7, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_08', 8, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_09', 9, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_10', 10, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_11', 11, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_12', 12, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_13', 13, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_14', 14, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_15', 15, 1);
        

INSERT INTO walking_map_relations (map_id, feature_id, display_order, is_highlight)
VALUES ('260101_tsing_hua_night_market', '260101_16', 16, 1);
        