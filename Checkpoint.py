unction is_palindrome(word):
    start = 0
    end = length(word) - 1

    while start <= end:
        if word[start] == word[end]:
            start = start + 1
            end = end - 1
        else:
            return False

    if length(word) <= 1:
        return True
    else:
        return True
