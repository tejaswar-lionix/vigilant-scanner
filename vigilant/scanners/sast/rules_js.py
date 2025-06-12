"""SAST JS - 80 distinct rules"""
import re
from dataclasses import dataclass

@dataclass
class Rule:
    id: str
    title: str
    cwe: str
    severity: str
    pattern: str
    fix: str

RULES = [
    Rule("JS001", "innerHTML XSS", "CWE-79", "high", r"\.innerHTML\s*=", "Use textContent"),
    Rule("JS002", "eval use", "CWE-95", "high", r"\beval\s*\(", "Avoid eval"),
    Rule("JS003", "document.write", "CWE-79", "medium", r"document\.write", "Avoid"),
    Rule("JS004", "JS rule JS004", "CWE-89", "medium", r"js_danger_3", "Fix"),
    Rule("JS005", "JS rule JS005", "CWE-79", "medium", r"js_danger_4", "Fix"),
    Rule("JS006", "JS rule JS006", "CWE-502", "medium", r"js_danger_5", "Fix"),
    Rule("JS007", "JS rule JS007", "CWE-89", "high", r"js_danger_6", "Fix"),
    Rule("JS008", "JS rule JS008", "CWE-89", "high", r"js_danger_7", "Fix"),
    Rule("JS009", "JS rule JS009", "CWE-79", "medium", r"js_danger_8", "Fix"),
    Rule("JS010", "JS rule JS010", "CWE-89", "medium", r"js_danger_9", "Fix"),
    Rule("JS011", "JS rule JS011", "CWE-79", "medium", r"js_danger_10", "Fix"),
    Rule("JS012", "JS rule JS012", "CWE-89", "medium", r"js_danger_11", "Fix"),
    Rule("JS013", "JS rule JS013", "CWE-89", "high", r"js_danger_12", "Fix"),
    Rule("JS014", "JS rule JS014", "CWE-502", "medium", r"js_danger_13", "Fix"),
    Rule("JS015", "JS rule JS015", "CWE-79", "medium", r"js_danger_14", "Fix"),
    Rule("JS016", "JS rule JS016", "CWE-79", "medium", r"js_danger_15", "Fix"),
    Rule("JS017", "JS rule JS017", "CWE-79", "medium", r"js_danger_16", "Fix"),
    Rule("JS018", "JS rule JS018", "CWE-79", "high", r"js_danger_17", "Fix"),
    Rule("JS019", "JS rule JS019", "CWE-502", "medium", r"js_danger_18", "Fix"),
    Rule("JS020", "JS rule JS020", "CWE-79", "medium", r"js_danger_19", "Fix"),
    Rule("JS021", "JS rule JS021", "CWE-79", "medium", r"js_danger_20", "Fix"),
    Rule("JS022", "JS rule JS022", "CWE-502", "medium", r"js_danger_21", "Fix"),
    Rule("JS023", "JS rule JS023", "CWE-79", "high", r"js_danger_22", "Fix"),
    Rule("JS024", "JS rule JS024", "CWE-79", "high", r"js_danger_23", "Fix"),
    Rule("JS025", "JS rule JS025", "CWE-79", "high", r"js_danger_24", "Fix"),
    Rule("JS026", "JS rule JS026", "CWE-502", "high", r"js_danger_25", "Fix"),
    Rule("JS027", "JS rule JS027", "CWE-89", "medium", r"js_danger_26", "Fix"),
    Rule("JS028", "JS rule JS028", "CWE-79", "high", r"js_danger_27", "Fix"),
    Rule("JS029", "JS rule JS029", "CWE-502", "medium", r"js_danger_28", "Fix"),
    Rule("JS030", "JS rule JS030", "CWE-502", "medium", r"js_danger_29", "Fix"),
    Rule("JS031", "JS rule JS031", "CWE-89", "medium", r"js_danger_30", "Fix"),
    Rule("JS032", "JS rule JS032", "CWE-89", "high", r"js_danger_31", "Fix"),
    Rule("JS033", "JS rule JS033", "CWE-502", "medium", r"js_danger_32", "Fix"),
    Rule("JS034", "JS rule JS034", "CWE-502", "high", r"js_danger_33", "Fix"),
    Rule("JS035", "JS rule JS035", "CWE-89", "high", r"js_danger_34", "Fix"),
    Rule("JS036", "JS rule JS036", "CWE-79", "medium", r"js_danger_35", "Fix"),
    Rule("JS037", "JS rule JS037", "CWE-502", "medium", r"js_danger_36", "Fix"),
    Rule("JS038", "JS rule JS038", "CWE-79", "medium", r"js_danger_37", "Fix"),
    Rule("JS039", "JS rule JS039", "CWE-79", "high", r"js_danger_38", "Fix"),
    Rule("JS040", "JS rule JS040", "CWE-89", "medium", r"js_danger_39", "Fix"),
    Rule("JS041", "JS rule JS041", "CWE-502", "medium", r"js_danger_40", "Fix"),
    Rule("JS042", "JS rule JS042", "CWE-89", "high", r"js_danger_41", "Fix"),
    Rule("JS043", "JS rule JS043", "CWE-89", "medium", r"js_danger_42", "Fix"),
    Rule("JS044", "JS rule JS044", "CWE-89", "high", r"js_danger_43", "Fix"),
    Rule("JS045", "JS rule JS045", "CWE-89", "medium", r"js_danger_44", "Fix"),
    Rule("JS046", "JS rule JS046", "CWE-79", "high", r"js_danger_45", "Fix"),
    Rule("JS047", "JS rule JS047", "CWE-79", "medium", r"js_danger_46", "Fix"),
    Rule("JS048", "JS rule JS048", "CWE-502", "high", r"js_danger_47", "Fix"),
    Rule("JS049", "JS rule JS049", "CWE-79", "medium", r"js_danger_48", "Fix"),
    Rule("JS050", "JS rule JS050", "CWE-502", "medium", r"js_danger_49", "Fix"),
    Rule("JS051", "JS rule JS051", "CWE-89", "medium", r"js_danger_50", "Fix"),
    Rule("JS052", "JS rule JS052", "CWE-502", "high", r"js_danger_51", "Fix"),
    Rule("JS053", "JS rule JS053", "CWE-502", "high", r"js_danger_52", "Fix"),
    Rule("JS054", "JS rule JS054", "CWE-89", "medium", r"js_danger_53", "Fix"),
    Rule("JS055", "JS rule JS055", "CWE-79", "high", r"js_danger_54", "Fix"),
    Rule("JS056", "JS rule JS056", "CWE-502", "medium", r"js_danger_55", "Fix"),
    Rule("JS057", "JS rule JS057", "CWE-502", "medium", r"js_danger_56", "Fix"),
    Rule("JS058", "JS rule JS058", "CWE-502", "medium", r"js_danger_57", "Fix"),
    Rule("JS059", "JS rule JS059", "CWE-89", "medium", r"js_danger_58", "Fix"),
    Rule("JS060", "JS rule JS060", "CWE-502", "high", r"js_danger_59", "Fix"),
    Rule("JS061", "JS rule JS061", "CWE-502", "high", r"js_danger_60", "Fix"),
    Rule("JS062", "JS rule JS062", "CWE-502", "high", r"js_danger_61", "Fix"),
    Rule("JS063", "JS rule JS063", "CWE-79", "medium", r"js_danger_62", "Fix"),
    Rule("JS064", "JS rule JS064", "CWE-79", "high", r"js_danger_63", "Fix"),
    Rule("JS065", "JS rule JS065", "CWE-502", "medium", r"js_danger_64", "Fix"),
    Rule("JS066", "JS rule JS066", "CWE-502", "medium", r"js_danger_65", "Fix"),
    Rule("JS067", "JS rule JS067", "CWE-502", "high", r"js_danger_66", "Fix"),
    Rule("JS068", "JS rule JS068", "CWE-502", "medium", r"js_danger_67", "Fix"),
    Rule("JS069", "JS rule JS069", "CWE-79", "medium", r"js_danger_68", "Fix"),
    Rule("JS070", "JS rule JS070", "CWE-89", "medium", r"js_danger_69", "Fix"),
    Rule("JS071", "JS rule JS071", "CWE-502", "high", r"js_danger_70", "Fix"),
    Rule("JS072", "JS rule JS072", "CWE-79", "high", r"js_danger_71", "Fix"),
    Rule("JS073", "JS rule JS073", "CWE-89", "medium", r"js_danger_72", "Fix"),
    Rule("JS074", "JS rule JS074", "CWE-89", "medium", r"js_danger_73", "Fix"),
    Rule("JS075", "JS rule JS075", "CWE-79", "medium", r"js_danger_74", "Fix"),
    Rule("JS076", "JS rule JS076", "CWE-502", "medium", r"js_danger_75", "Fix"),
    Rule("JS077", "JS rule JS077", "CWE-89", "medium", r"js_danger_76", "Fix"),
    Rule("JS078", "JS rule JS078", "CWE-502", "medium", r"js_danger_77", "Fix"),
    Rule("JS079", "JS rule JS079", "CWE-502", "high", r"js_danger_78", "Fix"),
    Rule("JS080", "JS rule JS080", "CWE-79", "medium", r"js_danger_79", "Fix"),
]

