import os
from PIL import Image
import streamlit as st

# Streamlit interface
st.title("TIFF to JPEG Converter")

# Input and output folder paths
tiff_folder = st.text_input("Input Folder for TIFF Files", "")
jpeg_folder = st.text_input("Output Folder for JPEG Files", "")

if st.button("Start Conversion"):
    if not tiff_folder or not jpeg_folder:
        st.error("Please provide both input and output folders.")
    else:
        # Create the output folder if it doesn't exist
        os.makedirs(jpeg_folder, exist_ok=True)

        # Get list of TIFF files
        tiff_files = [f for f in os.listdir(tiff_folder) if f.endswith('.tiff') or f.endswith('.tif')]

        if not tiff_files:
            st.error("No TIFF files found in the input folder.")
        else:
            # Conversion process
            for tiff_file in tiff_files:
                tiff_path = os.path.join(tiff_folder, tiff_file)
                jpeg_path = os.path.join(jpeg_folder, os.path.splitext(tiff_file)[0] + '.jpg')

                # Open the TIFF image
                with Image.open(tiff_path) as img:
                    # Preserve DPI
                    dpi = img.info.get('dpi', (72, 72))

                    # Convert to RGB if needed (JPEG doesn't support transparency)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    # Save as JPEG with the same DPI and resolution
                    img.save(jpeg_path, "JPEG", dpi=dpi)

            st.success(f"Conversion complete! {len(tiff_files)} files converted.")

