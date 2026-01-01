
import sqlite3
import re
import urllib.parse
import os

# Config
# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# DB is in the parent folder
DB_PATH = os.path.join(SCRIPT_DIR, "../walkgis.db")
MAP_ID = "260101_tsing_hua_night_market"
# KML goes to maps folder
OUTPUT_KML = os.path.join(SCRIPT_DIR, "../maps/260101_tsing_hua_night_market.kml")

def parse_wkt_point(wkt):
    # WKT format: POINT(lon lat)
    match = re.search(r"POINT\s*\(\s*([0-9\.]+)\s+([0-9\.]+)\s*\)", wkt)
    if match:
        lon = float(match.group(1))
        lat = float(match.group(2))
        return lat, lon # Return Google Maps format (lat, lon)
    return None, None

def create_kml(features):
    kml_content = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>清大夜市散步地圖</name>
    <description>2026年清大夜市平價美食散步地圖，收錄經典老店與人氣新秀。</description>
"""
    for f in features:
        name = f['name']
        lat, lon = f['coords']
        desc = f['note'] if f['note'] else f['feature_desc']
        
        kml_content += f"""
    <Placemark>
      <name>{name}</name>
      <description>{desc}</description>
      <Point>
        <coordinates>{lon},{lat},0</coordinates>
      </Point>
    </Placemark>"""

    kml_content += """
  </Document>
</kml>"""
    return kml_content

def create_google_maps_link(features):
    base_url = "https://www.google.com/maps/dir/"
    waypoints = []
    
    for f in features:
        lat, lon = f['coords']
        # Convert name to URL safe string, but Google Maps dir works best with coords or Place IDs
        # We use "lat,lng" for precision
        waypoints.append(f"{lat},{lon}")
        
    # Join with slashes
    full_url = base_url + "/".join(waypoints)
    return full_url

def main():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        query = """
        SELECT f.name, f.description, f.geometry_wkt, r.note
        FROM walking_map_features f
        JOIN walking_map_relations r ON f.feature_id = r.feature_id
        WHERE r.map_id = ?
        ORDER BY r.display_order ASC
        """
        
        cursor.execute(query, (MAP_ID,))
        rows = cursor.fetchall()
        
        features = []
        for row in rows:
            lat, lon = parse_wkt_point(row[2])
            if lat and lon:
                features.append({
                    'name': row[0],
                    'feature_desc': row[1],
                    'note': row[3],
                    'coords': (lat, lon)
                })
        
        if not features:
            print(f"No features found for map: {MAP_ID}")
            return

        # 1. Generate KML
        kml_data = create_kml(features)
        with open(OUTPUT_KML, "w", encoding="utf-8") as f:
            f.write(kml_data)
        print(f"KML file created at: {OUTPUT_KML}")

        # 2. Generate Google Maps Link
        nav_link = create_google_maps_link(features)
        print("\n=== Google Maps Navigation Link ===")
        print(nav_link)
        print("===================================")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
