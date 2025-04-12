import open3d as o3d
import numpy as np
import time
import matplotlib.pyplot as plt
from itertools import islice
import pykitti

# Load KITTI odometry sequence
basedir = "/home/deepak-bhagat/Downloads/data_odometry_velodyne/dataset/"
sequence = "00"
dataset = pykitti.odometry(basedir, sequence)

# Get the first scan and initialize PointCloud
initial_scan = dataset.get_velo(0)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(initial_scan[:, :3])

# Set colors using height (z-axis)
z = initial_scan[:, 2]
z_normalized = (z - np.min(z)) / (np.max(z) - np.min(z) + 1e-8)
colors = plt.get_cmap("gray")(z_normalized)[:, :3]  # <-- black to white
pcd.colors = o3d.utility.Vector3dVector(colors)

# Start visualizer
vis = o3d.visualization.Visualizer()
vis.create_window(window_name="KITTI LiDAR Animation", width=1280, height=720)
vis.add_geometry(pcd)

# Improve visuals
render_option = vis.get_render_option()
render_option.background_color = np.array([1, 1, 1])  # white background
render_option.point_size = 1.5

# Animate first 500 frames
for i, scan in enumerate(islice(dataset.velo, 500)):
    print(f"Rendering frame {i+1}/500")

    # Update points
    points = scan[:, :3]
    pcd.points = o3d.utility.Vector3dVector(points)

    # Update colors
    z = points[:, 2]
    z_normalized = (z - np.min(z)) / (np.max(z) - np.min(z) + 1e-8)
    colors = plt.get_cmap("gray")(z_normalized)[:, :3]  # <-- black to white
    pcd.colors = o3d.utility.Vector3dVector(colors)

    # Update visualizer
    vis.update_geometry(pcd)
    vis.poll_events()
    vis.update_renderer()
    time.sleep(0.05)

vis.destroy_window()
