from math import floor;

from PIL import Image;

from support import draw_image_segments, read_image;

from samples.definitions import IMAGE_SIMPLE_SAMPLES, IMAGE_MAP_SAMPLES;

from clustering.dbscan import dbscan;


def template_segmentation_image(source, color_radius, color_neighbors, object_radius, object_neighbors, noise_size):    
    data = read_image(source);

    dbscan_instance = dbscan(data, color_radius, color_neighbors, True);
    dbscan_instance.process();
    
    clusters = dbscan_instance.get_clusters();
    
    real_clusters = [cluster for cluster in clusters if len(cluster) > noise_size];
    draw_image_segments(source, real_clusters);
    
    if (object_radius is None):
        return;
    
    # continue analysis
    pointer_image = Image.open(source);
    image_size = pointer_image.size;
    
    object_colored_clusters = [];
    
    for cluster in clusters:
        coordinates = [];
        for index in cluster:
            y = floor(index / image_size[0]);
            x = index - y * image_size[0];
            
            coordinates.append([x, y]);
        
        # perform clustering analysis of the colored objects
        if (len(coordinates) < noise_size):
            continue;
        
        dbscan_instance = dbscan(coordinates, object_radius, object_neighbors, True);
        dbscan_instance.process();
    
        object_clusters = dbscan_instance.get_clusters();
        
        # decode it
        real_description_clusters = [];
        for object_cluster in object_clusters:
            real_description = [];
            for index_object in object_cluster:
                real_description.append(cluster[index_object]);
            
            real_description_clusters.append(real_description);
            
            if (len(real_description) > noise_size):
                object_colored_clusters.append(real_description);
    
    draw_image_segments(source, object_colored_clusters);
    

def segmentation_image_simple1():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE01, 128, 4, None, None, 10);
    
def segmentation_image_simple2():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE02, 128, 4, None, None, 10);  
    
def segmentation_image_simple3():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE03, 128, 4, None, None, 10);
    
def segmentation_image_simple4():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE04, 128, 4, None, None, 10);
    
def segmentation_image_simple5():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE05, 128, 4, 4, 10, 4);

def segmentation_image_simple6():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE06, 128, 4, 4, 10, 4);
  
def segmentation_image_simple7():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE07, 128, 5, 4, 10, 4);
  
def segmentation_image_simple8():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE08, 128, 5, 4, 10, 4);

def segmentation_image_simple9():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE09, 128, 4, 4, 10, 4);

def segmentation_image_simple10():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE10, 128, 5, 4, 10, 4);  

def segmentation_image_beach():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE_BEACH, 128, 4, None, None, 10);
    
def segmentation_image_building():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE_BUILDING, 16, 10, 10, 10, 10);

def segmentation_image_fruits_small():
    template_segmentation_image(IMAGE_SIMPLE_SAMPLES.IMAGE_SIMPLE_FRUITS_SMALL, 15, 10, 2, 4, 20);

def segmentation_image_white_sea():
    template_segmentation_image(IMAGE_MAP_SAMPLES.IMAGE_WHITE_SEA, 16, 4, None, None, 50);

def segmentation_image_white_sea_small():
    template_segmentation_image(IMAGE_MAP_SAMPLES.IMAGE_WHITE_SEA_SMALL, 16, 4, None, None, 50);
    
def segmentation_image_nile():
    template_segmentation_image(IMAGE_MAP_SAMPLES.IMAGE_NILE, 16, 4, None, None, 50);
    
def segmentation_image_nile_small():
    template_segmentation_image(IMAGE_MAP_SAMPLES.IMAGE_NILE_SMALL, 16, 4, None, None, 50);
    
    
segmentation_image_simple1();
segmentation_image_simple2();
segmentation_image_simple3();
segmentation_image_simple4();
segmentation_image_simple5();
segmentation_image_simple6();
segmentation_image_simple7();
segmentation_image_simple8();
segmentation_image_simple9();
segmentation_image_simple10();
segmentation_image_beach();
segmentation_image_building();
segmentation_image_fruits_small();
 
segmentation_image_white_sea();
segmentation_image_white_sea_small();
segmentation_image_nile();
segmentation_image_nile_small();