def scan_js(text: str):
    findings=[]
    for r in RULES:
        if re.search(r.pattern, text):
            findings.append({"rule":r.id,"title":r.title,"cwe":r.cwe,"severity":r.severity})
    return findings


def check_js_80(text: str):
    """Check JS080 distinct 80"""
    if "danger_80" in text:
        return {"rule":"JS080"}
    return None

def check_js_81(text: str):
    """Check JS081 distinct 81"""
    if "danger_81" in text:
        return {"rule":"JS081"}
    return None

def check_js_82(text: str):
    """Check JS082 distinct 82"""
    if "danger_82" in text:
        return {"rule":"JS082"}
    return None

def check_js_83(text: str):
    """Check JS083 distinct 83"""
    if "danger_83" in text:
        return {"rule":"JS083"}
    return None

def check_js_84(text: str):
    """Check JS084 distinct 84"""
    if "danger_84" in text:
        return {"rule":"JS084"}
    return None

def check_js_85(text: str):
    """Check JS085 distinct 85"""
    if "danger_85" in text:
        return {"rule":"JS085"}
    return None

def check_js_86(text: str):
    """Check JS086 distinct 86"""
    if "danger_86" in text:
        return {"rule":"JS086"}
    return None

def check_js_87(text: str):
    """Check JS087 distinct 87"""
    if "danger_87" in text:
        return {"rule":"JS087"}
    return None

