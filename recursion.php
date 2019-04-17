<?php
function fact($x){
    if($x == 1){    //基线条件，这个条件会停止递归
        return 1;
    } else{        //递归条件，这个条件会一直调用递归
        return $x * fact($x - 1);
    }
}

for($i=0; $i<1000000; $i++){
    fact(20);
}
