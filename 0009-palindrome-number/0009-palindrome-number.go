func isPalindrome(x int) bool {
   arr := strconv.Itoa(x)
   l := 0
   r := len(arr) -1
   for l < r {
    if arr[l] != arr[r] {
        return false
    }
    r--
    l++
   }

    return true

}