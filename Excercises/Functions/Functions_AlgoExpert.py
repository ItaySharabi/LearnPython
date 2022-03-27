"""
בהינתן שני מערכים לא ריקים של מספרים שלמים, כתוב פונקציה שקובעת אם המערך השני הוא תת רצף של הראשון.
תת רצף של מערך הוא אוסף של מספרים שאינם בהכרח סמוכים במערך, אך נמצאים באותו סדר כפי שהם מופיעים במערך.
לדוגמה, המספרים [4, 3, 1] יוצרים תת-רצף של המערך [4, 3, 2, 1], וכך המספרים [4, 2].
שימו לב שמספר בודד במערך והמערך עצמו הם שניהם תתי-רצפים חוקיים של המערך.
"""


def is_subsequence(array: list, subsequence: list):
    arr_size = len(array)
    seq_size = len(subsequence)

    i = j = 0  # אינדקסים לריצה על המערכים

    while i < arr_size and j < seq_size:  # לולאה שמוגבלת בגודל של שני המערכים יחד
        if array[i] == subsequence[j]:  # נחפש שוויון
            # print(f'{array[i]} == {subsequence[j]}')
            if j == seq_size - 1:
                return True
            j += 1
        i += 1

    return False


arr = [1, 2, 3, 4]
seq = [1, 2, 3, 4, 4]

print(f'is_subsequence({arr}, {seq}) = {is_subsequence(arr, seq)}')  # Prints True

arr = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [1, 6, -1, 10]

print(f'is_subsequence({arr}, {seq}) = {is_subsequence(arr, seq)}')  # Prints True
