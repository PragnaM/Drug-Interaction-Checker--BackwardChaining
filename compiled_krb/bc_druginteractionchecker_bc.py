# bc_druginteractionchecker_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def diabetes_check(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'any_diseases', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.diabetes_check: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Sulphonylureas(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.Sulphonylureas: got unexpected plan from when clause 1"
            with engine.prove('questions', 'any_diabetes_medication', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.Sulphonylureas: got unexpected plan from when clause 2"
                if context.lookup_data('drug1') in (1, 2, 3):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def CYP2C9inhibitors(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.CYP2C9inhibitors: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_diabetes', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.CYP2C9inhibitors: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (1, 2)	:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def drug_interaction1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.drug_interaction1: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_sulphonylureas(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_sulphonylureas: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_diabetes', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.no_interaction_sulphonylureas: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (3, 4, 5, 6, 7, 8, 9):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_sulphonylureas_others(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication_nointeraction_sulphonylureas', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_sulphonylureas_others: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Meglitanides(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.Meglitanides: got unexpected plan from when clause 1"
            with engine.prove('questions', 'any_diabetes_medication', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.Meglitanides: got unexpected plan from when clause 2"
                if context.lookup_data('drug1') in (4, ):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Gemfibrozil(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.Gemfibrozil: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_diabetes', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.Gemfibrozil: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (3, ):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def drug_interaction2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.drug_interaction2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_Meglitanides(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_Meglitanides: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_diabetes', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.no_interaction_Meglitanides: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (1, 2, 4, 5, 6, 7, 8, 9):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_Meglitanides_others(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication_nointeraction_Meglitanides', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_Meglitanides_others: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Metformin(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.Metformin: got unexpected plan from when clause 1"
            with engine.prove('questions', 'any_diabetes_medication', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.Metformin: got unexpected plan from when clause 2"
                if context.lookup_data('drug1') in (5, ):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Cimetidine(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.Cimetidine: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_diabetes', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.Cimetidine: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (4, ):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def drug_interaction3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.drug_interaction3: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_Metformin(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_Metformin: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_diabetes', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.no_interaction_Metformin: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (1, 2, 3, 5, 6, 7, 8, 9):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_Metformin_others(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication_nointeraction_Metformin', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_Metformin_others: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def hypertension_check(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'any_diseases', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.hypertension_check: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Captopril(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.Captopril: got unexpected plan from when clause 1"
            with engine.prove('questions', 'any_hypertension_medication', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.Captopril: got unexpected plan from when clause 2"
                if context.lookup_data('drug1') in (1, ):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Clomipramine(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.Clomipramine: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_hypertension', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.Clomipramine: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (1, )	:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def drug_interaction4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.drug_interaction4: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_captopril(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_captopril: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_hypertension', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.no_interaction_captopril: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (2, 3, 4):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_captopril_others(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication_nointeraction_captopril', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_captopril_others: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Enalapril(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.Enalapril: got unexpected plan from when clause 1"
            with engine.prove('questions', 'any_hypertension_medication', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.Enalapril: got unexpected plan from when clause 2"
                if context.lookup_data('drug1') in (2, ):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def CYP3A4inhibitors(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.CYP3A4inhibitors: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_hypertension', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.CYP3A4inhibitors: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (2, 3, 4)	:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def drug_interaction5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.drug_interaction5: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_enalapril(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_enalapril: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_hypertension', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.no_interaction_enalapril: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (1, ):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_enalapril_others(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication_nointeraction_enalapril', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_enalapril_others: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def CCBs(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.CCBs: got unexpected plan from when clause 1"
            with engine.prove('questions', 'any_hypertension_medication', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.CCBs: got unexpected plan from when clause 2"
                if context.lookup_data('drug1') in (3, 4)	:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def CYP3A4inhibitors1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.CYP3A4inhibitors1: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_hypertension', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.CYP3A4inhibitors1: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (2, 3, 4):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def drug_interaction6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.drug_interaction6: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_CCBs(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_medication', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_CCBs: got unexpected plan from when clause 1"
            with engine.prove('questions', 'check_medication_hypertension', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_druginteractionchecker.no_interaction_CCBs: got unexpected plan from when clause 2"
                if context.lookup_data('drug2') in (1, ):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_interaction_CCBs_others(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'disease_newmedication_nointeraction_CCBs', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_druginteractionchecker.no_interaction_CCBs_others: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_druginteractionchecker')
  
  bc_rule.bc_rule('diabetes_check', This_rule_base, 'disease',
                  diabetes_check, None,
                  (pattern.pattern_literal('Diabetes'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Sulphonylureas', This_rule_base, 'disease_medication',
                  Sulphonylureas, None,
                  (pattern.pattern_literal('Sulphonylureas'),),
                  (),
                  (pattern.pattern_literal('Diabetes'),
                   contexts.variable('drug1'),))
  
  bc_rule.bc_rule('CYP2C9inhibitors', This_rule_base, 'disease_newmedication',
                  CYP2C9inhibitors, None,
                  (pattern.pattern_literal('CYP2C9inhibitors'),),
                  (),
                  (pattern.pattern_literal('Sulphonylureas'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('drug_interaction1', This_rule_base, 'drug_interaction',
                  drug_interaction1, None,
                  (pattern.pattern_literal('Sulphonylureas'),
                   pattern.pattern_literal('CYP2C9inhibitors'),),
                  (),
                  (pattern.pattern_literal('CYP2C9inhibitors'),))
  
  bc_rule.bc_rule('no_interaction_sulphonylureas', This_rule_base, 'disease_newmedication_nointeraction_sulphonylureas',
                  no_interaction_sulphonylureas, None,
                  (pattern.pattern_literal('Others'),),
                  (),
                  (pattern.pattern_literal('Sulphonylureas'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('no_interaction_sulphonylureas_others', This_rule_base, 'drug_interaction',
                  no_interaction_sulphonylureas_others, None,
                  (pattern.pattern_literal('NoInteraction'),
                   pattern.pattern_literal('Safe'),),
                  (),
                  (pattern.pattern_literal('Others'),))
  
  bc_rule.bc_rule('Meglitanides', This_rule_base, 'disease_medication',
                  Meglitanides, None,
                  (pattern.pattern_literal('Meglitanides'),),
                  (),
                  (pattern.pattern_literal('Diabetes'),
                   contexts.variable('drug1'),))
  
  bc_rule.bc_rule('Gemfibrozil', This_rule_base, 'disease_newmedication',
                  Gemfibrozil, None,
                  (pattern.pattern_literal('Gemfibrozil'),),
                  (),
                  (pattern.pattern_literal('Meglitanides'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('drug_interaction2', This_rule_base, 'drug_interaction',
                  drug_interaction2, None,
                  (pattern.pattern_literal('Meglitanides'),
                   pattern.pattern_literal('Gemfibrozil'),),
                  (),
                  (pattern.pattern_literal('Gemfibrozil'),))
  
  bc_rule.bc_rule('no_interaction_Meglitanides', This_rule_base, 'disease_newmedication_nointeraction_Meglitanides',
                  no_interaction_Meglitanides, None,
                  (pattern.pattern_literal('Others'),),
                  (),
                  (pattern.pattern_literal('Meglitanides'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('no_interaction_Meglitanides_others', This_rule_base, 'drug_interaction',
                  no_interaction_Meglitanides_others, None,
                  (pattern.pattern_literal('NoInteraction'),
                   pattern.pattern_literal('Safe'),),
                  (),
                  (pattern.pattern_literal('Others'),))
  
  bc_rule.bc_rule('Metformin', This_rule_base, 'disease_medication',
                  Metformin, None,
                  (pattern.pattern_literal('Metformin'),),
                  (),
                  (pattern.pattern_literal('Diabetes'),
                   contexts.variable('drug1'),))
  
  bc_rule.bc_rule('Cimetidine', This_rule_base, 'disease_newmedication',
                  Cimetidine, None,
                  (pattern.pattern_literal('Cimetidine'),),
                  (),
                  (pattern.pattern_literal('Metformin'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('drug_interaction3', This_rule_base, 'drug_interaction',
                  drug_interaction3, None,
                  (pattern.pattern_literal('Metformin'),
                   pattern.pattern_literal('Cimetidine'),),
                  (),
                  (pattern.pattern_literal('Cimetidine'),))
  
  bc_rule.bc_rule('no_interaction_Metformin', This_rule_base, 'disease_newmedication_nointeraction_Metformin',
                  no_interaction_Metformin, None,
                  (pattern.pattern_literal('Others'),),
                  (),
                  (pattern.pattern_literal('Metformin'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('no_interaction_Metformin_others', This_rule_base, 'drug_interaction',
                  no_interaction_Metformin_others, None,
                  (pattern.pattern_literal('NoInteraction'),
                   pattern.pattern_literal('Safe'),),
                  (),
                  (pattern.pattern_literal('Others'),))
  
  bc_rule.bc_rule('hypertension_check', This_rule_base, 'disease',
                  hypertension_check, None,
                  (pattern.pattern_literal('Hypertension'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Captopril', This_rule_base, 'disease_medication',
                  Captopril, None,
                  (pattern.pattern_literal('Captopril'),),
                  (),
                  (pattern.pattern_literal('Hypertension'),
                   contexts.variable('drug1'),))
  
  bc_rule.bc_rule('Clomipramine', This_rule_base, 'disease_newmedication',
                  Clomipramine, None,
                  (pattern.pattern_literal('Clomipramine'),),
                  (),
                  (pattern.pattern_literal('Captopril'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('drug_interaction4', This_rule_base, 'drug_interaction',
                  drug_interaction4, None,
                  (pattern.pattern_literal('Captopril'),
                   pattern.pattern_literal('Clomipramine'),),
                  (),
                  (pattern.pattern_literal('Clomipramine'),))
  
  bc_rule.bc_rule('no_interaction_captopril', This_rule_base, 'disease_newmedication_nointeraction_captopril',
                  no_interaction_captopril, None,
                  (pattern.pattern_literal('Others'),),
                  (),
                  (pattern.pattern_literal('Captopril'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('no_interaction_captopril_others', This_rule_base, 'drug_interaction',
                  no_interaction_captopril_others, None,
                  (pattern.pattern_literal('NoInteraction'),
                   pattern.pattern_literal('Safe'),),
                  (),
                  (pattern.pattern_literal('Others'),))
  
  bc_rule.bc_rule('Enalapril', This_rule_base, 'disease_medication',
                  Enalapril, None,
                  (pattern.pattern_literal('Enalapril'),),
                  (),
                  (pattern.pattern_literal('Hypertension'),
                   contexts.variable('drug1'),))
  
  bc_rule.bc_rule('CYP3A4inhibitors', This_rule_base, 'disease_newmedication',
                  CYP3A4inhibitors, None,
                  (pattern.pattern_literal('CYP3A4inhibitors'),),
                  (),
                  (pattern.pattern_literal('Enalapril'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('drug_interaction5', This_rule_base, 'drug_interaction',
                  drug_interaction5, None,
                  (pattern.pattern_literal('Enalapril'),
                   pattern.pattern_literal('CYP3A4inhibitors'),),
                  (),
                  (pattern.pattern_literal('CYP3A4inhibitors'),))
  
  bc_rule.bc_rule('no_interaction_enalapril', This_rule_base, 'disease_newmedication_nointeraction_enalapril',
                  no_interaction_enalapril, None,
                  (pattern.pattern_literal('Others'),),
                  (),
                  (pattern.pattern_literal('Enalapril'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('no_interaction_enalapril_others', This_rule_base, 'drug_interaction',
                  no_interaction_enalapril_others, None,
                  (pattern.pattern_literal('NoInteraction'),
                   pattern.pattern_literal('Safe'),),
                  (),
                  (pattern.pattern_literal('Others'),))
  
  bc_rule.bc_rule('CCBs', This_rule_base, 'disease_medication',
                  CCBs, None,
                  (pattern.pattern_literal('CCBs'),),
                  (),
                  (pattern.pattern_literal('Hypertension'),
                   contexts.variable('drug1'),))
  
  bc_rule.bc_rule('CYP3A4inhibitors1', This_rule_base, 'disease_newmedication',
                  CYP3A4inhibitors1, None,
                  (pattern.pattern_literal('CYP3A4inhibitors1'),),
                  (),
                  (pattern.pattern_literal('CCBs'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('drug_interaction6', This_rule_base, 'drug_interaction',
                  drug_interaction6, None,
                  (pattern.pattern_literal('CCBs'),
                   pattern.pattern_literal('CYP3A4inhibitors'),),
                  (),
                  (pattern.pattern_literal('CYP3A4inhibitors1'),))
  
  bc_rule.bc_rule('no_interaction_CCBs', This_rule_base, 'disease_newmedication_nointeraction_CCBs',
                  no_interaction_CCBs, None,
                  (pattern.pattern_literal('Others'),),
                  (),
                  (pattern.pattern_literal('CCBs'),
                   contexts.variable('drug2'),))
  
  bc_rule.bc_rule('no_interaction_CCBs_others', This_rule_base, 'drug_interaction',
                  no_interaction_CCBs_others, None,
                  (pattern.pattern_literal('NoInteraction'),
                   pattern.pattern_literal('Safe'),),
                  (),
                  (pattern.pattern_literal('Others'),))


Krb_filename = '..\\bc_druginteractionchecker.krb'
Krb_lineno_map = (
    ((14, 18), (3, 3)),
    ((20, 25), (5, 5)),
    ((26, 26), (6, 6)),
    ((39, 43), (9, 9)),
    ((45, 50), (11, 11)),
    ((51, 56), (12, 12)),
    ((57, 57), (13, 13)),
    ((70, 74), (16, 16)),
    ((76, 81), (18, 18)),
    ((82, 87), (19, 19)),
    ((88, 88), (20, 20)),
    ((101, 105), (23, 23)),
    ((107, 112), (25, 25)),
    ((125, 129), (28, 28)),
    ((131, 136), (30, 30)),
    ((137, 142), (31, 31)),
    ((143, 143), (32, 32)),
    ((156, 160), (35, 35)),
    ((162, 167), (37, 37)),
    ((180, 184), (40, 40)),
    ((186, 191), (42, 42)),
    ((192, 197), (43, 43)),
    ((198, 198), (44, 44)),
    ((211, 215), (47, 47)),
    ((217, 222), (49, 49)),
    ((223, 228), (50, 50)),
    ((229, 229), (51, 51)),
    ((242, 246), (54, 54)),
    ((248, 253), (56, 56)),
    ((266, 270), (59, 59)),
    ((272, 277), (61, 61)),
    ((278, 283), (62, 62)),
    ((284, 284), (63, 63)),
    ((297, 301), (66, 66)),
    ((303, 308), (68, 68)),
    ((321, 325), (71, 71)),
    ((327, 332), (73, 73)),
    ((333, 338), (74, 74)),
    ((339, 339), (75, 75)),
    ((352, 356), (78, 78)),
    ((358, 363), (80, 80)),
    ((364, 369), (81, 81)),
    ((370, 370), (82, 82)),
    ((383, 387), (85, 85)),
    ((389, 394), (87, 87)),
    ((407, 411), (90, 90)),
    ((413, 418), (92, 92)),
    ((419, 424), (93, 93)),
    ((425, 425), (94, 94)),
    ((438, 442), (97, 97)),
    ((444, 449), (99, 99)),
    ((462, 466), (102, 102)),
    ((468, 473), (104, 104)),
    ((474, 474), (105, 105)),
    ((487, 491), (108, 108)),
    ((493, 498), (110, 110)),
    ((499, 504), (111, 111)),
    ((505, 505), (112, 112)),
    ((518, 522), (115, 115)),
    ((524, 529), (117, 117)),
    ((530, 535), (118, 118)),
    ((536, 536), (119, 119)),
    ((549, 553), (122, 122)),
    ((555, 560), (124, 124)),
    ((573, 577), (127, 127)),
    ((579, 584), (129, 129)),
    ((585, 590), (130, 130)),
    ((591, 591), (131, 131)),
    ((604, 608), (134, 134)),
    ((610, 615), (136, 136)),
    ((628, 632), (139, 139)),
    ((634, 639), (141, 141)),
    ((640, 645), (142, 142)),
    ((646, 646), (143, 143)),
    ((659, 663), (146, 146)),
    ((665, 670), (148, 148)),
    ((671, 676), (149, 149)),
    ((677, 677), (150, 150)),
    ((690, 694), (153, 153)),
    ((696, 701), (155, 155)),
    ((714, 718), (158, 158)),
    ((720, 725), (160, 160)),
    ((726, 731), (161, 161)),
    ((732, 732), (162, 162)),
    ((745, 749), (165, 165)),
    ((751, 756), (167, 167)),
    ((769, 773), (170, 170)),
    ((775, 780), (172, 172)),
    ((781, 786), (173, 173)),
    ((787, 787), (174, 174)),
    ((800, 804), (177, 177)),
    ((806, 811), (179, 179)),
    ((812, 817), (180, 180)),
    ((818, 818), (181, 181)),
    ((831, 835), (184, 184)),
    ((837, 842), (186, 186)),
    ((855, 859), (189, 189)),
    ((861, 866), (191, 191)),
    ((867, 872), (192, 192)),
    ((873, 873), (193, 193)),
    ((886, 890), (196, 196)),
    ((892, 897), (198, 198)),
)
