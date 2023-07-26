def school_report(results_string):
    results = results_string.split(', ')

    # Handle input without spaces after commas
    if len(results) == 1:
        results = results[0].split(',')

    grades = ('Green', 'Amber', 'Red')

    result_counts = {}
    # Add each grade to the results_counts with a starting count of 0
    for grade in grades:
        result_counts[grade] = 0
    
    for result in results:
        result = result.capitalize()

        if result in grades:
            result_counts[result] += 1
        else:
            if 'Uncounted' in result_counts.keys():
                result_counts['Uncounted'] += 1
            else:
                result_counts['Uncounted'] = 1

    output = ''
    for key in result_counts:
        if result_counts[key] > 0:
            output += f'{key}: {result_counts[key]}\n'
    
    return output.strip()  