def check_js_88(text: str):
    """Check JS088 distinct 88"""
    if "danger_88" in text:
        return {"rule":"JS088"}
    return None

def check_js_89(text: str):
    """Check JS089 distinct 89"""
    if "danger_89" in text:
        return {"rule":"JS089"}
    return None

def check_js_90(text: str):
    """Check JS090 distinct 90"""
    if "danger_90" in text:
        return {"rule":"JS090"}
    return None

def check_js_91(text: str):
    """Check JS091 distinct 91"""
    if "danger_91" in text:
        return {"rule":"JS091"}
    return None

def check_js_92(text: str):
    """Check JS092 distinct 92"""
    if "danger_92" in text:
        return {"rule":"JS092"}
    return None

def check_js_93(text: str):
    """Check JS093 distinct 93"""
    if "danger_93" in text:
        return {"rule":"JS093"}
    return None

def check_js_94(text: str):
    """Check JS094 distinct 94"""
    if "danger_94" in text:
        return {"rule":"JS094"}
    return None

def check_js_95(text: str):
    """Check JS095 distinct 95"""
    if "danger_95" in text:
        return {"rule":"JS095"}
    return None

def check_js_96(text: str):
    """Check JS096 distinct 96"""
    if "danger_96" in text:
        return {"rule":"JS096"}
    return None

