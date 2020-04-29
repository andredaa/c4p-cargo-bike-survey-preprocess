from openpyxl import Workbook, load_workbook
from headers import orignal_column_headers, question_codes


def rename_headers(sheet):
    sheet["K1"].value = "Randomization Group"

    if "Die kommenden Fragen beziehen sich" in sheet["CG1"].value:
        sheet["CG1"].value = "Wie einfach oder schwierig ist es für Sie, das Lastenrad unterwegs in Hamburg zu parken? (nicht an Ihrem Wohnort)"
    else:
        print("did not replace introduction: Die kommenden Fragen beziehen sich")

    if "Diese Frage bezieht sich auf das Parken von Lastenrädern im öffentlichen Raum" in sheet["FL1"].value:
        sheet["FL1"].value = "Wie einfach oder schwierig stellen Sie es vor, ein Lastenrad unterwegs in Hamburg zu parken? (nicht am Wohnort)"
    else:
        print("did not replace introduction: Diese Frage bezieht sich auf das Parken von Lastenrädern im öffentlichen Raum")

    if "Wir würden gerne auch soziodemografische Daten erheben. " in sheet["FT1"].value:
        sheet["FT1"].value = "Was ist Ihr Geschlecht?"
    else:
        print("did not replace introduction: Wir würden gerne auch soziodemografische Daten erheben.")

    if "Haben Sie vor sich ein eigenes Lastenrad anzuschaffen?" in sheet["DJ1"].value:
        sheet["DJ1"].value = "Haben Sie vor sich ein eigenes Lastenrad zu kaufen?"
    else:
        print("did not replace introduction: Haben Sie vor sich ein eigenes Lastenrad anzuschaffen?")


   # clean headers from double whitespaces etc.
    for cell in sheet[1]:
        cell.value = ' '.join(cell.value.split())
        cell.value.replace(u'\xa0', u' ').strip()



def get_input_workbook():
    return load_workbook(filename="results-survey.xlsx")


def truncate_empty_cells(processed_sheet):
    for row in processed_sheet.iter_rows(min_row=2,
                                         min_col=1,
                                         ):
        for column in range(len(row)):
            if row[column].value == "N/A":
                row[column].value = None


def check_sheet_format(sheet):
    for column in sheet.iter_cols(min_col=1, min_row=1, max_row=1):
        for cell in column:
            # remove duplicate whitespaces
            cell.value = ' '.join(cell.value.split())
            if cell.value.replace(u'\xa0', u' ').strip() != orignal_column_headers[cell.column].replace(u'\xa0',
                                                                                                        u' ').strip():
                print("ERROR: column does not have expected header")
                print("column id:", cell.column)
                print("column header", cell.value)
                print("expected header", orignal_column_headers[cell.column])


def summarize_challenges_for_cargo_bikes(sheet):
    summary_columns_names = orignal_column_headers[25:35]

    for row in sheet.iter_rows(min_row=2, min_col=25, max_col=74):
        for cell in row:
            if cell.value is not None:
                # identify in which summary column to write the value
                column_header = sheet.cell(row=1, column=cell.column).value
                summary_column_id = summary_columns_names.index(column_header) + 24
                # write value to summary columns
                sheet.cell(row=cell.row, column=summary_column_id).value = cell.value

    return sheet["Y1:AH4"]


# some questions are asked multiple times. this function groups all results as a single question
def group_duplicate_questions(sheet, resulting_columns, duplicate_question_columns):
    # get the column headers for the resulting columns
    summary_columns_names = orignal_column_headers[resulting_columns[0]: (resulting_columns[1] + 1)]
    columns_to_delete.append(duplicate_question_columns)

    for row in sheet.iter_rows(min_row=2, min_col=duplicate_question_columns[0], max_col=duplicate_question_columns[1]):
        for cell in row:
            if cell.value is not None:
                column_header = sheet.cell(row=1, column=cell.column).value
                print(column_header)
                # try to find the current column header in the questions to be summarized.
                summary_column = summary_columns_names.index(column_header) + (resulting_columns[0])  # TODO: writing to the right cell?
                # copy value to summary columns
                sheet.cell(row=cell.row, column=summary_column).value = cell.value



def delete_superfluous_columns(sheet):

    # sort columns highest to lowest
    columns_to_delete.sort(key=lambda x: x[0], reverse=True)

    for section in columns_to_delete:
        delete_from = section[0]
        section_length = section[1] - section[0] + 1
        sheet.delete_cols(idx=delete_from, amount=section_length)


