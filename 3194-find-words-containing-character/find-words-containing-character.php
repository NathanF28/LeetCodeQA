class Solution {

    /**
     * @param String[] $words
     * @param String $x
     * @return Integer[]
     */
    function findWordsContaining($words, $x) {
        $final = array();
        for ($i = 0; $i < count($words); $i++){
            if (strpos($words[$i],$x) !== false){
                array_push($final,$i);
            }
        }
        return $final;
    }
}