func lengthOfLastWord(s string) int {
    var ans[]string
    temp := ""
    for _,v := range s {

        if v == ' ' {
            if len(temp) > 0 {
                ans = append(ans,temp)
            }
        temp = ""
        } else {
            temp += string(v)
        }
    }   
    if len(temp) > 0 {
        ans = append(ans,temp)
    }
    return len(ans[len(ans)-1])
}