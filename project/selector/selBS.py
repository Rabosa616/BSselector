
class BranchingStrategy :

  BS_UNKNOWN              = -1
  BS_NONE                 = 0
  BS_SINGLEDEV            = 10
  BS_ANARCHY              = 11
  BS_GITFLOW              = 20
  BS_GITHUBFLOW           = 21
  BS_TRUNKBASED           = 22
  BS_GITLABFLOW           = 23
  BS_ONEFLOW              = 24
  BS_CONTINUOUSINTEG      = 25
  BS_SIMPLIFIEDGITFLOW1   = 30
  BS_ONEFLOWEXTENDED      = 31
  BS_FORKINGFLOW          = 32


  dictNamesBS = {
    BS_UNKNOWN              : "UNKNOWN / N.A."                  ,
    BS_NONE                 : "NONE"                            ,
    BS_SINGLEDEV            : "Single developer"                ,
    BS_ANARCHY              : "Anarchy workflow"                ,
    BS_GITFLOW              : "git-flow"                        ,
    BS_GITHUBFLOW           : "github-flow"                     ,
    BS_TRUNKBASED           : "trunk-based development"         ,
    BS_GITLABFLOW           : "gitlab-flow"                     ,
    BS_ONEFLOW              : "one-flow"                        ,
    BS_CONTINUOUSINTEG      : "Continuous Integration"          ,
    BS_SIMPLIFIEDGITFLOW1   : "Simplified git-flow"             ,
    BS_ONEFLOWEXTENDED      : "Extended one-flow"               ,
    BS_FORKINGFLOW          : "Forking workflow (git-flow)"     ,
  }


  dictBS_1_developers = {
    BS_NONE                 : True,
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_TRUNKBASED           : True,
    BS_ONEFLOWEXTENDED      : True,

    BS_CONTINUOUSINTEG      : False,
    BS_FORKINGFLOW          : False,
  }

  dictBS_1_3_developers = {
    BS_NONE                 : True,
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_TRUNKBASED           : True,
    BS_GITHUBFLOW           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,

    BS_FORKINGFLOW          : False,
  }

  dictBS_2_8_developers = {
    BS_TRUNKBASED           : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_CONTINUOUSINTEG      : True,
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
  }

  dictBS_5_13_developers = {
    BS_TRUNKBASED           : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
  }

  dictBS_8_21_developers = {
    BS_ONEFLOWEXTENDED      : True,
    BS_CONTINUOUSINTEG      : True,
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_GITHUBFLOW           : False,
    BS_CONTINUOUSINTEG      : False,
  }

  dictBS_21_more_developers = {
    BS_ONEFLOWEXTENDED      : True,
    BS_CONTINUOUSINTEG      : True,
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_GITHUBFLOW           : False,
    BS_CONTINUOUSINTEG      : False,
  }

  dictBS_test_coverage_low = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,

    BS_CONTINUOUSINTEG      : False,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
  }

  dictBS_test_coverage_medium = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_GITHUBFLOW           : False,
    BS_CONTINUOUSINTEG      : False,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
  }

  dictBS_test_coverage_high = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,
  }

  dictBS_single_version_product = {
    BS_GITHUBFLOW           : True,
  }

  dictBS_multiple_version_product = {
    BS_GITFLOW              : True,

    BS_SIMPLIFIEDGITFLOW1   : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_GITHUBFLOW           : False,
    BS_NONE                 : False,
  }
  
  dictBS_continuous_delivery = {
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,

    BS_GITFLOW              : False,
    BS_ONEFLOW              : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_NONE                 : False,
    BS_FORKINGFLOW          : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
  }

  # short: half year or less
  dictBS_short_project_life = {
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_NONE                 : True,
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,

    BS_GITFLOW              : False,
    BS_ONEFLOW              : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_FORKINGFLOW          : False,
  }

  # medium: around 1 year, less than 2 years
  dictBS_medium_project_life = {
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,

    BS_ONEFLOWEXTENDED      : False,
  }

  # long: 2 years or more
  dictBS_long_project_life = {
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_GITFLOW              : True,
    BS_FORKINGFLOW          : True,

    BS_ONEFLOWEXTENDED      : False,
    BS_GITHUBFLOW           : False,
    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
  }

  # 1-time a day or more
  dictBS_deploy_very_frequently = {
    BS_GITHUBFLOW           : True,
    BS_GITLABFLOW           : True,
    BS_TRUNKBASED           : True,

    BS_ONEFLOWEXTENDED      : False,
    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_FORKINGFLOW          : False,
    BS_ONEFLOW              : False,
    BS_GITFLOW              : False,
  }

  # 2-3 times a a week
  dictBS_deploy_frequently = {
    BS_GITHUBFLOW           : True,
    BS_GITLABFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_ONEFLOW              : False,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_FORKINGFLOW          : False,
    BS_GITFLOW              : False,
  }

  # 1 times every week or two
  dictBS_deploy_not_frequently = {
    BS_GITLABFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_ONEFLOW              : True,
    BS_SINGLEDEV            : True,
    BS_FORKINGFLOW          : True,
    BS_GITFLOW              : True,
    BS_NONE                 : True,

    BS_GITHUBFLOW           : False,
  }

  # around once a month or less
  dictBS_deploy_rarely = {
    BS_GITFLOW              : True,
    BS_ONEFLOW              : True,
    BS_NONE                 : True,
    BS_SINGLEDEV            : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,
    BS_ANARCHY              : True,

    BS_GITHUBFLOW           : False,
    BS_GITLABFLOW           : False,
  }

  dictBS_1_longlived_branches = {
    BS_TRUNKBASED           : True,
    BS_SINGLEDEV            : True,
    BS_GITHUBFLOW           : True,
    BS_GITLABFLOW           : True,
    BS_NONE                 : True,
    BS_CONTINUOUSINTEG      : True,

    BS_ANARCHY              : False,
    BS_GITFLOW              : False,
    BS_ONEFLOW              : False,
    BS_FORKINGFLOW          : False,
  }

  dictBS_2_longlived_branches = {
    BS_GITLABFLOW           : True,
    BS_GITFLOW              : True,
    BS_ONEFLOW              : True,
    BS_FORKINGFLOW          : True,
    BS_ONEFLOWEXTENDED      : True,

    BS_TRUNKBASED           : False,
    BS_SINGLEDEV            : False,
    BS_GITHUBFLOW           : False,
    BS_ANARCHY              : False,
    BS_CONTINUOUSINTEG      : False,
    BS_SIMPLIFIEDGITFLOW1   : False,
  }

  dictBS_3_longlived_branches = {
    BS_GITFLOW              : True,
    BS_FORKINGFLOW          : True,

    BS_TRUNKBASED           : False,
    BS_SINGLEDEV            : False,
    BS_GITHUBFLOW           : False,
    BS_ANARCHY              : False,
    BS_GITLABFLOW           : False,
    BS_ONEFLOW              : False,
    BS_CONTINUOUSINTEG      : False,
    BS_SIMPLIFIEDGITFLOW1   : False,
    BS_ONEFLOWEXTENDED      : False,
  }

  dictBS_1_subteams_or_projects = {
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_NONE                 : True,
  }

  dictBS_2_more_subteams_or_projects = {
    BS_GITFLOW              : True,
    BS_FORKINGFLOW          : True,

    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
    BS_CONTINUOUSINTEG      : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_NONE                 : False,
  }

  dictBS_existing_codebase_zero_or_small = {
    BS_CONTINUOUSINTEG      : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_NONE                 : True,

    BS_GITFLOW              : False,
    BS_FORKINGFLOW          : False,
  }

  dictBS_existing_codebase_large = {
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_TRUNKBASED           : False,
    BS_CONTINUOUSINTEG      : False,
  }

  dictBS_existing_repositories_1 = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_NONE                 : True,

    BS_FORKINGFLOW          : False,
  }

  dictBS_existing_repositories_2_more = {
    BS_GITFLOW              : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
    BS_CONTINUOUSINTEG      : False,
  }

  dictBS_application_type_mobile = {
    BS_SINGLEDEV            : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,

    BS_GITFLOW              : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_FORKINGFLOW          : False,
    BS_NONE                 : False,
  }

  dictBS_application_type_web = {
    BS_SINGLEDEV            : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,

    BS_FORKINGFLOW          : False,
    BS_NONE                 : False,
    BS_ANARCHY              : False,
    BS_GITFLOW              : False,
  }

  dictBS_application_type_desktop = {
    BS_SINGLEDEV            : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,

    BS_NONE                 : False,
    BS_GITHUBFLOW           : False,
  }

  dictBS_application_type_firmware = {
    BS_SINGLEDEV            : True,
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_NONE                 : False,
    BS_ANARCHY              : False,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
  }

  dictBS_application_type_embedded = {
    BS_SINGLEDEV            : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,

    BS_ANARCHY              : False,
    BS_CONTINUOUSINTEG      : False,
  }

  dictBS_maintain_single_version_product = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,
  }

  dictBS_maintain_multiple_version_product = {
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_CONTINUOUSINTEG      : False,

    BS_NONE                 : False,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
  }

  dictBS_integration_frequency_high  = {
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_CONTINUOUSINTEG      : True,

    BS_SIMPLIFIEDGITFLOW1   : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_FORKINGFLOW          : False,
    BS_NONE                 : False,
    BS_ANARCHY              : False,
    BS_GITFLOW              : False,
  }

  dictBS_integration_frequency_medium  = {
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,

    BS_ANARCHY              : False,
    BS_FORKINGFLOW          : False,
    BS_NONE                 : False,
  }

  dictBS_integration_frequency_low  = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,

    BS_GITHUBFLOW           : False,
    BS_CONTINUOUSINTEG      : False,
    BS_NONE                 : False,
  }

  dictBS_integrate_with_merge = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,

    BS_ONEFLOW              : False,
    BS_ONEFLOWEXTENDED      : False,
  }

  dictBS_integrate_with_rebase = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,

    BS_GITHUBFLOW           : False,
}

  dictBS_integrate_with_squash = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,

    BS_GITFLOW              : False,
    BS_SIMPLIFIEDGITFLOW1   : False,
    BS_GITHUBFLOW           : False,
  }

  dictBS_error_tolerance_production_high = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,

    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
    BS_CONTINUOUSINTEG      : False,
  }

  dictBS_error_tolerance_production_regular = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : False,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_NONE                 : True,
  }

  dictBS_error_tolerance_production_low = {
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_CONTINUOUSINTEG      : True,

    BS_FORKINGFLOW          : False,
  }

  dictBS_release_branches_allowed = {
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
    BS_GITLABFLOW           : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : False,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : False,
  }

  dictBS_release_branches_not_allowed = {
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_GITFLOW              : False,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : False,
    BS_ONEFLOW              : False,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : False,
    BS_FORKINGFLOW          : False,
    BS_NONE                 : True,
  }

  dictBS_feature_branches_allowed = {
    BS_SINGLEDEV            : False,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : False,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : False,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,
  }

  dictBS_feature_branches_not_allowed = {
    BS_SINGLEDEV            : True,
    BS_TRUNKBASED           : True,
    BS_CONTINUOUSINTEG      : True,

    BS_ANARCHY              : False,
    BS_GITFLOW              : False,
    BS_GITHUBFLOW           : False,
    BS_GITLABFLOW           : False,
    BS_ONEFLOW              : False,
    BS_SIMPLIFIEDGITFLOW1   : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_FORKINGFLOW          : False,
    BS_NONE                 : False,
  }


  dictBS_deployment_frequency_high = {
    BS_GITHUBFLOW           : True,
    BS_TRUNKBASED           : True,
    BS_CONTINUOUSINTEG      : True,

    BS_SINGLEDEV            : False,
    BS_ANARCHY              : False,
    BS_GITFLOW              : False,
    BS_SIMPLIFIEDGITFLOW1   : False,
    BS_ONEFLOWEXTENDED      : False,
    BS_FORKINGFLOW          : False,
    BS_NONE                 : False,
  }

  dictBS_deployment_frequency_medium = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_TRUNKBASED           : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_CONTINUOUSINTEG      : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_NONE                 : True,

    BS_FORKINGFLOW          : False,
    BS_GITFLOW              : False,
  }

  dictBS_deployment_frequency_low = {
    BS_SINGLEDEV            : True,
    BS_ANARCHY              : True,
    BS_GITFLOW              : True,
    BS_GITLABFLOW           : True,
    BS_ONEFLOW              : True,
    BS_SIMPLIFIEDGITFLOW1   : True,
    BS_ONEFLOWEXTENDED      : True,
    BS_FORKINGFLOW          : True,
    BS_NONE                 : True,

    BS_GITHUBFLOW           : False,
    BS_TRUNKBASED           : False,
    BS_CONTINUOUSINTEG      : False,
  }




  def __init__(self) :

    self.listSelectorDicts = []

    self.dictSelectedBS = {}
    self.dictRejectedBS = {}
    self.listFinalBS = []


  def addSelector(self, addedSelectorDict) :

    self.listSelectorDicts.append(addedSelectorDict)


  def select(self) :

    for selDict in self.listSelectorDicts :
      print("select, selectDict ...")
      self.selectDict(selDict)

    print("========")
    print("select, check selected not rejected")
    rejected = self.dictRejectedBS
    for bs in self.dictSelectedBS :
      print("bs id = %d, selected %d times [%s]" % (bs, self.dictSelectedBS[bs], BranchingStrategy.dictNamesBS[bs]))

      if bs not in rejected :
        print("bs id = %d, never rejected -- adding to final list" % bs)
        self.listFinalBS.append(bs)
      else :
        print("bs id = %d, rejected %d times" % (bs, self.dictRejectedBS[bs]))

    print("====")
    print("select, list of final selected BS:")
    print(self.listFinalBS)
    for bs in self.listFinalBS :
      print("-- %d : %s" % (bs, BranchingStrategy.dictNamesBS[bs]))


  def selectDict(self, selDict) :

    for key in selDict :
      if selDict[key] == False :
        try :
          val = self.dictRejectedBS[key]
        except :
          val = 0
        self.dictRejectedBS[key] = val + 1

      else : # True
        try :
          val = self.dictSelectedBS[key]
        except :
          val = 0
        self.dictSelectedBS[key] = val + 1

    print("----")
    print("selectDict, dictRejectedBS:")
    print(self.dictRejectedBS)
    print("----")
    print("selectDict, dictSelectedBS:")
    print(self.dictSelectedBS)
    print("====")


if __name__ == "__main__":

  selector = BranchingStrategy()

  # example #0 : gitlab-flow, simplified git-flow
  selector.addSelector(BranchingStrategy.dictBS_1_developers)
  selector.addSelector(BranchingStrategy.dictBS_continuous_delivery)
  selector.addSelector(BranchingStrategy.dictBS_test_coverage_low)

  selector.select()