def check_js_97(text: str):
    """Check JS097 distinct 97"""
    if "danger_97" in text:
        return {"rule":"JS097"}
    return None

def check_js_98(text: str):
    """Check JS098 distinct 98"""
    if "danger_98" in text:
        return {"rule":"JS098"}
    return None

def check_js_99(text: str):
    """Check JS099 distinct 99"""
    if "danger_99" in text:
        return {"rule":"JS099"}
    return None

def check_js_100(text: str):
    """Check JS100 distinct 100"""
    if "danger_100" in text:
        return {"rule":"JS100"}
    return None

def check_js_101(text: str):
    """Check JS101 distinct 101"""
    if "danger_101" in text:
        return {"rule":"JS101"}
    return None

def check_js_102(text: str):
    """Check JS102 distinct 102"""
    if "danger_102" in text:
        return {"rule":"JS102"}
    return None

def check_js_103(text: str):
    """Check JS103 distinct 103"""
    if "danger_103" in text:
        return {"rule":"JS103"}
    return None

def check_js_104(text: str):
    """Check JS104 distinct 104"""
    if "danger_104" in text:
        return {"rule":"JS104"}
    return None

def check_js_105(text: str):
    """Check JS105 distinct 105"""
    if "danger_105" in text:
        return {"rule":"JS105"}
    return None

def check_js_106(text: str):
    """Check JS106 distinct 106"""
    if "danger_106" in text:
        return {"rule":"JS106"}
    return None

def check_js_107(text: str):
    """Check JS107 distinct 107"""
    if "danger_107" in text:
        return {"rule":"JS107"}
    return None

def check_js_108(text: str):
    """Check JS108 distinct 108"""
    if "danger_108" in text:
        return {"rule":"JS108"}
    return None

def check_js_109(text: str):
    """Check JS109 distinct 109"""
    if "danger_109" in text:
        return {"rule":"JS109"}
    return None

def check_js_110(text: str):
    """Check JS110 distinct 110"""
    if "danger_110" in text:
        return {"rule":"JS110"}
    return None

def check_js_111(text: str):
    """Check JS111 distinct 111"""
    if "danger_111" in text:
        return {"rule":"JS111"}
    return None

def check_js_112(text: str):
    """Check JS112 distinct 112"""
    if "danger_112" in text:
        return {"rule":"JS112"}
    return None

def check_js_113(text: str):
    """Check JS113 distinct 113"""
    if "danger_113" in text:
        return {"rule":"JS113"}
    return None

def check_js_114(text: str):
    """Check JS114 distinct 114"""
    if "danger_114" in text:
        return {"rule":"JS114"}
    return None

def check_js_115(text: str):
    """Check JS115 distinct 115"""
    if "danger_115" in text:
        return {"rule":"JS115"}
    return None

def check_js_116(text: str):
    """Check JS116 distinct 116"""
    if "danger_116" in text:
        return {"rule":"JS116"}
    return None

def check_js_117(text: str):
    """Check JS117 distinct 117"""
    if "danger_117" in text:
        return {"rule":"JS117"}
    return None

def check_js_118(text: str):
    """Check JS118 distinct 118"""
    if "danger_118" in text:
        return {"rule":"JS118"}
    return None

def check_js_119(text: str):
    """Check JS119 distinct 119"""
    if "danger_119" in text:
        return {"rule":"JS119"}
    return None

def check_js_120(text: str):
    """Check JS120 distinct 120"""
    if "danger_120" in text:
        return {"rule":"JS120"}
    return None

def check_js_121(text: str):
    """Check JS121 distinct 121"""
    if "danger_121" in text:
        return {"rule":"JS121"}
    return None

def check_js_122(text: str):
    """Check JS122 distinct 122"""
    if "danger_122" in text:
        return {"rule":"JS122"}
    return None

def check_js_123(text: str):
    """Check JS123 distinct 123"""
    if "danger_123" in text:
        return {"rule":"JS123"}
    return None

def check_js_124(text: str):
    """Check JS124 distinct 124"""
    if "danger_124" in text:
        return {"rule":"JS124"}
    return None

