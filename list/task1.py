def remove_duplicates(original_list):
    seen = set()
    result = []
    for item in original_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result




