# bc_rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def shortness(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'shortness_of_breath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'shortnessOfBreath',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fatigue(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'fatigue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'fatigue',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def chestPain(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'chestPain',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def no_major_symptoms(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'shortness_of_breath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'fatigue', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'chest_pain', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                engine.assert_('symptoms', 'inconclusive',
                               (rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def LS_Heart_failure(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'coughing', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                engine.assert_('symptoms', 'inconclusive',
                               (rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def RS_Heart_failure(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'shortnessOfBreath', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'irregular_heartbeat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'leg_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'abdominal_swelling', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'weight_gain', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        engine.assert_('symptoms', 'diagnosis',
                                       (rule.pattern(0).as_data(context),)),
                        engine.assert_('symptoms', 'inconclusive',
                                       (rule.pattern(1).as_data(context),)),
                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'heart_attack', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'cholesterol', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'Family_history', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'highBloodPressure', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        with knowledge_base.Gen_once if index == 5 \
                                 else engine.lookup('questions', 'smoking', context,
                                                    rule.foreach_patterns(5)) \
                          as gen_5:
                          for dummy in gen_5:
                            engine.assert_('symptoms', 'diagnosis',
                                           (rule.pattern(0).as_data(context),)),
                            engine.assert_('symptoms', 'inconclusive',
                                           (rule.pattern(1).as_data(context),)),
                            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'cholesterol', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'Family_history', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'highBloodPressure', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'smoking', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        engine.assert_('symptoms', 'diagnosis',
                                       (rule.pattern(0).as_data(context),)),
                        engine.assert_('symptoms', 'inconclusive',
                                       (rule.pattern(1).as_data(context),)),
                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'heart_attack', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'cholesterol', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                engine.assert_('symptoms', 'inconclusive',
                               (rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'cholesterol', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'Family_history', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                engine.assert_('symptoms', 'inconclusive',
                               (rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def coronary_artery4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'cholesterol', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'smoking', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                engine.assert_('symptoms', 'inconclusive',
                               (rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'upper_body', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'cold_sweat', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'indigestion', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    engine.assert_('symptoms', 'inconclusive',
                                   (rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'upper_body', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'cold_sweat', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                engine.assert_('symptoms', 'inconclusive',
                               (rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'upper_body', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'indigestion', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                engine.assert_('symptoms', 'inconclusive',
                               (rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'chest_pain', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'upper_body', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('symptoms', 'diagnosis',
                           (rule.pattern(0).as_data(context),)),
            engine.assert_('symptoms', 'inconclusive',
                           (rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def tachycardia_arrhythmia(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'fluttering', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'racing', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'anxiety', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'faint', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    engine.assert_('symptoms', 'inconclusive',
                                   (rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def bradycardia_arrhythmia(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'slow', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'dizzy', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'memory', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'faint', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('symptoms', 'diagnosis',
                                   (rule.pattern(0).as_data(context),)),
                    engine.assert_('symptoms', 'inconclusive',
                                   (rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease_regurgitation(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'abdominal_swelling', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'leg_swelling', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'dizzy', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'faint', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        engine.assert_('symptoms', 'diagnosis',
                                       (rule.pattern(0).as_data(context),)),
                        engine.assert_('symptoms', 'inconclusive',
                                       (rule.pattern(1).as_data(context),)),
                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'dizzy', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'faint', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('symptoms', 'diagnosis',
                               (rule.pattern(0).as_data(context),)),
                engine.assert_('symptoms', 'inconclusive',
                               (rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'dizzy', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('symptoms', 'diagnosis',
                           (rule.pattern(0).as_data(context),)),
            engine.assert_('symptoms', 'inconclusive',
                           (rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'faint', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('symptoms', 'diagnosis',
                           (rule.pattern(0).as_data(context),)),
            engine.assert_('symptoms', 'inconclusive',
                           (rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_valve_disease4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('questions', 'heart_murmur', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'diagnosis',
                       (rule.pattern(0).as_data(context),)),
        engine.assert_('symptoms', 'inconclusive',
                       (rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def test_inconclusive(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('symptoms', 'inconclusive', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('symptoms', 'diagnosis',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_rules')
  
  fc_rule.fc_rule('shortness', This_rule_base, shortness,
    (('questions', 'shortness_of_breath',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fatigue', This_rule_base, fatigue,
    (('questions', 'fatigue',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('chestPain', This_rule_base, chestPain,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('no_major_symptoms', This_rule_base, no_major_symptoms,
    (('questions', 'shortness_of_breath',
      (pattern.pattern_literal(False),),
      False),
     ('questions', 'fatigue',
      (pattern.pattern_literal(False),),
      False),
     ('questions', 'chest_pain',
      (pattern.pattern_literal(False),),
      False),),
    (pattern.pattern_literal("No heart disease symptoms detected!"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('LS_Heart_failure', This_rule_base, LS_Heart_failure,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'coughing',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Left sided heart failure"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('RS_Heart_failure', This_rule_base, RS_Heart_failure,
    (('symptoms', 'shortnessOfBreath',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'irregular_heartbeat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'leg_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'abdominal_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'weight_gain',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Right sided heart failure"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('coronary_artery', This_rule_base, coronary_artery,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'heart_attack',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'Family_history',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'highBloodPressure',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'smoking',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('coronary_artery1', This_rule_base, coronary_artery1,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'Family_history',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'highBloodPressure',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'smoking',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('coronary_artery2', This_rule_base, coronary_artery2,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'heart_attack',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('coronary_artery3', This_rule_base, coronary_artery3,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'Family_history',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('coronary_artery4', This_rule_base, coronary_artery4,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cholesterol',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'smoking',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Coronary artery disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_attack', This_rule_base, heart_attack,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'upper_body',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cold_sweat',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'indigestion',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Infraction (Heart attack)"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_attack2', This_rule_base, heart_attack2,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'upper_body',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'cold_sweat',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Infraction (Heart attack)"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_attack3', This_rule_base, heart_attack3,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'upper_body',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'indigestion',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Infraction (Heart attack)"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_attack4', This_rule_base, heart_attack4,
    (('questions', 'chest_pain',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'upper_body',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Infraction (Heart attack)"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('tachycardia_arrhythmia', This_rule_base, tachycardia_arrhythmia,
    (('questions', 'fluttering',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'racing',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'anxiety',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Tachycardia Arrhythmia"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('bradycardia_arrhythmia', This_rule_base, bradycardia_arrhythmia,
    (('questions', 'slow',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'dizzy',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'memory',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Bradycardia Arrhythmia"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_valve_disease_regurgitation', This_rule_base, heart_valve_disease_regurgitation,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'abdominal_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'leg_swelling',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'dizzy',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease (valve regurgitation)"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_valve_disease1', This_rule_base, heart_valve_disease1,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'dizzy',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_valve_disease2', This_rule_base, heart_valve_disease2,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'dizzy',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_valve_disease3', This_rule_base, heart_valve_disease3,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),
     ('questions', 'faint',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('heart_valve_disease4', This_rule_base, heart_valve_disease4,
    (('questions', 'heart_murmur',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Heart Valve Disease"),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('test_inconclusive', This_rule_base, test_inconclusive,
    (('symptoms', 'inconclusive',
      (pattern.pattern_literal(True),),
      False),),
    (pattern.pattern_literal("Test Inconclusive"),))


Krb_filename = '../bc_rules.krb'
Krb_lineno_map = (
    ((12, 16), (5, 5)),
    ((17, 18), (7, 7)),
    ((27, 31), (11, 11)),
    ((32, 33), (13, 13)),
    ((42, 46), (17, 17)),
    ((47, 48), (19, 19)),
    ((57, 61), (24, 24)),
    ((62, 66), (25, 25)),
    ((67, 71), (26, 26)),
    ((72, 73), (28, 28)),
    ((74, 75), (29, 29)),
    ((84, 88), (33, 33)),
    ((89, 93), (34, 34)),
    ((94, 98), (35, 35)),
    ((99, 100), (37, 37)),
    ((101, 102), (38, 38)),
    ((111, 115), (42, 42)),
    ((116, 120), (43, 43)),
    ((121, 125), (44, 44)),
    ((126, 130), (45, 45)),
    ((131, 135), (46, 46)),
    ((136, 137), (48, 48)),
    ((138, 139), (49, 49)),
    ((148, 152), (54, 54)),
    ((153, 157), (55, 55)),
    ((158, 162), (56, 56)),
    ((163, 167), (57, 57)),
    ((168, 172), (58, 58)),
    ((173, 177), (59, 59)),
    ((178, 179), (61, 61)),
    ((180, 181), (62, 62)),
    ((190, 194), (66, 66)),
    ((195, 199), (67, 67)),
    ((200, 204), (68, 68)),
    ((205, 209), (69, 69)),
    ((210, 214), (70, 70)),
    ((215, 216), (72, 72)),
    ((217, 218), (73, 73)),
    ((227, 231), (78, 78)),
    ((232, 236), (79, 79)),
    ((237, 241), (80, 80)),
    ((242, 243), (82, 82)),
    ((244, 245), (83, 83)),
    ((254, 258), (87, 87)),
    ((259, 263), (88, 88)),
    ((264, 268), (89, 89)),
    ((269, 270), (91, 91)),
    ((271, 272), (92, 92)),
    ((281, 285), (96, 96)),
    ((286, 290), (97, 97)),
    ((291, 295), (98, 98)),
    ((296, 297), (100, 100)),
    ((298, 299), (101, 101)),
    ((308, 312), (106, 106)),
    ((313, 317), (107, 107)),
    ((318, 322), (108, 108)),
    ((323, 327), (109, 109)),
    ((328, 329), (111, 111)),
    ((330, 331), (112, 112)),
    ((340, 344), (116, 116)),
    ((345, 349), (117, 117)),
    ((350, 354), (118, 118)),
    ((355, 356), (120, 120)),
    ((357, 358), (121, 121)),
    ((367, 371), (125, 125)),
    ((372, 376), (126, 126)),
    ((377, 381), (127, 127)),
    ((382, 383), (129, 129)),
    ((384, 385), (130, 130)),
    ((394, 398), (134, 134)),
    ((399, 403), (135, 135)),
    ((404, 405), (137, 137)),
    ((406, 407), (138, 138)),
    ((416, 420), (142, 142)),
    ((421, 425), (143, 143)),
    ((426, 430), (144, 144)),
    ((431, 435), (145, 145)),
    ((436, 437), (147, 147)),
    ((438, 439), (148, 148)),
    ((448, 452), (152, 152)),
    ((453, 457), (153, 153)),
    ((458, 462), (154, 154)),
    ((463, 467), (155, 155)),
    ((468, 469), (157, 157)),
    ((470, 471), (158, 158)),
    ((480, 484), (162, 162)),
    ((485, 489), (163, 163)),
    ((490, 494), (164, 164)),
    ((495, 499), (165, 165)),
    ((500, 504), (166, 166)),
    ((505, 506), (168, 168)),
    ((507, 508), (169, 169)),
    ((517, 521), (173, 173)),
    ((522, 526), (174, 174)),
    ((527, 531), (175, 175)),
    ((532, 533), (177, 177)),
    ((534, 535), (178, 178)),
    ((544, 548), (182, 182)),
    ((549, 553), (183, 183)),
    ((554, 555), (185, 185)),
    ((556, 557), (186, 186)),
    ((566, 570), (191, 191)),
    ((571, 575), (192, 192)),
    ((576, 577), (194, 194)),
    ((578, 579), (195, 195)),
    ((588, 592), (199, 199)),
    ((593, 594), (201, 201)),
    ((595, 596), (202, 202)),
    ((605, 609), (206, 206)),
    ((610, 611), (208, 208)),
)
