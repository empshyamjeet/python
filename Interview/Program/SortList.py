def sort_list(lst):
    """
    Sorts a list in ascending order.

    Args:
        lst (list): The list to sort.

    Returns:
        list: A new sorted list.
    """
    return sorted(lst)

# Example usage:
if __name__ == "__main__":
    sample_list = [5, 2, 9, 1, 5, 6]
    print("Original list:", sample_list)
    print("Sorted list:", sort_list(sample_list))