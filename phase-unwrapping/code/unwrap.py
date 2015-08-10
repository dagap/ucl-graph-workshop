# Graph Cut optimization exercise for the UCL medical imaging summer school, 2015.
# Author: Pankaj Daga

__author__ = 'Pankaj Daga'

from image import Image
import sys
import argparse
import os
try:
    import maxflow
except ImportError:
    sys.exit('Please install pymaxflow to use these functions')

try:
    import numpy as np
except ImportError:
    sys.exit('Please install numpy to use these functions')


# Here we setup the command line parameters to the program.
# The program takes 3 parameters:
# -p: Path to the wrapped phase.
# -m: Path to the image mask
# -o: Path of the output file.

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--phase', help='The input phase image',
                    required=True, type=str)
parser.add_argument('-m', '--mask', help='The input mask file'
                    , required=True, type=str)
parser.add_argument('-o', '--output', help='Path to output image. '
                    'Default[Current_working_dir/unwrapped.nii]', required=False,
                    type=str, default=os.getcwd() + '/unwrapped.nii')

# args will now contain the input values. For example, you can get the
# file name of the input phase file as args.phase
args = parser.parse_args()

# Load the wrapped image and the mask image.
# Refer to the image.py file to see how you can load a nifti image
# from a file. In particular, see Image.from_file function.

# Load the two images.

# Step 2: Phase is only uniquely defined in the 2 PI range. Scale the input image so that
# it is in the principal range.
# Hint: Use np.max, np.min and np.pi expressions.
# Check the documentation online at http://docs.scipy.org/doc/numpy/reference/

# TO DO: Scale the input image.

# Write out the scaled data as a nifti image. See the save() function in the Image class.

# TO DO: Save the scaled image to a nifti file.

# For the optimization, we will only consider voxels that lie under the mask. This is needed
# because we have no valid measurement outside the masked region. Using the area outside the mask
# could lead to errors in estimation. Another reason for masking is that, perhaps, the measurements
# outside the mask are not captured well by our model.
# You can create a dictionary that maps a valid 3D index to a number. This will be useful later for
# matching indexes to the node IDs on the graph.

# TO DO: Write a function that takes the image data and masked data and returns a dictionary
# maps a 3D index to an integer.

# Now we are ready to start thinking about the optimization. Refer to the notes on the how this
# unwrapping problem can be formulated as an iterative algorithm where each step is a binary
# optimization step.

# We want to estimate an integer label at each voxel which determines the number of 2PI wraps
# at that voxel. Create a numpy array of labels of the correct size and set it to zero.
# This will be our initial estimate of the labels.

# TO DO: Create a numpy array of zeros representing the initial label values.

# Before we start the optimization, we should compute the initial energy of the current
# configuration. Write a function called compute_energy that computes the initial energy based
# on the sum of squared errors for each of the MRF cliques.
# Consider which voxels you need to take into account.

# TO DO: Write the energy function.

# Now we are ready to optimize. The graph is created for you below.

G = maxflow.Graph[float](0, 0)

# Now add the nodes to the graph. The graph will have as many nodes as the number of valid voxels.
# i.e. each voxel we need to unwrap is a random variable.

# TO DO: Create the graph nodes. In particular, you might want to see the help on Graph.add_nodes()
# method. Check out the examples at http://pmneila.github.io/PyMaxflow/ to see how to do this.

# Now we need to create the edges. See the handout for the edge weights and how they are calculated.
# See the pymaxflow documentation on how to add these edges.

# To DO: Write a function to create the edges on the graph.

# Now we can use the maxflow algorithm to do a binary partitioning of the datasets. See the pymaxflow
# documentation to see how you can call maxflow on the graph.

# TO DO: Call maxflow

# Computing the maximum flow corresponds to computing the minimum cut which gives you the lowest
# MRF energy configuration for this binary step. Based on the result, we can update our labels.
# Write a function which updates the labels based on which segment the node belongs to.

# TO DO: Write a function called upate_labels which update the current label configuration.

# Compute the new energy of the MRF configuration. Does it go down from the original configuration?

# TO DO: Call the energy function to compute the new energy

# So far we have successfully performed one binary optimization step using graph cuts.
# However, we need to solve a multilabel problem. You will need to create a loop which performs
# one binary optimization at each iteration. You will need to monitor the energy function and
# terminate when the energy difference is lower than some threshold (say 0.001). Take the code
# you have written so far and modify it to perform the full optimization.

# TO DO: Convert the binary solution to a multilabel one.

# You have an optimal solution! Congratulations! Well done indeed. Hopefully, it was a rewarding
# journey to solve this problem. Now it is time to visualize the results. For this, you will need
# to write a function that unwraps the image using the optimal label configuration.

# TO DO: Write a function that unwraps the image.

# Now we can write the image to the output file. Do that and visualize the result.

# TO DO: Save the unwrapped image and compare with original.


