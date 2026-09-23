no_of_eggs = int(input("Input number of eggs you have - "))
full_boxes = (no_of_eggs // 12)
remain_eggs = (no_of_eggs % 12)
print(f"Number of boxes you needed - {full_boxes} "
      f"\nNo of eggs remains - {remain_eggs}" 
      f"\nAll boxes needed - {(no_of_eggs + 11) // 12}")