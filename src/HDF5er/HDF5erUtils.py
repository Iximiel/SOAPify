import h5py
from sys import getsizeof
import numpy

# TODO need to work on type-hinting
def exportChunk2HDF5(
    trajFolder: h5py.Group,
    intervalStart: int,
    intervalEnd: int,
    boxes: "list[list[list[3*float]]]|numpy.ndarray",
    coordinates: "list|numpy.ndarray",
):
    """Export a chunk of atom information in an h5py.Group

    Args:
        trajFolder (h5py.Group): the group in the hdf5 file
        intervalStart (int): the first frame to save within the group
        intervalEnd (int): the last frame to save within the group
        boxes (list): the list of the boxes, frame per frame (for each frame 6 floats representing the dimension and the angles of the box)
        coordinates (list): the list of the coordinates, frame per frame (for each frame a list that contains the coordinates of all atoms in that frame)
    """

    # TODO: put an if and /or decide if this is an expansion or an ovewrite
    trajFolder["Box"].resize((intervalEnd, 6))
    trajFolder["Trajectory"].resize((intervalEnd, len(coordinates[0]), 3))
    print(
        f"[{intervalStart}:{intervalEnd}]",
        len(coordinates),
        len(trajFolder["Box"][intervalStart:intervalEnd]),
        f"chunk of {getsizeof(coordinates)} B",
    )

    trajFolder["Box"][intervalStart:intervalEnd] = boxes
    trajFolder["Trajectory"][intervalStart:intervalEnd] = coordinates