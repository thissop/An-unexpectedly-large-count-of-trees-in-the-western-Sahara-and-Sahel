def preprocess(verbose:bool=False):
    import geopandas as gps
    import os
    from tqdm import tqdm
    from tree_core.preprocessing_utilities import readInputImages, extractAreasThatOverlapWithTrainingData, dividePolygonsInTrainingAreas

    training_base_dir = ''
    training_area_fn = ''
    training_polygon_fn = ''

    raw_image_base_dir = ''
    raw_image_file_type = '' 
    raw_ndvi_image_prefix = '' 
    raw_pan_image_prefix = '' 

    show_boundaries_during_processing = True

    path_to_write = ''
    extracted_ndvi_filename = ''
    extracted_pan_filename = ''
    extracted_annotation_filename = ''
    extracted_boundary_filename = ''
    bands = ''


    ## CELL THREE ##

    trainingArea = gps.read_file(os.path.join(training_base_dir, training_area_fn))
    trainingPolygon = gps.read_file(os.path.join(training_base_dir, training_polygon_fn))

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
    areasWithPolygons = dividePolygonsInTrainingAreas(trainingPolygon, trainingArea, show_boundaries_during_processing=show_boundaries_during_processing)
    if verbose: 
        print(f'Assigned training polygons in {len(areasWithPolygons)} training areas and created weighted boundaries for polygons')

    inputImages = readInputImages(raw_image_base_dir, raw_image_file_type, raw_ndvi_image_prefix, raw_pan_image_prefix)
    if verbose:
        print(f'Found a total of {len(inputImages)} pair of raw image(s) to process!')

    # For each raw satellite image, determine if it overlaps with a training area. 
    # If a overlap if found, then extract + write the overlapping part of the raw image, create + write an image from training polygons and create + write an image from boundary weights in the that overlapping region.
        
    # Run the main function for extracting part of ndvi and pan images that overlap with training areas
    writeCounter=0 # THIS MAY BE WERE THE ISSUE IS!
    extractAreasThatOverlapWithTrainingData(inputImages, areasWithPolygons, path_to_write, extracted_ndvi_filename, extracted_pan_filename, extracted_annotation_filename, extracted_boundary_filename, bands, writeCounter)