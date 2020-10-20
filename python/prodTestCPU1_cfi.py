import FWCore.ParameterSet.Config as cms

from CUDAdemo.testGPUFirst.CUDATest.testCUDAProducerCPU_cfi import testCUDAProducerCPU as _testCUDAProducerCPU
prodTestCPU1 = _testCUDAProducerCPU.clone()
