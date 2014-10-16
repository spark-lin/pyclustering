import unittest;

from nnet import initial_type, conn_represent, solve_type;

from clustering.syncnet import syncnet;

from support import read_sample, read_image;

from numpy import pi;

from samples.definitions import SIMPLE_SAMPLES, IMAGE_MAP_SAMPLES;


class Test(unittest.TestCase):
    def templateClustering(self, file, radius, order, solver, initial, storage_flag, conn_weigh_flag, tolerance, connection, expected_cluster_length, ccore_flag):
        result_testing = False;
        
        # If phases crosses each other because of random part of the network then we should try again.
        for attempt in range(0, 3, 1):
            sample = read_sample(file);
            network = syncnet(sample, radius, connection, initial, conn_weigh_flag, ccore_flag);
            network.process(order, solver, storage_flag);
            
            clusters = network.get_clusters(tolerance);
            
            obtained_cluster_sizes = [len(cluster) for cluster in clusters];
    
            if (len(obtained_cluster_sizes) != len(expected_cluster_length)):
                continue;
            
            obtained_cluster_sizes.sort();
            expected_cluster_length.sort();
            
            if (obtained_cluster_sizes != expected_cluster_length):
                continue;
            
            # Unit-test is passed
            result_testing = True;
            break;
        
        assert result_testing;
        
    
    def testClusteringSampleSimple1(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.MATRIX, [5, 5], False);
    
    def testClusteringSampleSimple1ListRepr(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.LIST, [5, 5], False);
        
    def testClusteringSampleSimple1ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, None, [5, 5], True);
        
    def testClusteringSampleSimple2(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.MATRIX, [5, 8, 10], False);
    
    def testClusteringSampleSimple2ListRepr(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.LIST, [5, 8, 10], False);     

    def testClusteringSampleSimple2ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, None, [5, 8, 10], True);
        
    def testClusteringSampleSimple3(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.MATRIX, [10, 10, 10, 30], False);
 
    def testClusteringSampleSimple3ListRepr(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.LIST, [10, 10, 10, 30], False);
    
    def testClusteringSampleSimple3ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, None, [10, 10, 10, 30], True);
        
    def testClusteringSampleSimple4(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.MATRIX, [15, 15, 15, 15, 15], False); 
    
    def testClusteringSampleSimple4ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, None, [15, 15, 15, 15, 15], True);
        
    def testClusteringSampleSimple5(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.MATRIX, [15, 15, 15, 15], False);
        
    def testClusteringSampleSimple5ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, None, [15, 15, 15, 15], True);
        
    def testClusteringSampleElongateByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_ELONGATE, 0.5, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 0.05, None, [135, 20], True);
        
    
    def testClusterAllocationHighToleranceSampleSimple1(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, conn_represent.MATRIX, [10], False);
    
    def testClusterAllocationHighToleranceSampleSimple1ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, None, [10], True);
    
    def testClusterAllocationHighToleranceSampleSimple2(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, conn_represent.MATRIX, [23], False);

    def testClusterAllocationHighToleranceSampleSimple2ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, None, [23], True);
        
    def testClusterAllocationHighToleranceSampleSimple3(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, conn_represent.MATRIX, [60], False);

    def testClusterAllocationHighToleranceSampleSimple3ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, None, [60], True);
    
    def testClusterAllocationHighToleranceSampleSimple4(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 0.7, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, conn_represent.MATRIX, [75], False);

    def testClusterAllocationHighToleranceSampleSimple4ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE4, 0.7, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, None, [75], True);
    
    def testClusterAllocationHighToleranceSampleSimple5(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 0.7, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, conn_represent.MATRIX, [60], False);

    def testClusterAllocationHighToleranceSampleSimple5ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE5, 0.7, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, False, 2 * pi, None, [60], True);

        
    def testClusterAllocationConnWeightSampleSimple1(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, True, 0.05, conn_represent.MATRIX, [5, 5], False);
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 10, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, True, 0.05, conn_represent.MATRIX, [10], False);
    
    def testClusterAllocationConnWeightSampleSimple2(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 2, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, True, 0.05, conn_represent.MATRIX, [5, 8, 10], False);
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 10, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, True, 0.05, conn_represent.MATRIX, [23], False);
        
    def testClusterAllocationConnWeightSampleSimple1ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 2, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, True, 0.05, None, [5, 5], True);
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 10, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, True, 0.05, None, [10], True);
        
    def testClusterAllocationConnWeightSampleSimple2ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 2, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, True, 0.05, None, [5, 8, 10], True);
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 10, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, True, True, 0.05, None, [23], True);
    
    
    def testClusteringWithoutDynamicCollectingSampleSimple1(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, False, False, 0.05, conn_represent.MATRIX, [5, 5], False);
    
    def testClusteringWithoutDynamicCollectingSampleSimple1ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, False, False, 0.05, conn_represent.MATRIX, [5, 5], True);
    
    def testClusteringWithoutDynamicCollectingSampleSimple2(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, False, False, 0.05, conn_represent.MATRIX, [5, 8, 10], False);
    
    def testClusteringWithoutDynamicCollectingSampleSimple2ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, False, False, 0.05, conn_represent.MATRIX, [5, 8, 10], True);    
    
    def testClusteringWithoutDynamicCollectingSampleSimple3(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, False, False, 0.05, conn_represent.MATRIX, [10, 10, 10, 30], False);

    def testClusteringWithoutDynamicCollectingSampleSimple3ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 1, 0.999, solve_type.FAST, initial_type.EQUIPARTITION, False, False, 0.05, conn_represent.MATRIX, [10, 10, 10, 30], False);


    def testClusteringRandomInitialSampleSimple1(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.RANDOM_GAUSSIAN, True, False, 0.05, conn_represent.MATRIX, [5, 5], False);
        
    def testClusteringRandomInitialSampleSimple1ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.FAST, initial_type.RANDOM_GAUSSIAN, True, False, 0.05, None, [5, 5], True);    

    def testClusteringRandomInitialSampleSimple2(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.RANDOM_GAUSSIAN, False, False, 0.05, conn_represent.MATRIX, [5, 8, 10], False);

    def testClusteringRandomInitialSampleSimple2ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 1, 0.999, solve_type.FAST, initial_type.RANDOM_GAUSSIAN, False, False, 0.05, None, [5, 8, 10], True);


    def testClusteringSolverRK4SampleSimple1(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.RK4, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.MATRIX, [5, 5], False);

    def testClusteringSolverRK4SampleSimple1ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.RK4, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.MATRIX, [5, 5], True);

    def testClusteringSolverRKF45SampleSimple1ByCore(self):
        self.templateClustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 1, 0.999, solve_type.RKF45, initial_type.EQUIPARTITION, True, False, 0.05, conn_represent.MATRIX, [5, 5], True);


    def testCreationDeletionByCore(self):
        # Crash occurs in case of memory leak
        data = read_image(IMAGE_MAP_SAMPLES.IMAGE_WHITE_SEA_SMALL);
        for iteration in range(0, 15):
            network = syncnet(data, 16, ccore = True);
            del network;

if __name__ == "__main__":
    unittest.main();