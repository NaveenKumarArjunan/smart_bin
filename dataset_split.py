import os
import random
import shutil

# --- CONFIGURATION ---
image_dir = "./all_images"  # Path to your folder containing all 1085 images
label_dir = "./all_labels"  # Path to your folder containing all 1085 .txt labels
output_dir = "./Smart_Bin"  # Where you want the structured dataset saved

train_ratio = 0.8

# Ensure target directories exist
for split in ["train", "valid"]:
    os.makedirs(os.path.join(output_dir, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, split, "labels"), exist_ok=True)

# Get all images and sort to pair them correctly
image_extensions = (".jpg", ".jpeg", ".png", ".bmp")
all_images = [f for f in os.listdir(image_dir) if f.lower().endswith(image_extensions)]
random.seed(42)  # Ensures reproducibility
random.shuffle(all_images)

# Calculate split index
split_idx = int(len(all_images) * train_ratio)
train_images = all_images[:split_idx]
valid_images = all_images[split_idx:]

def move_files(image_list, split_name):
    for img_name in image_list:
        base_name = os.path.splitext(img_name)[0]
        lbl_name = base_name + ".txt"
        
        src_img = os.path.join(image_dir, img_name)
        src_lbl = os.path.join(label_dir, lbl_name)
        
        dest_img = os.path.join(output_dir, split_name, "images", img_name)
        dest_lbl = os.path.join(output_dir, split_name, "labels", lbl_name)
        
        # Move image
        if os.path.exists(src_img):
            shutil.copy(src_img, dest_img)
            
        # Move corresponding label if it exists
        if os.path.exists(src_lbl):
            shutil.copy(src_lbl, dest_lbl)

# Execute the move
move_files(train_images, "train")
move_files(valid_images, "valid")

print(f"Data split successfully!")
print(f"Train: {len(train_images)} images | Valid: {len(valid_images)} images")