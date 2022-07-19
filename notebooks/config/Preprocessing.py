
import os


# Configuration of the parameters for the 1-Preprocessing.ipynb notebook
class Configuration:
    '''
    Configuration for the first notebook.
    Copy the configTemplate folder and define the paths to input and output data. Variables such as raw_ndvi_image_prefix may also need to be corrected if you are use a different source.
    '''
    def __init__(self):
        # For reading the training areas and polygons
        self.training_base_dir = '/mnt/c/Users/Research/Documents/GitHub/africa-trees/SampleAnnotations' 
        self.training_area_fn = 'area.gpkg' #'training_areas_example.shp'
        self.training_polygon_fn = 'test.gpkg' #'training_polygons_example.shp'

        # For reading the VHR images
        self.bands = [0]
        self.raw_image_base_dir = '/mnt/c/Users/Research/Documents/GitHub/africa-trees/SampleAnnotations'
        self.raw_image_file_type = '.tif'
        self.raw_ndvi_image_prefix = 'ndvi_SSA_32628_010_003_mosaic_2_3_mask'
        self.raw_pan_image_prefix = 'pan_SSA_32628_010_003_mosaic_2_3_mask'

        # For writing the extracted images and their corresponding annotations and boundary file
        self.path_to_write = '/mnt/c/Users/Research/Documents/GitHub/africa-trees/SampleResults-Preprocessing'
        self.show_boundaries_during_processing = False
        self.extracted_file_type = '.tif' # .png' 
        self.extracted_ndvi_filename = 'ndvi'
        self.extracted_pan_filename = 'pan'
        self.extracted_annotation_filename = 'annotation' #annotation
        self.extracted_boundary_filename = 'boundary' #boundary
        

        # Path to write should be a valid directory
        assert os.path.exists(self.path_to_write)

        if not len(os.listdir(self.path_to_write)) == 0:
            print('Warning: path_to_write is not empty! The old files in the directory may not be overwritten!!')
