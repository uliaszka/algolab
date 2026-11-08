from algorithms.duplicates import contains_duplicates

def test_contains_duplicates():
    nums=[1,2,3,1]
    result=contains_duplicates(nums)

    assert result == True

def test_no_duplicates():
    nums=[1,2,3,4]
    result=contains_duplicates(nums)

    assert result  == False