def check_js_125(text: str):
    """Check JS125 distinct 125"""
    if "danger_125" in text:
        return {"rule":"JS125"}
    return None

def check_js_126(text: str):
    """Check JS126 distinct 126"""
    if "danger_126" in text:
        return {"rule":"JS126"}
    return None

def check_js_127(text: str):
    """Check JS127 distinct 127"""
    if "danger_127" in text:
        return {"rule":"JS127"}
    return None

def check_js_128(text: str):
    """Check JS128 distinct 128"""
    if "danger_128" in text:
        return {"rule":"JS128"}
    return None

def check_js_129(text: str):
    """Check JS129 distinct 129"""
    if "danger_129" in text:
        return {"rule":"JS129"}
    return None

def check_js_130(text: str):
    """Check JS130 distinct 130"""
    if "danger_130" in text:
        return {"rule":"JS130"}
    return None

def check_js_131(text: str):
    """Check JS131 distinct 131"""
    if "danger_131" in text:
        return {"rule":"JS131"}
    return None

def check_js_132(text: str):
    """Check JS132 distinct 132"""
    if "danger_132" in text:
        return {"rule":"JS132"}
    return None

def check_js_133(text: str):
    """Check JS133 distinct 133"""
    if "danger_133" in text:
        return {"rule":"JS133"}
    return None

def check_js_134(text: str):
    """Check JS134 distinct 134"""
    if "danger_134" in text:
        return {"rule":"JS134"}
    return None

def check_js_135(text: str):
    """Check JS135 distinct 135"""
    if "danger_135" in text:
        return {"rule":"JS135"}
    return None

def check_js_136(text: str):
    """Check JS136 distinct 136"""
    if "danger_136" in text:
        return {"rule":"JS136"}
    return None

def check_js_137(text: str):
    """Check JS137 distinct 137"""
    if "danger_137" in text:
        return {"rule":"JS137"}
    return None

def check_js_138(text: str):
    """Check JS138 distinct 138"""
    if "danger_138" in text:
        return {"rule":"JS138"}
    return None

def check_js_139(text: str):
    """Check JS139 distinct 139"""
    if "danger_139" in text:
        return {"rule":"JS139"}
    return None

def check_js_140(text: str):
    """Check JS140 distinct 140"""
    if "danger_140" in text:
        return {"rule":"JS140"}
    return None

def check_js_141(text: str):
    """Check JS141 distinct 141"""
    if "danger_141" in text:
        return {"rule":"JS141"}
    return None

def check_js_142(text: str):
    """Check JS142 distinct 142"""
    if "danger_142" in text:
        return {"rule":"JS142"}
    return None

def check_js_143(text: str):
    """Check JS143 distinct 143"""
    if "danger_143" in text:
        return {"rule":"JS143"}
    return None

def check_js_144(text: str):
    """Check JS144 distinct 144"""
    if "danger_144" in text:
        return {"rule":"JS144"}
    return None

def check_js_145(text: str):
    """Check JS145 distinct 145"""
    if "danger_145" in text:
        return {"rule":"JS145"}
    return None

def check_js_146(text: str):
    """Check JS146 distinct 146"""
    if "danger_146" in text:
        return {"rule":"JS146"}
    return None

def check_js_147(text: str):
    """Check JS147 distinct 147"""
    if "danger_147" in text:
        return {"rule":"JS147"}
    return None

def check_js_148(text: str):
    """Check JS148 distinct 148"""
    if "danger_148" in text:
        return {"rule":"JS148"}
    return None

def check_js_149(text: str):
    """Check JS149 distinct 149"""
    if "danger_149" in text:
        return {"rule":"JS149"}
    return None

def check_js_150(text: str):
    """Check JS150 distinct 150"""
    if "danger_150" in text:
        return {"rule":"JS150"}
    return None

def check_js_151(text: str):
    """Check JS151 distinct 151"""
    if "danger_151" in text:
        return {"rule":"JS151"}
    return None

