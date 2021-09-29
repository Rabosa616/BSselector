
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

  """
  separator
  """

  dictOptionsSelectionDictionaries = {
    "1_developers"                               : dictBS_1_developers,
    "1_3_developers"                             : dictBS_1_3_developers,
    "2_8_developers"                             : dictBS_2_8_developers,
    "5_13_developers"                            : dictBS_5_13_developers,
    "8_21_developers"                            : dictBS_8_21_developers,
    "21_more_developers"                         : dictBS_21_more_developers,
    "test_coverage_low"                          : dictBS_test_coverage_low,
    "test_coverage_medium"                       : dictBS_test_coverage_medium,
    "test_coverage_high"                         : dictBS_test_coverage_high,
    "single_version_product"                     : dictBS_single_version_product,
    "multiple_version_product"                   : dictBS_multiple_version_product,
    "continuous_delivery"                        : dictBS_continuous_delivery,
    "short_project_life"                         : dictBS_short_project_life,
    "medium_project_life"                        : dictBS_medium_project_life,
    "long_project_life"                          : dictBS_long_project_life,
    "deploy_very_frequently"                     : dictBS_deploy_very_frequently,
    "deploy_frequently"                          : dictBS_deploy_frequently,
    "deploy_not_frequently"                      : dictBS_deploy_not_frequently,
    "deploy_rarely"                              : dictBS_deploy_rarely,
    "1_longlived_branches"                       : dictBS_1_longlived_branches,
    "2_longlived_branches"                       : dictBS_2_longlived_branches,
    "3_longlived_branches"                       : dictBS_3_longlived_branches,
    "1_subteams_or_projects"                     : dictBS_1_subteams_or_projects,
    "2_more_subteams_or_projects"                : dictBS_2_more_subteams_or_projects,
    "existing_codebase_zero_or_small"            : dictBS_existing_codebase_zero_or_small,
    "existing_codebase_large"                    : dictBS_existing_codebase_large,
    "existing_repositories_1"                    : dictBS_existing_repositories_1,
    "existing_repositories_2_more"               : dictBS_existing_repositories_2_more,
    "application_type_mobile"                    : dictBS_application_type_mobile,
    "application_type_web"                       : dictBS_application_type_web,
    "application_type_desktop"                   : dictBS_application_type_desktop,
    "application_type_firmware"                  : dictBS_application_type_firmware,
    "application_type_embedded"                  : dictBS_application_type_embedded,
    "maintain_single_version_product"            : dictBS_maintain_single_version_product,
    "maintain_multiple_version_product"          : dictBS_maintain_multiple_version_product,
    "integration_frequency_high"                 : dictBS_integration_frequency_high,
    "integration_frequency_medium"               : dictBS_integration_frequency_medium,
    "integration_frequency_low"                  : dictBS_integration_frequency_low,
    "integrate_with_merge"                       : dictBS_integrate_with_merge,
    "integrate_with_rebase"                      : dictBS_integrate_with_rebase,
    "integrate_with_squash"                      : dictBS_integrate_with_squash,
    "error_tolerance_production_high"            : dictBS_error_tolerance_production_high,
    "error_tolerance_production_regular"         : dictBS_error_tolerance_production_regular,
    "error_tolerance_production_low"             : dictBS_error_tolerance_production_low,
    "release_branches_allowed"                   : dictBS_release_branches_allowed,
    "release_branches_not_allowed"               : dictBS_release_branches_not_allowed,
    "feature_branches_allowed"                   : dictBS_feature_branches_allowed,
    "feature_branches_not_allowed"               : dictBS_feature_branches_not_allowed,
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
      #print("select, selectDict ...")
      self.selectDict(selDict)

    #print("========")
    #print("select, check selected not rejected")
    rejected = self.dictRejectedBS.keys()
    for bs in self.dictSelectedBS :
      #print("bs id = %d, selected %d times [%s]" % (bs, self.dictSelectedBS[bs], BranchingStrategy.dictNamesBS[bs]))

      if bs not in rejected :
        #print("bs id = %d, never rejected -- adding to final list" % bs)
        self.listFinalBS.append((bs, self.dictSelectedBS[bs]))
      else :
        #print("bs id = %d, rejected %d times" % (bs, self.dictRejectedBS[bs]))
        pass

    print("====")
    print("list of rejected BS:")
    for bs in sorted(self.dictRejectedBS, reverse = True) :
      print("-- BS id#%d : (score=-%d) %s" % (bs, self.dictRejectedBS[bs], BranchingStrategy.dictNamesBS[bs]))
    print("list of final selected BS:")
    for bsTuple in sorted(self.listFinalBS, key = lambda x: x[1], reverse = True) :
      print("-- BS id#%d : (score=%d) %s" % (bsTuple[0], bsTuple[1], BranchingStrategy.dictNamesBS[bsTuple[0]]))



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

    """
    print("----")
    print("selectDict, dictRejectedBS:")
    print(self.dictRejectedBS)
    print("----")
    print("selectDict, dictSelectedBS:")
    print(self.dictSelectedBS)
    print("====")
    """


if __name__ == "__main__":

  selector = BranchingStrategy()

  """
  # example #0 : gitlab-flow, simplified git-flow
  selector.addSelector(BranchingStrategy.dictBS_1_developers)
  selector.addSelector(BranchingStrategy.dictBS_continuous_delivery)
  selector.addSelector(BranchingStrategy.dictBS_test_coverage_low)
  """

  """
  # example #1 : git-flow, gitlab-flow, one-flow, Simplified git-flow, Forking workflow,
  selector.addSelector(BranchingStrategy.dictBS_5_13_developers)
  selector.addSelector(BranchingStrategy.dictBS_test_coverage_low)
  selector.addSelector(BranchingStrategy.dictBS_2_more_subteams_or_projects)
  selector.addSelector(BranchingStrategy.dictBS_maintain_multiple_version_product) 
  selector.addSelector(BranchingStrategy.dictBS_long_project_life)
  """

  """
  # example #2 : trunk-based development, github-flow, gitlab-flow, Continuous Integration, Simplified git-flow,
  selector.addSelector(BranchingStrategy.dictBS_1_3_developers)
  selector.addSelector(BranchingStrategy.dictBS_deploy_very_frequently)
  selector.addSelector(BranchingStrategy.dictBS_single_version_product)
  selector.addSelector(BranchingStrategy.dictBS_test_coverage_high)
  """

  """
  # example #2, searching text dictionary
  selector.addSelector(BranchingStrategy.dictOptionsSelectionDictionaries["1_3_developers"])
  selector.addSelector(BranchingStrategy.dictOptionsSelectionDictionaries["deploy_very_frequently"])
  selector.addSelector(BranchingStrategy.dictOptionsSelectionDictionaries["single_version_product"])
  selector.addSelector(BranchingStrategy.dictOptionsSelectionDictionaries["test_coverage_high"])
  """

  selector.select()

