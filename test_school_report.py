from school_report import school_report 

def test_school_report_result_1():
    input = "Green"
    assert(school_report(input)) == 'Green: 1'

def test_school_report_result_2():
    input = "Red"
    assert(school_report(input)) == 'Red: 1'

def test_school_report_result_3():
    input = "Amber"
    assert(school_report(input)) == 'Amber: 1'