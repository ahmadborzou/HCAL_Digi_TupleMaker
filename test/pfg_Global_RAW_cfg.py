#------------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
import FWCore.ParameterSet.VarParsing as VarParsing

#------------------------------------------------------------------------------------
# Declare the process and input variables
#------------------------------------------------------------------------------------
process = cms.Process('PFG')
#inputFiles = "/store/data/Run2016B/JetHT/RAW/v2/000/273/502/00000/0029695E-AC1B-E611-8E15-02163E011934.root"
inputFiles = "/store/data/Run2016B/JetHT/RAW/v2/000/275/311/00000/04986442-CC35-E611-A3B0-02163E0142BD.root"
skipEvents = 0
processEvents = -1
outputFile = "HcalTupleMaker.root"

#------------------------------------------------------------------------------------
# Get and parse the command line arguments
#------------------------------------------------------------------------------------
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(processEvents) )
process.source = cms.Source("PoolSource",
    fileNames  = cms.untracked.vstring(inputFiles),
    skipEvents = cms.untracked.uint32(skipEvents)
)

process.TFileService = cms.Service("TFileService",
     fileName = cms.string(outputFile)
)

#------------------------------------------------------------------------------------
# import of standard configurations
#------------------------------------------------------------------------------------
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_0T_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('RecoMET.METProducers.hcalnoiseinfoproducer_cfi')
process.load("CommonTools.RecoAlgos.HBHENoiseFilter_cfi")
process.load("CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi")

#------------------------------------------------------------------------------------
# Set up our analyzer
#------------------------------------------------------------------------------------
#process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_cfi") # Dont want to use this, load modules individually
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Tree_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Event_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HBHEDigis_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HODigis_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HFDigis_cfi")
process.hcalTupleHFDigis.DoEnergyReco = False
process.hcalTupleHFDigis.FilterChannels = True
process.hcalTupleHFDigis.ChannelFilterList = cms.untracked.VPSet(
    # -------------------------------------------------
    # HF channels for QIE10 study
    # 26 = (24+2) QIE10 channels
    # 22 = (24-2) dual readout QIE8 channels
    # 2 dead QIE8 channels replaced with QIE10 channels
    # -------------------------------------------------
    # depth 1
    cms.PSet(iEta = cms.int32(29), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(30), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(31), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(32), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(33), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(34), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(35), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(36), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(37), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(38), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(39), iPhi = cms.int32(39), depth = cms.int32(1)),
    cms.PSet(iEta = cms.int32(41), iPhi = cms.int32(39), depth = cms.int32(1)),
    # depth 2
    cms.PSet(iEta = cms.int32(29), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(30), iPhi = cms.int32(39), depth = cms.int32(2)), # dead
    cms.PSet(iEta = cms.int32(31), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(32), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(33), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(34), iPhi = cms.int32(39), depth = cms.int32(2)), # dead
    cms.PSet(iEta = cms.int32(35), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(36), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(37), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(38), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(39), iPhi = cms.int32(39), depth = cms.int32(2)),
    cms.PSet(iEta = cms.int32(41), iPhi = cms.int32(39), depth = cms.int32(2))
    )
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HBHERecHits_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HFRecHits_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_L1Jets_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HcalTriggerPrimitives_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalL1JetDigisProducer_cfi")
#process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Trigger_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_MuonTrack_cfi")
process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_QIE10Digis_cfi")

from Configuration.StandardSequences.RawToDigi_Data_cff import *
process.CustomizedRawToDigi = cms.Sequence(
                gtDigis*
		#siPixelDigis*
		#siStripDigis*
		#ecalDigis*
		#ecalPreshowerDigis*
		hcalDigis
		#muonDTDigis*
		#muonCSCDigis*
		#muonRPCDigis*
		#castorDigis*
		#scalersRawToDigi*
		#tcdsDigis
)

#------------------------------------------------------------------------------------
# QIE10  Unpacker
#------------------------------------------------------------------------------------
process.qie10Digis = process.hcalDigis.clone()
#process.qie10Digis.InputLabel = cms.InputTag("source") 
process.qie10Digis.FEDs = cms.untracked.vint32(1132)

