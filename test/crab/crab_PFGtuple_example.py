
# example crab configuration file for one single run

##________________________________________________________________________________||
#Configurables

#dataset = '/JetHT/Run2015D-v1/RAW'
#run = '256729'
#dataset = '/MinimumBias/Commissioning2016-v1/RAW'
dataset = '/JetHT/Run2016B-v2/RAW'
#run = '266667'
run = '275311'

##________________________________________________________________________________||

jobname = dataset[1:].replace('/','__')
jobname = jobname.replace(':','___')
jobname = jobname.replace('RAW','RAW_'+run)

##________________________________________________________________________________||

from WMCore.Configuration import Configuration
config = Configuration()

##________________________________________________________________________________||

config.section_("General")
config.General.requestName  = jobname
config.General.workArea     = 'out_crab'

##________________________________________________________________________________||

config.section_("JobType")
config.JobType.pluginName   = 'Analysis'
#config.JobType.psetName     = 'analysis_Collision_crab_cfg.py'
#config.JobType.psetName     = 'pfg_CommissioningCosmic_RAW_cfg.py'
config.JobType.psetName     = 'pfg_Global_RAW_cfg.py'

##________________________________________________________________________________||

config.section_("Data")
config.Data.inputDataset    = dataset
config.Data.inputDBS        = 'global'
config.Data.splitting       = 'LumiBased'
config.Data.unitsPerJob     = 30 
#config.Data.publication     = True
config.Data.publication     = False
#config.Data.publishDBS      = 'phys03'
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = 'testName'
config.Data.outLFNDirBase = '/store/user/borzou/ntuples/Aug_2016'
#config.Data.lumiMask        = 'json.txt'
config.Data.runRange        = run

##________________________________________________________________________________||

config.section_("Site")
#config.Site.storageSite     = 'T2_CH_CERN'
config.Site.storageSite     = 'T3_US_Baylor'

#config.Site.whitelist = ['T2_US_Caltech','T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt', 'T2_US_Wisconsin', 'T1_US_FNAL','T2_US_MIT']
# you may want to uncomment this line and force jobs to run in the US
# only a few datasets (mostly very new ones) will not be accessible