def export_question_times_to_separate_sheet():
    times_sheet = input_wb.copy_worksheet(input_wb.active)
    input_wb.active = times_sheet
    input_wb.active.title = "question_times"

    col_to_keep = [
        237,
        232,
        226,
        220,
        212,
        201,
        195,
        191,
        190,
        3,
        1
    ]

    # delete all columns that do not contain questions times
    for col in range(times_sheet.max_column + 1, 1, -1):
        if col not in col_to_keep:
            times_sheet.delete_cols(idx=col, amount=1)

    # set processed sheet back as active sheet
    input_wb.active = processed_sheet


def add_question_and_subquestion_ids_to_cols(sheet):
    # add 2 rows for question_id and subquestion_id
    sheet.insert_rows(idx=1, amount=2)
    for cell in sheet[3]:
        header = cell.value
        for entry in question_codes:
            if entry[2] == header:
                # set question code
                sheet.cell(row=1, column=cell.column).value = entry[0]
                # set subquestion code or None
                sheet.cell(row=2, column=cell.column).value = entry[1]
                break
        else:
            # Didn't find anything..
            print("could not find question code for ", header)
            exit()


def export_question_ids():
    question_codes_sheet = input_wb.copy_worksheet(input_wb.active)
    input_wb.active = question_codes_sheet
    input_wb.active.title = "question_codes"

    sheet = input_wb.active
    sheet.cell(row=1, column=1).value = "Question_IDs"
    sheet.cell(row=1, column=2).value = "Question_text"
    sheet.cell(row=1, column=3).value = "Sub_Question_ID"
    sheet.cell(row=1, column=4).value = "Sub_Question_text"

    listed_questions = []
    row_it = 2

    for entry in question_codes:
        if entry[0] not in listed_questions:
            listed_questions.append(entry[0])
            sheet.cell(row=row_it, column=1).value = entry[0]
            sheet.cell(row=row_it, column=2).value = entry[2].rsplit('[', 1)[0]
            sheet.cell(row=row_it, column=3).value = None
            sheet.cell(row=row_it, column=4).value = None
            row_it += 1
        else:
            sheet.cell(row=row_it, column=1).value = None
            sheet.cell(row=row_it, column=2).value = None
            sheet.cell(row=row_it, column=3).value = entry[1]
            sheet.cell(row=row_it, column=4).value = entry[2].rsplit('[', 1)[len(entry[2].rsplit('[', 1)) - 1]
            row_it += 1


    input_wb.active.delete_cols(5, amount=300)
    input_wb.active.delete_rows(row_it + 1, amount=300)

    # set processed sheet back as active sheet
    input_wb.active = processed_sheet


if __name__ == '__main__':
    input_wb = get_input_workbook()
    input_wb.active.title = "raw_data"

    processed_sheet = input_wb.copy_worksheet(input_wb.active)
    input_wb.active = processed_sheet
    processed_sheet.title = "processed_data"

    check_sheet_format(processed_sheet)

    truncate_empty_cells(processed_sheet)

    # group_duplicate_columns(processed_sheet)
    columns_to_delete = [
        [190, 243],
        [9, 9],
        [4, 4]
    ]

    rename_headers(processed_sheet)

    # summarize challenges
    group_duplicate_questions(processed_sheet, [25, 34], [35, 74])

    # summarize improvements
    group_duplicate_questions(processed_sheet, [75, 76], [77, 84])

    # summarize criteria
    group_duplicate_questions(processed_sheet, [96, 100], [101, 105])

    # summarize criteria (non-user)
    group_duplicate_questions(processed_sheet, [96, 100], [171, 174])

    # summarize imagined challenges [non-user]
    group_duplicate_questions(processed_sheet, [118, 127], [128, 167])

    # summarize hurdles in purchase
    group_duplicate_questions(processed_sheet, [23, 24], [115, 116])

    # summarize "Kennen Sie den lastenradstellplatz"
    group_duplicate_questions(processed_sheet, [95, 95], [169, 169])

    # summarize "Haben Sie Vorschläge..."
    group_duplicate_questions(processed_sheet, [107, 107], [175, 175])

    export_question_times_to_separate_sheet()

    export_question_ids()

    delete_superfluous_columns(processed_sheet)

    add_question_and_subquestion_ids_to_cols(processed_sheet)

    # TODO Test if all cells are filled in that should be filled

    # if no answer becuse dropped out early - they which answers are empty (one column)

    input_wb.save('final.xlsx')
    print("finished!")