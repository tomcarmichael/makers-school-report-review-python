def school_report(results_string):
    results = results_string.split(', ')

    # Handle input without spaces after commas
    if len(results) == 1:
        results = results[0].split(',')

    output = ''

    grades = ('Green', 'Amber', 'Red')

    result_counts = {}

    for grade in grades:
        result_counts[grade] = 0
    
    for result in results:
        formatted_result = result.capitalize()

        if formatted_result in result_counts.keys():
                result_counts[formatted_result] += 1
        else:
            if 'Uncounted' in result_counts.keys():
                result_counts['Uncounted'] += 1
            else:
                result_counts['Uncounted'] = 1
    
    for key in result_counts:
        if result_counts[key] > 0:
            output += f'{key}: {result_counts[key]}\n'
    
    return output.strip()


    # results_list = results_string.split(',')

    # grades = ('Green', 'Amber', 'Red')

    # result_counts = {}

    # for grade in grades:
    #     result_counts[grade] = 0
    
    # result_counts['Uncounted'] = 0

    # for result in results_list:
    #     for grade in grades:
    #         if result.upper() == grade.upper():
    #             result_counts[grade] += 1
    #         else:
    #             result_counts['Uncounted'] += 1

    # output = f''

    # for key in result_counts:
    #     if result_counts[key] > 0:
    #         output += f'{key}: {result_counts[key]}\n'
    
    # return output
        
    

