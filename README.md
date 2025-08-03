# CC-Mahasena


---

### 🔢 **Code:**

```python
n = int(input())
```

* This reads an integer `n` from the user.
* `n` represents the number of soldiers in the army.

---

```python
weapons = list(map(int, input().split()))
```

* This reads `n` space-separated numbers (number of weapons each soldier has).
* `input().split()` splits the input string into a list of strings.
* `map(int, ...)` converts each string to an integer.
* `list(...)` stores all the integers in the list called `weapons`.

---

```python
even_count = 0
odd_count = 0
```

* These two variables will keep track of how many soldiers have an **even** or **odd** number of weapons.

---

```python
for w in weapons:
```

* Loops through each number `w` in the `weapons` list (i.e., each soldier's weapon count).

---

```python
    if w % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
```

* Checks if `w` is **even** using `w % 2 == 0`:

  * If it is even, add 1 to `even_count`.
  * If it's not (i.e., odd), add 1 to `odd_count`.

---

```python
if even_count > odd_count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
```

* After counting all soldiers:

  * If there are **more even** than odd, print `"READY FOR BATTLE"`.
  * Otherwise, print `"NOT READY"`.

---

### ✅ Example:

#### Input:

```
5
1 2 3 4 5
```

#### Processing:

* even: 2, 4 → `even_count = 2`
* odd: 1, 3, 5 → `odd_count = 3`

#### Output:

```
NOT READY
```

---




---

## 📝 **Python List Methods**

| Method                               | Description                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `list.append(x)`                     | Adds element `x` to the end of the list                                                           |
| `list.extend(iterable)`              | Extends the list by appending elements from the iterable                                          |
| `list.insert(i, x)`                  | Inserts element `x` at position `i`                                                               |
| `list.remove(x)`                     | Removes the first occurrence of `x` from the list                                                 |
| `list.pop([i])`                      | Removes and returns the element at position `i` (default last)                                    |
| `list.clear()`                       | Removes all items from the list                                                                   |
| `list.index(x[, start[, end]])`      | Returns the index of the first occurrence of `x` (optionally searching between `start` and `end`) |
| `list.count(x)`                      | Returns the number of times `x` appears in the list                                               |
| `list.sort(key=None, reverse=False)` | Sorts the list in ascending order (customizable)                                                  |
| `list.reverse()`                     | Reverses the elements of the list in place                                                        |
| `list.copy()`                        | Returns a shallow copy of the list                                                                |

---

### Quick examples:

```python
lst = [3, 1, 2, 3]

lst.append(4)          # [3, 1, 2, 3, 4]
lst.extend([5, 6])     # [3, 1, 2, 3, 4, 5, 6]
lst.insert(1, 10)      # [3, 10, 1, 2, 3, 4, 5, 6]
lst.remove(3)          # Removes first 3 → [10, 1, 2, 3, 4, 5, 6]
lst.pop()              # Removes and returns last → 6, list now [10, 1, 2, 3, 4, 5]
lst.count(3)           # Returns 1
lst.index(4)           # Returns index of first 4 → 4
lst.sort()             # Sorts list → [1, 2, 3, 4, 5, 10]
lst.reverse()          # Reverses list → [10, 5, 4, 3, 2, 1]
lst.copy()             # Returns a shallow copy of the list
lst.clear()            # Empties the list → []
```

---



