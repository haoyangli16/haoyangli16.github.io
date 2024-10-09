def rgb_depth2pointcloud(rgb: np.ndarray, depth: np.ndarray, intrinsic: np.ndarray, max_depth=None, obj_mask=None, return_o3d=False):
    mask = depth > 0
    if obj_mask is not None:
        mask = mask & obj_mask

    if max_depth is not None:
        mask = mask & (depth < max_depth * 1000)

    width = rgb.shape[1]
    height = rgb.shape[0]

    coords = np.stack(np.meshgrid(np.arange(width), np.arange(height)), axis=-1).astype(np.float32)
    coords = coords[:,::-1] + 0.5

    coords = np.concatenate((coords, np.ones((height, width, 1))), axis=-1)
    coords = coords @ np.linalg.inv(intrinsic).T


    position = coords * depth[..., None]
    depth = - position[mask]/1000.
    rgb = rgb[mask]

    xyz = depth.reshape(-1, 3).copy()
    if return_o3d:
        assert rgb.dtype == np.uint8, rgb.dtype
        import open3d as o3d
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(xyz)
        pcd.colors = o3d.utility.Vector3dVector(rgb/255.)
        return pcd

    xyz = xyz[:, [2, 0, 1]]
    xyz[:, 0] *= -1
    xyz[:, 1] *= -1

    return xyz, rgb.reshape(-1, 3)