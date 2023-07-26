from school_report import school_report 
import pytest

def test_school_report_result_1():
    input = "Green"
    assert(school_report(input)) == 'Green: 1'

def test_school_report_result_2():
    input = "Red"
    assert(school_report(input)) == 'Red: 1'

def test_school_report_result_3():
    input = "Amber"
    assert(school_report(input)) == 'Amber: 1'

def test_school_report_result_4():
    input = "Green, Amber"
    assert(school_report(input)) == 'Green: 1\nAmber: 1'

def test_school_report_result_5():
    input = "Green, Amber, Red"
    assert(school_report(input)) == 'Green: 1\nAmber: 1\nRed: 1'

def test_school_report_result_6():
    input = "Green, Green, Amber, Red, Green"
    assert(school_report(input)) == 'Green: 3\nAmber: 1\nRed: 1'

def test_school_report_result_6():
    input = "Green, Green, Amber"
    assert(school_report(input)) == 'Green: 2\nAmber: 1'

def test_school_report_result_6():
    input = "Green, Green, Red, Red, Red"
    assert(school_report(input)) == 'Green: 2\nRed: 3'

def test_school_report_result_6():
    input = "GREEN, green, rEd, reD, Red"
    assert(school_report(input)) == 'Green: 2\nRed: 3'

def test_school_report_result_6():
    input = "GREEN, green, rEd, reD, Red, Bob, steve"
    assert(school_report(input)) == 'Green: 2\nRed: 3\nUncounted: 2'