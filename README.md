# WalkGIS Sample Data

這是一個 WalkGIS 的範例資料庫，展示如何組織地圖路線 (Maps) 與地標特色 (Features) 資料。本專案可用於測試與展示 `walkgis-template` 或 WalkGIS 應用程式的功能。

## 📂 資料結構

本專案採用 WalkGIS 的標準資料結構：

*   **`maps/`**: 存放地圖路線定義檔。
    *   包含 Markdown (`.md`) 格式的路線描述與關聯圖 (Graph)。
    *   包含 KML (`.kml`) 格式的地理空間資料。
*   **`features/`**: 存放個別地點或特色的詳細描述。
    *   每個檔案代表一個地點 (POI)，包含標籤 (Tags) 與詳細介紹。

## 🗺️ 精選地圖 (Maps)

### [清大夜市散步地圖](maps/260101_tsing_hua_night_market.md)
探索新竹清華大學周邊的夜市美食，從經典老店到人氣新秀。
*   **ID**: `260101_tsing_hua_night_market`
*   **格式**: KML + Markdown
*   **景點數**: 16 個精選美食站點
*   **特色**: 包含立晉豆花、小洞天、懷香臭臭鍋等在地必吃名單。

## 📍 特色景點 (Features)

`features/` 目錄下包含了組成地圖的各個景點詳細資訊，例如：
*   [立晉傳統豆花](features/260101_01.md)
*   [小洞天](features/260101_02.md)
*   ...以及更多。

---
*Created for WalkGIS ecosystem.*
