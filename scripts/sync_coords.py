import sqlite3
import os
import re
import xml.etree.ElementTree as ET

DB_PATH = 'walkgis.db'
FEATURES_DIR = 'features'
KML_PATH = 'maps/260101_tsing_hua_night_market.kml'

def get_db_features():
    """Retrieve features from the database with their coordinates."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT feature_id, name, geometry_wkt FROM walking_map_features")
    rows = cursor.fetchall()
    conn.close()
    
    features = []
    for row in rows:
        fid, name, wkt = row
        # Parse WKT format: POINT(lon lat) or POINT(lon lat z)
        # Note: WKT can have optional spaces
        match = re.search(r'POINT\s*\(\s*([-\d\.]+)\s+([-\d\.]+)', wkt)
        if match:
            lon = match.group(1)
            lat = match.group(2)
            features.append({'id': fid, 'name': name, 'lat': lat, 'lon': lon})
    return features

def update_markdown(features):
    """Update frontmatter of markdown files with coordinate field [lat, lon]."""
    updated_count = 0
    for feat in features:
        # Construct filename from feature ID
        filepath = os.path.join(FEATURES_DIR, f"{feat['id']}.md")
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            fm_content = fm_match.group(1)
            
            new_fm_content = fm_content
            # Remove existing lat/lon/coordinate lines to avoid duplicates/redundancy
            new_fm_content = re.sub(r'^latitude:.*$\n?', '', new_fm_content, flags=re.MULTILINE)
            new_fm_content = re.sub(r'^longitude:.*$\n?', '', new_fm_content, flags=re.MULTILINE)
            new_fm_content = re.sub(r'^coordinate:.*$\n?', '', new_fm_content, flags=re.MULTILINE)
            
            # Clean up trailing newlines
            new_fm_content = new_fm_content.strip()
            
            # Append new coordinate in [lat, lon] format
            # Note: The database WKT might be lon lat, but the file example showed [lat, lon]
            # Example in file: coordinate: [24.7968636, 120.9983978]  (Lat, Lon)
            new_keys = f"\ncoordinate: [{feat['lat']}, {feat['lon']}]"
            new_fm_content = new_fm_content + new_keys + '\n'
            
            new_content = content.replace(fm_match.group(1), new_fm_content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1
            
    print(f"Updated {updated_count} Markdown files.")

def update_kml(features):
    """Update KML placemark coordinates."""
    ET.register_namespace('', "http://www.opengis.net/kml/2.2")
    try:
        tree = ET.parse(KML_PATH)
        root = tree.getroot()
        ns = {'kml': 'http://www.opengis.net/kml/2.2'}
        
        feature_map = {f['name']: f for f in features}
        
        count = 0
        # Recursively find Placemarks
        for placemark in root.findall('.//kml:Placemark', ns):
            name_tag = placemark.find('kml:name', ns)
            if name_tag is not None and name_tag.text in feature_map:
                feat = feature_map[name_tag.text]
                point = placemark.find('kml:Point', ns)
                if point is None:
                    # Create Point if missing
                    point = ET.SubElement(placemark, 'Point')
                
                coords = point.find('kml:coordinates', ns)
                if coords is None:
                    coords = ET.SubElement(point, 'coordinates')
                
                # Update coordinates
                coords.text = f"{feat['lon']},{feat['lat']},0"
                count += 1
                
        tree.write(KML_PATH, encoding='UTF-8', xml_declaration=True)
        print(f"Updated {count} Placemarks in KML.")
    except Exception as e:
        print(f"Error updating KML: {e}")

if __name__ == "__main__":
    print("Starting synchronization...")
    feats = get_db_features()
    print(f"Found {len(feats)} features in DB.")
    update_markdown(feats)
    update_kml(feats)
    print("Synchronization complete.")
