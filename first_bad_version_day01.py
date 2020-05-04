__author__ = "saimadhu.polamuri"


def first_bad_version(n):
    """
    :type n: int
    :rtype: int
    """

    if n < 2:
        return n
    start = 1
    end = n

    while (start <= end):
        mid = (start + end) // 2

        if isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        elif isBadVersion(mid - 1):
            end = mid - 1
        else:
            start = mid + 1

