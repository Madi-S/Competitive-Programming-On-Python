def run(tricks):
    result = {}
    for trick in tricks:
        points = 0
        n_times_performed = 0
        curr_expected_points = 0

        while True:
            points += trick['points'] * (trick['mult_base'] ** n_times_performed)
            prev_expected_points = curr_expected_points
            curr_expected_points = trick['probability'] ** n_times_performed * points

            if curr_expected_points < prev_expected_points:
                result[trick['name']] = n_times_performed
                break
            
            n_times_performed += 1

    return result


args = [{'name': 'kickflip', 'points': 100,
         'mult_base': .8, 'probability': .85}]
print(run(args))
