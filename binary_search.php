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
            echo $i."\n";
            return $mid;
        }

        if($guess > $v){
            $high = $mid - 1;
        }

        if($guess < $v){
            $low = $mid + 1;
        }
    }

    echo $i." <<\n";
    return;
}

$list = [1, 2, 3, 4, 5, 6, 9, 30, 221, 244, 332];
$id = bs($list, 9);
var_dump($id);

$id = bs($list, 221);
var_dump($id);

$id = bs($list, 10);
var_dump($id);

$id = bs($list, 5);
var_dump($id);

$id = bs($list, 6);
var_dump($id);



/***
 * 2分查找的时间复杂度不会超过 O(logN)
 *
 * 上面数组共11个元素，所以最多 ceil(log(11, 2)) = 4 次
 */
