import FWCore.ParameterSet.Config as cms

from CUDAdemo.testGPUFirst.CUDATest.testCUDAProducerGPUFirst_cfi import testCUDAProducerGPUFirst as _testCUDAProducerGPUFirst
prodTestCUDA1 = _testCUDAProducerGPUFirst.clone()
