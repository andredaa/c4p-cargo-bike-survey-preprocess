from questions import all_questions


def find_identifiers_for_group_name(group_name):
    for group in group_identifiers:
        if group[0] == group_name:
            return group[1]

    return [None]


def find_relevant_questions_for_group_name(group_name):
    for group in relevant_questions:
        if group[0] == group_name:
            return group[1]

    return [None]


# list of group names in grouping
groupings = [
    ["cargo-riders", "no-riding-experience-group", "cargo-test-riders", "no-cargo-riders"],
    ["cargo-riders", "could-imagine-riding"],
    ["regular-riders", "seldom-riders"],
    ["people-from-altona"]
    # todo? ["daily-cargo-riders", "", ""]
]

# group name,  [identifying question, [identifying answers]]
group_identifiers = [
        ["cargo-riders", [["AA01A", ["Ja, mehrfach"]]]],
        ["no-riding-experience-group", [["AA01A", ["Nur zur Probe- oder Testfahrt", "Nein, niemals"]]]],
        ["cargo-test-riders", [["AA01A", ["Nur zur Probe- oder Testfahrt"]]]],
        ["no-cargo-riders", [["AA01A", ["Nein, niemals"]]]],
        ["could-imagine-riding", [["CN01A", ["Ja"]]]],
        ["regular-riders", [["BN01A", ["Täglich", "Wöchentlich oder öfter"]]]],
        ["seldom-riders", [["BN01A", ["Weniger als einmal im Monat", "Monatlich oder öfter"]]]],
        ["people-from-altona", [["AD02A", ["Ottensen", 22765, "Altona-Nord", "Altona-Altstadt","Altona"]]]],
]

# group name, list of relevant questions
# for now relevant questions are the same for the user-groups ["cargo-riders", "regular-riders", "seldom-riders"]
# and all non-user groups ["cargo-test-riders", ""could-imagine-riding", ...]
relevant_questions = [
    ["cargo-riders", [
        "AA01A",
        "RAND",
        "BN01A",
        "BN02A",
        "BN03A",
        "BN03B",
        "BN03C",
        "BN03C",
        "BH01A1",
        "BH02A1",
        "BE01A",
        "BE02A",
        "BE03A",
        "BE03B1",
        "BE03C",
        "BE03D",
        "AD01A",
        "AD02A",
        "AD03A",
        "AD04A",
        "AD05A",
        "AD06A"
    ]],
    ["regular-riders", [
        "AA01A",
        "RAND",
        "BN01A",
        "BN02A",
        "BN03A",
        "BN03B",
        "BN03C",
        "BN03C",
        "BH01A1",
        "BH02A1",
        "BE01A",
        "BE02A",
        "BE03A",
        "BE03B1",
        "BE03C",
        "BE03D",
        "AD01A",
        "AD02A",
        "AD03A",
        "AD04A",
        "AD05A",
        "AD06A"
    ]],
    ["seldom-riders", [
        "AA01A",
        "RAND",
        "BN01A",
        "BN02A",
        "BN03A",
        "BN03B",
        "BN03C",
        "BN03C",
        "BH01A1",
        "BH02A1",
        "BE01A",
        "BE02A",
        "BE03A",
        "BE03B1",
        "BE03C",
        "BE03D",
        "AD01A",
        "AD02A",
        "AD03A",
        "AD04A",
        "AD05A",
        "AD06A"
    ]],
    ["no-riding-experience-group", [
        "AA01A",
        "RAND",
        "CN01A",
        "CN01B",
        "CN01C",
        "CN01D",
        "CN02A",
        "CH01A1",
        "CE01A",
        "CE02A",
        "CE03B",
        "CE03D",
        "AD01A",
        "AD02A",
        "AD03A",
        "AD04A",
        "AD05A",
        "AD06A"
    ]],
    ["cargo-test-riders", [
        "AA01A",
        "RAND",
        "CN01A",
        "CN01B",
        "CN01C",
        "CN01D",
        "CN02A",
        "CH01A1",
        "CE01A",
        "CE02A",
        "CE03B",
        "CE03D",
        "AD01A",
        "AD02A",
        "AD03A",
        "AD04A",
        "AD05A",
        "AD06A"
    ]],
    ["no-cargo-riders", [
        "AA01A",
        "RAND",
        "CN01A",
        "CN01B",
        "CN01C",
        "CN01D",
        "CN02A",
        "CH01A1",
        "CE01A",
        "CE02A",
        "CE03B",
        "CE03D",
        "AD01A",
        "AD02A",
        "AD03A",
        "AD04A",
        "AD05A",
        "AD06A"
    ]],
    ["could-imagine-riding", [
        "AA01A",
        "RAND",
        "CN01A",
        "CN01B",
        "CN01C",
        "CN01D",
        "CN02A",
        "CH01A1",
        "CE01A",
        "CE02A",
        "CE03B",
        "CE03D",
        "AD01A",
        "AD02A",
        "AD03A",
        "AD04A",
        "AD05A",
        "AD06A"
    ]],
    ["people-from-altona", all_questions]
]