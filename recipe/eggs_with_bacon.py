
def eggs_with_bacon(eggs_count, bacon_count=0):
    assert isinstance(eggs_count, int)
    assert isinstance(bacon_count, int)

    if eggs_count <= 0 and bacon_count <= 0:
        return 'empty'

    if eggs_count > 0 and bacon_count <= 0:
        return 'eggs'

    if eggs_count <= 0 and bacon_count > 0:
        return 'bacon'

    if eggs_count > 0 and bacon_count > 0:
        return 'bacon with eggs'
