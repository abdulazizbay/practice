# I-TASK (PYTHON)

# Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"

def get_digits(str):
    nums = []
    for char in str:
        if char.isdigit():
            nums.append(char)
    return "".join(nums)

print(get_digits("m14i1t"))













# # // G-TASK (PYTHON)

# # // Shunday function tuzingki unga integerlardan iborat array pass bolsin
# # va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# # // MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.


# def get_highest_index(arr):
#     highestNum = sorted(arr)[len(arr)-1]
#     return arr.index(highestNum)


# print(get_highest_index([5, 21, 12, 21, 8]))
