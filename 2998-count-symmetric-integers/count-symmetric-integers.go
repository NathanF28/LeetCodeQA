func countSymmetricIntegers(low int, high int) int {
    count := 0
    for i:= low; i < high+1;i++ {
        check := fmt.Sprintf("%d",i)
        if len(check) % 2 == 1{
            continue 
        } 
            mid := len(check) / 2
            sum1 := 0
            sum2 := 0 
            for j:= 0; j < mid; j++ {
                sum1+= int(check[j] - '0')
            }
            for j:= mid; j < len(check); j++ {
                sum2+= int(check[j] - '0')
            }
            if sum1 == sum2 {
                count++
        }
    }    
    return count
}  