
import os
import shutil

# Step 1: Define source and destination
source_folder = r"C:\Users\Lenovo\Desktop"
destination_folder = os.path.join(source_folder, "jpg_files")

# Step 2: Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Step 3: List all files in source
files = os.listdir(source_folder)
print("📁 Files found on Desktop:")
for f in files:
    print("   -", f)

# Step 4: Move only .jpg or .JPG files
moved = False
for filename in files:
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, dest_path)
        print(f"✅ Moved: {filename}")
        moved = True

if not moved:
    print("❌ No .jpg files found in Desktop folder.")
else:
    print("✅ All .jpg files moved successfully!")
