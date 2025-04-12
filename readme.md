# LiDAR-Based SLAM and Path Planning for Robotic Navigation

## Overview

This project explores the application of **Simultaneous Localization and Mapping (SLAM)** and **path planning** for robotic navigation using **LiDAR data**. The key components of this system include **visualizing 3D LiDAR scans**, performing **SLAM for localization and mapping**, and implementing the **A* algorithm** for pathfinding. The goal of the project is to enable robots to autonomously navigate an environment by building a global map, identifying obstacles, and planning the optimal path from start to goal.

---

## Environment Setup

In the initial setup phase, we configure the environment and install the necessary libraries for LiDAR data processing and path planning. You'll need libraries like `Open3D`, `NumPy`, `Matplotlib`, and `TQDM` for 3D point cloud visualization, numerical operations, and progress tracking.

Additionally, download a LiDAR dataset (e.g., **KITTI**) to use as input data for mapping and pathfinding. This step is crucial as the dataset contains raw LiDAR scans that will be used to create maps and plan paths.

---

## Visualizing LiDAR Data

In this section, the LiDAR point cloud data is loaded and visualized to understand the structure of the environment. The point cloud represents 3D data captured by a LiDAR sensor, showing the location of obstacles, open space, and the robot's surroundings. Using **Open3D**, we can visualize individual scans of the LiDAR data in 3D, allowing us to inspect and verify the quality of the raw data.

This step helps in understanding how the point cloud data is structured and how we can use it for mapping and localization tasks in subsequent parts of the project.

---

## SLAM using ICP (Mapping + Localization)

In this section, we implement **Simultaneous Localization and Mapping (SLAM)** using the **Iterative Closest Point (ICP)** algorithm. The objective of SLAM is to simultaneously localize the robot in an environment while building a map of that environment. ICP is used to align consecutive LiDAR scans and estimate the transformation between them. This transformation helps us track the robot's movement and position over time.

The aligned point clouds are merged into a global 3D map, which serves as a representation of the robot’s surroundings. This step is vital for building an accurate map of the environment, which will be used for obstacle detection and path planning in later stages of the project.

---

## Path Planning with A\*

The **A\*** algorithm is employed to compute the optimal path from a start point to a goal point within the 2D occupancy grid. The algorithm uses a heuristic to determine the shortest, obstacle-free path between the start and goal, considering the terrain and obstacles.

In this phase, we implement the core logic for pathfinding. By exploring the grid from the start point and evaluating neighboring cells, A\* finds the most efficient route to the goal, while avoiding any obstacles.

---

## Visualization of Final Results

Once the path planning is complete, we visualize the final results. This includes:

- **Robot's trajectory**: A visual representation of the path the robot has taken during the exploration and path planning process.
- **Final map**: A 3D global map that combines all the LiDAR scans and obstacles, showing the environment the robot will navigate through.
- **Planned path**: The optimal path computed by A*, overlaid on the map, showing the route the robot will take from start to goal.

We use **Matplotlib** for visualizing the trajectory and final path, and **Open3D** to overlay the planned path on the 3D map, providing a comprehensive view of the robot’s journey.

---

## Applications

- **Autonomous Vehicles**: Enables vehicles to navigate in unknown environments using LiDAR sensors for mapping and path planning.
- **Robotics**: Assists mobile robots in navigating through complex environments while avoiding obstacles.
- **Drones**: Supports aerial drones in 3D space for navigation and pathfinding.
- **Search and Rescue**: Useful in scenarios where robots need to explore and navigate environments autonomously to find and rescue individuals.

---

## Requirements

To set up this project, you’ll need the following libraries:

- **Open3D**: For 3D point cloud visualization and manipulation.
- **NumPy**: For numerical operations and handling arrays.
- **Matplotlib**: For visualizing the path, trajectory, and occupancy grid.
- **TQDM**: For showing progress bars during data processing.

You can install the required libraries with:

```bash
pip install open3d numpy matplotlib tqdm
```

Additionally, download a LiDAR dataset, such as **KITTI**, which will be used in this project.

---

## Acknowledgments

- **Open3D**: A powerful library for 3D data processing and visualization.
- **Iterative Closest Point (ICP)**: For aligning and merging LiDAR scans to create a global map.
- **A\* Algorithm**: For efficient path planning and navigation in a 2D grid environment.
- **KITTI Dataset**: For providing real-world LiDAR data used in this project.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
