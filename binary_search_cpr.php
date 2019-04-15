<?php
function bs($list, $v){
    $low = 0;
    $high = count($list) - 1;
    $i = 0;

    while($low <= $high){     //只要还有2个以上就会找到中间那个数进行比较
        $i++;
        $mid = floor(($low+$high)/2);    //ceil 与 floor 效果一样
        $guess = $list[$mid];

        if($guess == $v){
            return $mid;
        }

        if($guess > $v){
            $high = $mid - 1;
        }

        if($guess < $v){
            $low = $mid + 1;
        }
    }

    return;
}

$list = [1, 2, 3, 4, 5, 6, 9, 30, 221, 244, 332];

for($i=0; $i<1000000; $i++){
    $id = bs($list, rand(1, 332));
}



/***
 * 2分查找的时间复杂度不会超过 O(logN)
 *
 * 上面数组共11个元素，所以最多 ceil(log(11, 2)) = 4 次
 *
 * php binary_search_cpr.php  0.57s user 0.02s system 97% cpu 0.608 total
 */
