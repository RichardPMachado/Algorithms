def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    # if None in (permanence_period, target_time):
    #     return None
    try:
        result = 0
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                result += 1
        # print(permanence_period)
        # print(result)
        return result
    except TypeError:
        return None