#------------------------------------------------------------------------------------
# Specify Global Tag
#------------------------------------------------------------------------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v8'

#------------------------------------------------------------------------------------
# Configure modules
#------------------------------------------------------------------------------------
process.my_hlt = cms.EDFilter("HLTHighLevel",
     TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
     HLTPaths = cms.vstring("HLT_L1SingleMuOpen_*"), # provide list of HLT paths (or patterns) you want
     eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
     andOr = cms.bool(True),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
     throw = cms.bool(False)    # throw exception on unknown path names
)

#------------------------------------------------------------------------------------------------------------------------------------
# Create Noise Filter
#------------------------------------------------------------------------------------------------------------------------------------
process.hcalnoise.fillCaloTowers = cms.bool(False)
process.hcalnoise.fillTracks = cms.bool(False)
process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
			inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
			reverseDecision = cms.bool(False)
			)

#------------------------------------------------------------------------------------
# HcalTupleMaker sequence definition
#------------------------------------------------------------------------------------
process.tuple_step = cms.Sequence(
    # Make HCAL tuples: Event, run, ls number
    process.hcalTupleEvent*
    # Make HCAL tuples: FED info
    #    process.hcalTupleFEDs*
    #    # Make HCAL tuples: digi info
    #raw
    #process.hcalTupleHBHEDigis*
    #process.hcalTupleHODigis*
    process.hcalTupleHFDigis*
    process.hcalTupleQIE10Digis*
    #process.hcalCosmicDigis*
    #process.hcalL1JetDigis*
    #process.hcalTupleTriggerPrimitives*
    #    # Make HCAL tuples: digi info
    #process.hcalTupleHBHECosmicsDigis*
    #    process.hcalTupleHOCosmicsDigis*
    #    # Make HCAL tuples: digi info
    #process.hcalTupleHBHEL1JetsDigis*
    #    process.hcalTupleHFL1JetsDigis*
    #    process.hcalTupleL1JetTriggerPrimitives*
    #    # Make HCAL tuples: reco info
    #process.hcalTupleHBHERecHits*
    #process.hcalTupleL1Jets*
    #process.hcalTupleHFRecHits*
    #process.hcalTupleHcalNoiseFilters*
    #process.hcalTupleMuonTrack*
    #
    #process.hcalTupleHBHERecHitsMethod0*
    #process.hcalTupleHcalNoiseFiltersMethod0*
    #process.hcalTupleCaloJetMetMethod0*
    #    process.hcalTupleHORecHits*
    #    process.hcalTupleHFRecHits*
    #    # Trigger info
    #process.hcalTupleTrigger*
    
    #    process.hcalTupleTriggerObjects*
    #    # Make HCAL tuples: cosmic muon info
    # process.hcalTupleCosmicMuons*
    #    # Package everything into a tree
    #
    process.hcalTupleTree
)

#-----------------------------------------------------------------------------------
# Path and EndPath definitions
#-----------------------------------------------------------------------------------
process.preparation = cms.Path(
    #process.my_hlt *
    #process.RawToDigi * #needed for RAW files
    #process.CustomizedRawToDigi *
    process.hcalDigis*
    process.qie10Digis*
    #process.L1Reco *
    #process.reconstruction * #needed for RAW files
    #process.caloglobalreco *
    #process.hcalLocalRecoSequence *
    #
    #process.horeco *
    #process.hfreco *
    #
    #process.hbheprerecoMethod0 *
    #process.hbheprerecoMethod2 *
    #process.hbherecoMethod0 *
    #process.hbherecoMethod2 *
    #
    #process.towerMakerMethod0 *
    #process.towerMakerMethod2 *
    #
    #process.hcalnoiseMethod0 *
    #process.hcalnoiseMethod2 *
    #
    #process.HBHENoiseFilterResultProducerMethod0 *
    #process.HBHENoiseFilterResultProducerMethod2 *
    #
    #
    #process.hcalCosmicDigis *
    #process.hcalL1JetDigis *
    #
    #process.hcalnoise *  #needed for RAW files
    #process.HBHENoiseFilterResultProducer *
    #process.ApplyBaselineHBHENoiseFilter *
    #
    process.tuple_step
)
