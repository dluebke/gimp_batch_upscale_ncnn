#!/usr/bin/env python

from gimpfu import *
import os

import sys

def batch_upscale_ncnn(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_dir, filename)
            print("Processing:", input_path)

            # Open the image
            image = pdb.gimp_file_load(input_path, input_path)
            drawable = pdb.gimp_image_get_active_layer(image)

            # Call the NCNN upscale plugin
            # Adjust the arguments as needed depending on your plugin's parameter signature
            # Example parameters: image, drawable, scale factor, model, tta
            pdb.python_fu_upscale_with_ncnn(image, drawable, 0, 0, False, 4)

            # Export the result
            output_path = os.path.join(output_dir, filename)
            pdb.file_png_save_defaults(image, image.active_layer, output_path, output_path)

            # Clean up
            pdb.gimp_image_delete(image)

register(
    proc_name = "python-fu-batch-upscale",
    blurb = "Batch Upscale using Upscale NCNN",
    help = "(no help available)",
    author = "github.com/dluebke",
    copyright = "github/dluebke; MIT-LICENSE; 2024;",
    date = "2025",
    label = "Batch AI Upscale (NCNN)...",
    menu = "<Toolbox>/File/Acquire",
    imagetypes = "*",
    params = [
        (PF_DIRNAME, "input_dir", "Input Directory with PNGs", None),
        (PF_DIRNAME, "output_dir", "Output Directory with PNGs", None)
    ],
    results = [],
    function = batch_upscale_ncnn,
)

main()