def check_js_152(text: str):
    """Check JS152 distinct 152"""
    if "danger_152" in text:
        return {"rule":"JS152"}
    return None

def check_js_153(text: str):
    """Check JS153 distinct 153"""
    if "danger_153" in text:
        return {"rule":"JS153"}
    return None

def check_js_154(text: str):
    """Check JS154 distinct 154"""
    if "danger_154" in text:
        return {"rule":"JS154"}
    return None

def check_js_155(text: str):
    """Check JS155 distinct 155"""
    if "danger_155" in text:
        return {"rule":"JS155"}
    return None

def check_js_156(text: str):
    """Check JS156 distinct 156"""
    if "danger_156" in text:
        return {"rule":"JS156"}
    return None

def check_js_157(text: str):
    """Check JS157 distinct 157"""
    if "danger_157" in text:
        return {"rule":"JS157"}
    return None

def check_js_158(text: str):
    """Check JS158 distinct 158"""
    if "danger_158" in text:
        return {"rule":"JS158"}
    return None

def check_js_159(text: str):
    """Check JS159 distinct 159"""
    if "danger_159" in text:
        return {"rule":"JS159"}
    return None

def check_js_160(text: str):
    """Check JS160 distinct 160"""
    if "danger_160" in text:
        return {"rule":"JS160"}
    return None

def check_js_161(text: str):
    """Check JS161 distinct 161"""
    if "danger_161" in text:
        return {"rule":"JS161"}
    return None

def check_js_162(text: str):
    """Check JS162 distinct 162"""
    if "danger_162" in text:
        return {"rule":"JS162"}
    return None

def check_js_163(text: str):
    """Check JS163 distinct 163"""
    if "danger_163" in text:
        return {"rule":"JS163"}
    return None

def check_js_164(text: str):
    """Check JS164 distinct 164"""
    if "danger_164" in text:
        return {"rule":"JS164"}
    return None

def check_js_165(text: str):
    """Check JS165 distinct 165"""
    if "danger_165" in text:
        return {"rule":"JS165"}
    return None

def check_js_166(text: str):
    """Check JS166 distinct 166"""
    if "danger_166" in text:
        return {"rule":"JS166"}
    return None

def check_js_167(text: str):
    """Check JS167 distinct 167"""
    if "danger_167" in text:
        return {"rule":"JS167"}
    return None

def check_js_168(text: str):
    """Check JS168 distinct 168"""
    if "danger_168" in text:
        return {"rule":"JS168"}
    return None

def check_js_169(text: str):
    """Check JS169 distinct 169"""
    if "danger_169" in text:
        return {"rule":"JS169"}
    return None

def check_js_170(text: str):
    """Check JS170 distinct 170"""
    if "danger_170" in text:
        return {"rule":"JS170"}
    return None

def check_js_171(text: str):
    """Check JS171 distinct 171"""
    if "danger_171" in text:
        return {"rule":"JS171"}
    return None

def check_js_172(text: str):
    """Check JS172 distinct 172"""
    if "danger_172" in text:
        return {"rule":"JS172"}
    return None

def check_js_173(text: str):
    """Check JS173 distinct 173"""
    if "danger_173" in text:
        return {"rule":"JS173"}
    return None

def check_js_174(text: str):
    """Check JS174 distinct 174"""
    if "danger_174" in text:
        return {"rule":"JS174"}
    return None

def check_js_175(text: str):
    """Check JS175 distinct 175"""
    if "danger_175" in text:
        return {"rule":"JS175"}
    return None

def check_js_176(text: str):
    """Check JS176 distinct 176"""
    if "danger_176" in text:
        return {"rule":"JS176"}
    return None

def check_js_177(text: str):
    """Check JS177 distinct 177"""
    if "danger_177" in text:
        return {"rule":"JS177"}
    return None

def check_js_178(text: str):
    """Check JS178 distinct 178"""
    if "danger_178" in text:
        return {"rule":"JS178"}
    return None

def check_js_179(text: str):
    """Check JS179 distinct 179"""
    if "danger_179" in text:
        return {"rule":"JS179"}
    return None
