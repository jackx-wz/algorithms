<?php

function findSmallest($list){
    $smallest = current($list);
    $smallestIndex = key($list);

    foreach($list as $k => $v){
        if($smallest > $v){
            $smallest = $v;
            $smallestIndex = $k;
        }
    }

    return [
        $smallestIndex,
        $smallest,
    ];
}

function selectionSort($list){
    $newList = [];

    while(count($list) > 0){
        var_dump(array_values($list));
        list($smallestIndex, $smallest) = findSmallest($list);
        $newList[] = $smallest;
        unset($list[$smallestIndex]);
    }

    return $newList;
}

$list = [2, 5, 3, 11, 52, 54, 66, 23];
var_dump(selectionSort($list));


/**
 * 选择排序，先按照规则选择最大或最小值
 * 然后将其放入新数组，最后返回新数组
 */
