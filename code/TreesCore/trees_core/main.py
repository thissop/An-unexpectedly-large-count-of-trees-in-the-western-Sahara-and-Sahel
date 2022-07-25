from __future__ import annotations
from xxlimited import Str


def preprocess(area_files:list, 
               annotation_files:list,
               raw_ndvi_images:list,
               raw_pan_images:list,
               output_path:str,
               bands=[0],
               show_boundaries_during_preprocessing:bool=True, verbose:bool=False):
    import geopandas as gps
    import os
    from tqdm import tqdm
    from trees_core.preprocessing_utilities import readInputImages, extractAreasThatOverlapWithTrainingData, dividePolygonsInTrainingAreas

    r'''
    # For reading the training areas and polygons
    training_base_dir = '/mnt/c/Users/Research/Documents/GitHub/africa-trees/data/first_mosaic/annotations/ready/vectors' 
    training_area_fn = 'thaddaeus_vector_rectangle_10.gpkg' #'training_areas_example.shp'
    training_polygon_fn = 'thaddaeus_training_annotations_10.gpkg' #'training_polygons_example.shp'

    # For reading the VHR images
    bands = [0]
    raw_image_base_dir = '/mnt/c/Users/Research/Documents/GitHub/africa-trees/data/first_mosaic/annotations/ready/images'
    raw_image_file_type = '.tif'
    raw_ndvi_image_prefix = 'ndvi_thaddaeus_training_area'
    raw_pan_image_prefix = 'pan_thaddaeus_training_area'

    # For writing the extracted images and their corresponding annotations and boundary file
    path_to_write = '/mnt/c/Users/Research/Documents/GitHub/africa-trees/data/first_mosaic/annotations/ready/temp_output'
    show_boundaries_during_processing = False
    extracted_file_type = '.tif' # .png' --> change this back to png! 
    extracted_ndvi_filename = 'ndvi'
    extracted_pan_filename = 'pan'
    extracted_annotation_filename = 'annotation' #annotation
    extracted_boundary_filename = 'boundary' #boundary
    '''
    
    for training_area, training_annotations in tqdm(zip(area_files, annotation_files)): 
        trainingArea = gps.read_file(training_area)
        trainingPolygon = gps.read_file(training_annotations)

        if verbose: 
            print(f'Read a total of {trainingPolygon.shape[0]} object polygons and {trainingArea.shape[0]} training areas.')
            print(f'Polygons will be assigned to training areas in the next steps.') 

        #Check if the training areas and the training polygons have the same crs
        if trainingArea.crs  != trainingPolygon.crs:
            print('Training area CRS does not match training_polygon CRS')
            targetCRS = trainingPolygon.crs #Areas are less in number so conversion should be faster
            trainingArea = trainingArea.to_crs(targetCRS)
        
        if verbose: 
            print(trainingPolygon.crs)
            print(trainingArea.crs)
        
        assert trainingPolygon.crs == trainingArea.crs

        trainingArea['id'] = range(trainingArea.shape[0])
        if verbose: 
            print(trainingArea)
        
        # areasWithPolygons contains the object polygons and weighted boundaries for each area!
        areasWithPolygons = dividePolygonsInTrainingAreas(trainingPolygon, trainingArea, show_boundaries_during_processing=show_boundaries_during_preprocessing)
        if verbose: 
            print(f'Assigned training polygons in {len(areasWithPolygons)} training areas and created weighted boundaries for polygons')

    inputImages = list(zip(raw_ndvi_images,raw_pan_images))
    if verbose:
        print(f'Found a total of {len(inputImages)} pair of raw image(s) to process!')

    # For each raw satellite image, determine if it overlaps with a training area. 
    # If a overlap if found, then extract + write the overlapping part of the raw image, create + write an image from training polygons and create + write an image from boundary weights in the that overlapping region.
        
    # Run the main function for extracting part of ndvi and pan images that overlap with training areas
    writeCounter=0 # THIS MAY BE WERE THE ISSUE IS!
    extractAreasThatOverlapWithTrainingData(inputImages, areasWithPolygons, path_to_write=output_path, extracted_ndvi_filename, extracted_pan_filename, extracted_annotation_filename, extracted_boundary_filename, bands, writeCounter)

def train(): 
    pass 

def evaluate():
    pass 