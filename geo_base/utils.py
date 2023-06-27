class RoleChoice:
    AGENT = 'agent'
    COMBAT_UNIT = 'combat_unit'
    CHOICES = [(AGENT, 'Agent'), (COMBAT_UNIT, 'Combat unit')]


class UnitChoice:
    M777 = 'm777'
    HIMARS_M142 = 'himars_m142'
    STORM_SHADOW = 'storm_shadow'
    C_300 = 'c_300'
    CHOICES = [(M777, 'M777'), (HIMARS_M142, 'HIMARS M142'), (STORM_SHADOW, 'Storm Shadow'), (C_300, 'C-300')]


class TargetChoice:
    MILITARY_PERSONNEL = 'military_personnel'
    COMMAND_POST = 'command_post'
    MILITARY_EQUIPMENT = 'military_equipment'
    CHOICES = [(MILITARY_PERSONNEL, 'Military personnel'), (COMMAND_POST, 'Command post'),
               (MILITARY_EQUIPMENT, 'Military equipment')]
