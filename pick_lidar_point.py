import open3d as o3d
import numpy as np
import pykitti

# Load KITTI data
basedir = "/home/deepak-bhagat/Downloads/data_odometry_velodyne/dataset/"
sequence = "00"
dataset = pykitti.odometry(basedir, sequence)

# Load LiDAR scan
scan = dataset.get_velo(0)

# Convert to Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(scan[:, :3])

# Save the point cloud to file
o3d.io.write_point_cloud("temp_lidar.pcd", pcd)

# Launch GUI to pick points (use Shift + Left Click to pick)
o3d.visualization.draw_geometries_with_editing([pcd])  # Use pcd here, not the file path
